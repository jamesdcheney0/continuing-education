FROM scratch 
COPY writedata /
CMD ["/writedata", "/logs/myapp"]

# based on scratch image
# copy go binary in this directory to the root docker directory

# to build the image, docker build -t "scratch_volume" .  

# docker bind mounts
# to run it: 
# docker run -d --mount type=bind,src="/Users/jamescheney/Documents/1000-hours/docker/ca-introduction-to-docker/storage",dst=/logs scratch_volume
# the output of the data is written to /Users/jamescheney/Documents/1000-hours/docker/ca-introduction-to-docker/storage/myapp, and the last 30 lines can be viewed with `tail -n 30 /Users/jamescheney/Documents/1000-hours/docker/ca-introduction-to-docker/storage/myapp`
# `cat /Users/jamescheney/Documents/1000-hours/docker/ca-introduction-to-docker/storage/myapp | cut -d " " -f 2 | sort | uniq` to see which unique container IDs wrote to the myapp file 

# docker volumes
# docker run -d --mount type=volume,src="logs",dst=/logs scratch_volume
# if the volume 'logs' doesn't exist, docker creates it
# `docker volume ls` to view it
# `docker volume inspect logs` to get JSON information about where the volume lives 