# Docker
- docker client is the CLI part, docker daemon runs the processes & does the coordination stuff
- namespaces help w process isolation: pid, net, ipc, mat, uts
- control groups allow limits to be set on processes so they don't take up too many resources
- create & execute a container
    - `sudo docker run -it ubuntu /bin/bash`
        - go to interactive (`-i`) terminal (`-t`) using the `ubuntu` image running bash shell (`/bin/bash`)   
            - when exiting bash, container will be stopped
- images live in `/var/lib/docker` 
    - images download automatically if not cached locally
- images vs containers (executable vs running application, respectively)
    - image: template of container
        - layers to this that add add'l features
        - images IDs are a truncated version of the SHA256 name of its binary
    - container commands 
        - `docker ps` to list running containers
            - `docker ps -a` to list all containers
        - `docker start <container name>` start a stopped container
        - `docker attach <container name>` get into running container 
- images from dockerfile
    - `docker container prune` nukes all docker containers
    - `docker container rm` remove containers one by one
    - use Dockerfile to create bespoke images
        - `docker build <Dockerfile directory path>`
            - have to build Dockerfile to use as an image 
            - `-t <tag-name>` append to the command to tag the image w repository name & by default, tagged with `latest`
    - `docker rmi <image id>` to remove docker images 
- images from container
    - recommended to use Dockerfile instead, since it's more of an IaC approach
    - `docker commit <container-id> <repository-tag>`
        - takes a container, and whatever changes were made in it, and creates a new image
        - by default, uses the access method of the image it is based on
            - e.g. the ubuntu container expects `/bin/bash`
            - to override that, `docker commit --change='CMD[commands to run]' <container-id> <repo-tag>`
- `docker kill $(docker ps -q)` delete all running docker containers

# Port Mapping
- `docker run -d <image>` to run containers in background 
- `docker inspect <container-id>` to get info about container including IP
- can curl that IP and the specific port to see the running web app
    - can also map port to port on localhost
    - `docker run -d -P <image-id>`
        - will run a detatched container and attach the docker port to a port on local host
        - `docker ps -a` will show which port is mapped
            - instead of the `0.0.0.0:<port>` that's listed, can use `localhost:<port>`
- `docker stop <container-id>` can accept multiple container IDs, separated w spaces
- can manually assign host(local) port to exposed docker port
    - `docker run -d -p 3000:8080 <image_id>`
        - attach local host port `3000` to docker container port `8080`

# Networking
- bridge network: default networking; don't need to use `--network=`
- ctrl+p, ctrl+q to exit from a container and leave it running. Does not work in VSCode
- I created two containers with `docker run -it ubuntu_networking`, after following the steps in the comments in`./ca-introduction-to-docker/networking/Dockerfile` and they're able to communicate b/w themselves, but I'm not able to ping them from localhost, although according to the training, I should be able to 
- host networking
    - no isolation b/w host and containers 
    - `docker run -d --network=host ubuntu_networking /webapp`
        - it does not get its own IP address and is reliant on the localhost networking 
- docker desktop doesn't play as nice as linux
    - cannot ping containers
    - to get to the container, had to create it with `docker run -d -p 80:8080 ubuntu_networking /webapp` and access it with `curl localhost:80`
- none network
    - only interface is the loopback interface, and no comms built in 

# Volumes
- bind mounts
    - need to know exact path on host to mount on container
    - useful for 
        - sharing config files from host machine to containers
        - sharing source code or build artifacts b/w dev env on docker host + container
        - when file or dir structure of docker host is going to be consistent w the bind mounts the containers require (meaning, it's not very portable)
    - downside: not decoupled from the host
    - `--mount type=bind,src="/local/machine/path",dst=/logs`
        - have to define local host path, then the dst (destination) path in the container will append the dir defined in it to the one defined on localhsot 
- volumes
    - preferred way to persist data
    - docker manages the storage on the host; don't need to know the underlying data path
    - friendlier to use cross-platform (vs bind mounts)
    - `--mount type=volume,src="logs", dst=/logs`
        - if the volume doesn't exist, docker creates it, and it can be checked with `docker volume ls` and the path can be found with `docker volume inspect <volume-name>`
- in-memory storage (tmpfs)
    - for when data should be ephemeral
    - allows for file-system access for the life on the container; good for secrets 
    - `--mount type=tmpfs,dst=/logs`
        - don't have to define location on localhost since the storage doesn't persist 
        - the docker directory shows on the local filesystem, but only as long as the container is running 

# Tagging 
- tags provide way of identifying specific version of an image 
- image can have more than one tag 
- `docker build -t "tag_demo" .`
    - with -t, can specify registries other than the default docker registry 
    - by default, docker tags with 'latest' 
    - `docker tag tag_demo:latest tag_demo:v1`
        - to rename the formerly made image and define a version tag
        - could be renamed something different in the second 'tag_demo', just same for demo purposes here 
- by default, docker runs the image with the latest tag, unless mentioned otherwise. 
    - when making increased versions, e.g., to v2, have to update the latest tag as well. 
        - in the e.g., he made a v2 container, and when he ran :latest, it picked up the :latest tagged image, which was still aligned with v1 
    - if the tag is not defined, latest will just apply to the latest revision of the image 
- outside of dev environments, it's best practice to use bespoke tags 
## Pushing image to dockerhub 
- `docker login` (after making accout on dockerhub)
- `docker push tag_demo:latest` doesn't work; it's not specific enough
    - `docker tag tag_demo:latest <username>/tag_demo:latest` - to tag to user-specific dockerhub account 
    - `docker push <username>/tag_demo`


# Misc Lab experimenting
- discovered that `docker build -t image_name .` needs the dot (or directory) specified to do things 
- if it fails somewhere in the dockerfile, it won't make the image 
- grabbed docker ip with `ip addr show`: 172.17.0.2/16, removed the /16, and was able to ping it 
- to install go, had to use wget instead of curl 
    - used the following guide: https://linuxize.com/post/how-to-install-go-on-centos-7/
- `docker exec <container name> ls <dir/path>` list file within docker container 
- run a container with the name 'web-server' detached (don't automatically go into the container bash) and assign port 8080 on the container to port 80 on the localhost and define the image and version of the image 
    - `docker run --name web-server -d -p 8080:80 nginx:1.12` 

# Container Orchestration with Docker Swarm Mode 