FROM ubuntu:16.04

RUN apt update && apt install -y \
    arp-scan \
    iputils-ping \
    iproute2

COPY webapp /

CMD ["/bin/bash"]

# on Linux: 
# to create an image, ran `docker build -t ubuntu_networking` 
# to create a docker container, ran `docker run -it ubuntu_networking` and was able to run `ip addr show` and `ping google.com` w/n the container to demonstrate it is connected to the internet via a bridge networking connection 
# in the docker bash, type `ip addr show` to list the container's networking info
# ping the container from the host with `ping <container-ip>`

# on macOS: 
# cannot ping containers w docker desktop on macOS
# to get to the container, create it with `docker run -d -p 80:8080 ubuntu_networking /webapp` and access with `curl localhost:80`