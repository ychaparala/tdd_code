#!/bin/bash

# 1) Installing Docker


### Install necessary certificates to download Docker images securely

sudo apt-get update
sudo apt-get install -y apt-transport-https ca-certificates wget software-properties-common

# Get the cryptographic (GPG) key for associated with Docker

wget https://download.docker.com/linux/debian/gpg 
sudo apt-key add gpg

# Add the official Docker repo to the packages searched by apt-get

echo "deb [arch=amd64] https://download.docker.com/linux/debian $(lsb_release -cs) stable" | sudo tee -a /etc/apt/sources.list.d/docker.list

sudo apt-get update

sudo apt-cache policy docker-ce

#ra  sudo apt-cache policy docker-ce
#docker-ce:                                                                        
#  Installed: 5:19.03.1~3-0~debian-stretch
#  Candidate: 5:19.03.1~3-0~debian-stretch                                         
#  Version table:                     
# *** 5:19.03.1~3-0~debian-stretch 500                                             
#        500 https://download.docker.com/linux/debian stretch/stable amd64 Packages
#        100 /var/lib/dpkg/status                                                  
#     5:19.03.0~3-0~debian-stretch 500
#        500 https://download.docker.com/linux/debian stretch/stable amd64 Packages
#     5:18.09.8~3-0~debian-stretch 500
#        500 https://download.docker.com/linux/debian stretch/stable amd64 Packages
#     5:18.09.7~3-0~debian-stretch 500
#        500 https://download.docker.com/linux/debian stretch/stable amd64 Packages
#     5:18.09.6~3-0~debian-stretch 500
#        500 https://download.docker.com/linux/debian stretch/stable amd64 Packages
#     5:18.09.5~3-0~debian-stretch 500
#        500 https://download.docker.com/linux/debian stretch/stable amd64 Packages
#     5:18.09.4~3-0~debian-stretch 500
#        500 https://download.docker.com/linux/debian stretch/stable amd64 Packages
#     5:18.09.3~3-0~debian-stretch 500



# Install Docker

sudo apt-get -y install docker-ce


# Managing Docker services

# start Docker service
sudo systemctl start docker

# stop Docker service
sudo systemctl stop docker

# restart Docker service
sudo systemctl restart docker

# check Docker service status
sudo systemctl status docker

#ra  sudo systemctl status docker
#● docker.service - Docker Application Container Engine
#   Loaded: loaded (/lib/systemd/system/docker.service; enabled; vendor preset: enabled)
#   Active: active (running) since Wed 2019-07-31 19:53:34 CDT; 40min ago
#     Docs: https://docs.docker.com
# Main PID: 833 (dockerd)
#    Tasks: 9
#   Memory: 124.4M
#      CPU: 737ms
#   CGroup: /system.slice/docker.service
#           └─833 /usr/bin/dockerd -H fd:// --containerd=/run/containerd/containerd.sock
#
#Jul 31 19:53:31 carter dockerd[833]: time="2019-07-31T19:53:31.401088436-05:00" level=warning msg="Your kernel does not support swap memory limit"
#Jul 31 19:53:31 carter dockerd[833]: time="2019-07-31T19:53:31.401544895-05:00" level=warning msg="Your kernel does not support cgroup rt period"
#Jul 31 19:53:31 carter dockerd[833]: time="2019-07-31T19:53:31.401840993-05:00" level=warning msg="Your kernel does not support cgroup rt runtime"
#Jul 31 19:53:31 carter dockerd[833]: time="2019-07-31T19:53:31.402205417-05:00" level=info msg="Loading containers: start."
#Jul 31 19:53:33 carter dockerd[833]: time="2019-07-31T19:53:33.871573710-05:00" level=info msg="Default bridge (docker0) is assigned with an IP address 172.17.0.0/16. Daemon
#Jul 31 19:53:33 carter dockerd[833]: time="2019-07-31T19:53:33.983973375-05:00" level=info msg="Loading containers: done."
#Jul 31 19:53:34 carter dockerd[833]: time="2019-07-31T19:53:34.465936142-05:00" level=info msg="Docker daemon" commit=74b1e89 graphdriver(s)=overlay2 version=19.03.1
#Jul 31 19:53:34 carter dockerd[833]: time="2019-07-31T19:53:34.481634518-05:00" level=info msg="Daemon has completed initialization"
#Jul 31 19:53:34 carter systemd[1]: Started Docker Application Container Engine.
#Jul 31 19:53:34 carter dockerd[833]: time="2019-07-31T19:53:34.566843704-05:00" level=info msg="API listen on /var/run/docker.sock"



# Autostart Docker upon reboot
sudo systemctl enable docker

# Run the nice default hello-world image
sudo docker run hello-world

#ra  sudo docker run hello-world
#
#Hello from Docker!
#This message shows that your installation appears to be working correctly.
#
#To generate this message, Docker took the following steps:
# 1. The Docker client contacted the Docker daemon.
# 2. The Docker daemon pulled the "hello-world" image from the Docker Hub.
#    (amd64)
# 3. The Docker daemon created a new container from that image which runs the
#    executable that produces the output you are currently reading.
# 4. The Docker daemon streamed that output to the Docker client, which sent it
#    to your terminal.
#
#To try something more ambitious, you can run an Ubuntu container with:
# $ docker run -it ubuntu bash
#
#Share images, automate workflows, and more with a free Docker ID:
# https://hub.docker.com/
#
#For more examples and ideas, visit:
# https://docs.docker.com/get-started/

# 3) Check your installation

docker --version

#ra  docker --version
#Docker version 19.03.1, build 74b1e89

docker info

# ra  docker info
#Client:
# Debug Mode: false
#
#Server:
# Containers: 3
#  Running: 0
#  Paused: 0
#  Stopped: 3
# Images: 1
# Server Version: 19.03.1
# Storage Driver: overlay2
#  Backing Filesystem: extfs
#  Supports d_type: true
#  Native Overlay Diff: true
# Logging Driver: json-file
# Cgroup Driver: cgroupfs
# Plugins:
#  Volume: local
#  Network: bridge host ipvlan macvlan null overlay
#  Log: awslogs fluentd gcplogs gelf journald json-file local logentries splunk syslog
# Swarm: inactive
# Runtimes: runc
# Default Runtime: runc
# Init Binary: docker-init
# containerd version: 894b81a4b802e4eb2a91d1ce216b8817763c29fb
# runc version: 425e105d5a03fabd737a126ad93d62a9eeede87f
# init version: fec3683
# Security Options:
#  seccomp
#   Profile: default
# Kernel Version: 4.9.0-8-amd64
# Operating System: Debian GNU/Linux 9 (stretch)
# OSType: linux
# Architecture: x86_64
# CPUs: 1
# Total Memory: 7.801GiB
# Name: carter
# ID: S47H:35SR:TDEM:VJCN:ZKQV:RIBH:VIHK:GQ6L:UUEI:CSBD:O7OE:IM3E
# Docker Root Dir: /var/lib/docker
# Debug Mode: false
# Registry: https://index.docker.io/v1/
# Labels:
# Experimental: false
# Insecure Registries:
#  127.0.0.0/8
# Live Restore Enabled: false
#
#WARNING: No swap limit support
# ra  

docker image ls

# ra  docker image ls
#REPOSITORY          TAG                 IMAGE ID            CREATED             SIZE
#hello-world         latest              fce289e99eb9        7 months ago        1.84kB
# ra  

docker container ls --all

# ra  docker container ls --all
#CONTAINER ID        IMAGE               COMMAND             CREATED             STATUS                      PORTS               NAMES
#9eec5f49fd27        hello-world         "/hello"            36 minutes ago      Exited (0) 36 minutes ago                       clever_lichterman
#886424febc43        hello-world         "/hello"            25 hours ago        Exited (0) 25 hours ago                         optimistic_leakey
# ra  

sudo docker images
docker rmi 886424febc43

# 3) Security considerations 
# You may have noticed all the commands so far have defaulted to running as root (sudo)
# This is an unsafe default and should be changed.

# Create a new group and add users to it:
sudo groupadd docker

sudo useradd ra

sudo usermod -aG docker ra

# 4) Creating a Dockerfile

mkdir -p docker_test
cd docker_test/

# Edit Dockerfile, requirements.txt, app.py


# Build your app

docker build --tag=roll20 .

# ra  docker_test  docker build --tag=roll20 .
#Sending build context to Docker daemon  13.82kB
#Step 1/7 : FROM python:3.7-stretch
#3.7-stretch: Pulling from library/python
#a4d8138d0f6b: Pull complete
#dbdc36973392: Pull complete
#f59d6d019dd5: Pull complete
#aaef3e026258: Pull complete
#6e454d3b6c28: Pull complete
#47c95b44ab24: Pull complete
#5570e9404146: Pull complete
#281654452bf7: Pull complete
#ea8e7ce389f6: Pull complete
#Digest: sha256:99a16ef43ba12811a369a2912d8c73b0ebc69aed55b327653185ba1330e3121c
#Status: Downloaded newer image for python:3.7-stretch
# ---> 46ccb963c04a
#Step 2/7 : WORKDIR /app
# ---> Running in 2d61c8c30d47
#Removing intermediate container 2d61c8c30d47
# ---> afe6111ba6db
#Step 3/7 : COPY . /app
# ---> 33de3c146ced
#Step 4/7 : RUN pip install --trusted-host pypi.python.org -r requirements.txt
# ---> Running in 67f6423f75ed
#Collecting Numpy (from -r requirements.txt (line 1))
#  Downloading https://files.pythonhosted.org/packages/05/4b/55cfbfd3e5e85016eeef9f21c0ec809d978706a0d60b62cc28aeec8c792f/numpy-1.17.0-cp37-cp37m-manylinux1_x86_64.whl (20.3MB)
#Installing collected packages: Numpy
#Successfully installed Numpy-1.17.0
#Removing intermediate container 67f6423f75ed
# ---> a377775d78d2
#Step 5/7 : EXPOSE 80
# ---> Running in a47e882fff57
#Removing intermediate container a47e882fff57
# ---> 7ce058f2a24d
#Step 6/7 : ENV NAME World
# ---> Running in 94af2c3d890e
#Removing intermediate container 94af2c3d890e
# ---> 7e616d4dae80
#Step 7/7 : CMD ["python", "app.py"]
# ---> Running in f79a3cee87bc
#Removing intermediate container f79a3cee87bc
# ---> 399918acce75
#Successfully built 399918acce75
#Successfully tagged roll20:latest
# ra  docker_test  

# Check your app was installed by checking your local Docker image registry:

docker image ls


# ra  docker_test  docker image ls
#REPOSITORY          TAG                 IMAGE ID            CREATED             SIZE
#roll20              latest              399918acce75        2 minutes ago       1.05GB
#python              3.7-stretch         46ccb963c04a        4 days ago          941MB
#hello-world         latest              fce289e99eb9        7 months ago        1.84kB
# ra  docker_test  

docker run roll20
 
# Can run with port settings with the -p flag too


# If you update just the app code, you can re-build the Docker image.
# This is not as resource-intensive as the initial build; only necessary changes are 
# brought in.

# After altering app.py

docker build --tag=roll20 .

# ra  docker_test  docker build --tag=roll20 .
#Sending build context to Docker daemon  14.85kB
#Step 1/7 : FROM python:3.7-stretch
# ---> 46ccb963c04a
#Step 2/7 : WORKDIR /app
# ---> Using cache
# ---> afe6111ba6db
#Step 3/7 : COPY . /app
# ---> 045ec16d8ef9
#Step 4/7 : RUN pip install --trusted-host pypi.python.org -r requirements.txt
# ---> Running in 43e19094cefc
#Collecting Numpy (from -r requirements.txt (line 1))
#  Downloading https://files.pythonhosted.org/packages/05/4b/55cfbfd3e5e85016eeef9f21c0ec809d978706a0d60b62cc28aeec8c792f/numpy-1.17.0-cp37-cp37m-manylinux1_x86_64.whl (20.3MB)
#Installing collected packages: Numpy
#Successfully installed Numpy-1.17.0
#Removing intermediate container 43e19094cefc
# ---> 163207aac796
#Step 5/7 : EXPOSE 80
# ---> Running in 8aa0e71c200a
#Removing intermediate container 8aa0e71c200a
# ---> b050fbb7e37d
#Step 6/7 : ENV NAME World
# ---> Running in 106425262fb7
#Removing intermediate container 106425262fb7
# ---> 74f217a1d060
#Step 7/7 : CMD ["python", "app.py"]
# ---> Running in 016daabdcdbf
#Removing intermediate container 016daabdcdbf
# ---> ccdf3af1d563
#Successfully built ccdf3af1d563
#Successfully tagged roll20:latest
# ra  docker_test  

# You can get a lot of details about your image using `inspect`:

docker inspect roll20

# ra  ⋯  notebooks  code  docker_test  docker inspect roll20
#[
#    {
#        "Id": "sha256:ccdf3af1d5639c44a2b2237415c3d0eb8d3181f04b3d7297bc5a7a24ba3ac119",
#        "RepoTags": [
#            "roll20:latest"
#        ],
#        "RepoDigests": [],
#        "Parent": "sha256:74f217a1d0607f53bc7ff0ded59c5260e3b6cdee6d7201bedfcde40bf9d50595",
#        "Comment": "",
#        "Created": "2019-08-03T22:21:30.841261217Z",
#        "Container": "016daabdcdbf44dd66aac37783f216ba034e25f5bc7592c43585337a88ab94c4",


#---
#
#In a distributed application, different pieces of the app are called “services”. For example, if you imagine a video sharing site, it probably includes a service for storing application data in a database, a service for video transcoding in the background after a user uploads something, a service for the front-end, and so on.
#
#Services are really just “containers in production.” A service only runs one image, but it codifies the way that image runs—what ports it should use, how many replicas of the container should run so the service has the capacity it needs, and so on. Scaling a service changes the number of container instances running that piece of software, assigning more computing resources to the service in the process.
#
#Luckily it’s very easy to define, run, and scale services with the Docker platform -- just write a docker-compose.yml file.
#
#--

# YAML ("YAML Ain't Markup Language")

# Initialize a Docker Swarm

docker swarm init

# ra  docker_test  docker swarm init
#Swarm initialized: current node (rf2mpr85sxew8crlg4s5zv71s) is now a manager.
#
#To add a worker to this swarm, run the following command:
#
#    docker swarm join --token SWMTKN-1-33jpx3rgyhnm4z2yeiftw2lvdyclhqjqeaoyz7w2ysg4om5c76-1inpnveoah0zjd01gopt4n20o 10.0.2.15:2377
#
#To add a manager to this swarm, run 'docker swarm join-token manager' and follow the instructions.
#
# ra  docker_test  

# Deploy the app
# We have to call it something

docker stack deploy -c docker-compose.yml attack_the_grue

# ra  docker_test  docker stack deploy -c docker-compose.yml attack_the_grue
#Creating network attack_the_grue_default
#Creating service attack_the_grue_roll20
# ra  docker_test  

docker service ls

# ra  docker_test  docker service ls
#ID                  NAME                     MODE                REPLICAS            IMAGE               PORTS
#uzxy32f944ye        attack_the_grue_roll20   replicated          0/5                 ra/roll20:latest
# ra  docker_test  

#---
#A single container running in a service is called a task. Tasks are given unique IDs that numerically increment, up to the number of replicas you defined in docker-compose.yml. List the tasks for your service:
#---

docker container ls -q

# Show all tasks on a stack:


docker stack ps attack_the_grue

# Scale up

#---
#You can scale the app by changing the replicas value in docker-compose.yml, saving the change, and re-running the docker stack deploy command:
#---

docker stack deploy -c docker-compose.yml attack_the_grue


#---
# Docker performs an in-place update, no need to tear the stack down first or kill any containers.

#Now, re-run docker container ls -q to see the deployed instances reconfigured. If you scaled up the replicas, more tasks, and hence, more containers, are started.


# Tear down the app and the swarm


docker stack rm attack_the_grue

docker swarm leave --force

# ra  docker_test  docker swarm leave --force
#Node left the swarm.
# ra  docker_test  


#---
#It’s as easy as that to stand up and scale your app with Docker. You’ve taken a huge step towards learning how to run containers in production. Up next, you learn how to run this app as a bonafide swarm on a cluster of Docker machines.
#---

#---
#Understanding Swarm clusters
#
#A swarm is a group of machines that are running Docker and joined into a cluster. After that has happened, you continue to run the Docker commands you’re used to, but now they are executed on a cluster by a swarm manager. The machines in a swarm can be physical or virtual. After joining a swarm, they are referred to as nodes.
#
#Swarm managers can use several strategies to run containers, such as “emptiest node” -- which fills the least utilized machines with containers. Or “global”, which ensures that each machine gets exactly one instance of the specified container. You instruct the swarm manager to use these strategies in the Compose file, just like the one you have already been using.
#
#Swarm managers are the only machines in a swarm that can execute your commands, or authorize other machines to join the swarm as workers. Workers are just there to provide capacity and do not have the authority to tell any other machine what it can and cannot do.
#
#Up until now, you have been using Docker in a single-host mode on your local machine. But Docker also can be switched into swarm mode, and that’s what enables the use of swarms. Enabling swarm mode instantly makes the current machine a swarm manager. From then on, Docker runs the commands you execute on the swarm you’re managing, rather than just on the current machine.
#---

#---
# Understanding the Stack

#In part 4, you learned how to set up a swarm, which is a cluster of machines running Docker, and deployed an application to it, with containers running in concert on multiple machines.
#
#Here in part 5, you reach the top of the hierarchy of distributed applications: the stack. A stack is a group of interrelated services that share dependencies, and can be orchestrated and scaled together. A single stack is capable of defining and coordinating the functionality of an entire application (though very complex applications may want to use multiple stacks).
#
#Some good news is, you have technically been working with stacks since part 3, when you created a Compose file and used docker stack deploy. But that was a single service stack running on a single host, which is not usually what takes place in production. Here, you can take what you’ve learned, make multiple services relate to each other, and run them on multiple machines.
#---

#---
# Open ports to services on cloud provider machines
# 
# At this point, your app is deployed as a swarm on your cloud provider servers, as evidenced by the docker commands you just ran. But, you still need to open ports on your cloud servers in order to:
# 
#     if using many nodes, allow communication between the redis service and web service
# 
#     allow inbound traffic to the web service on any worker nodes so that Hello World and Visualizer are accessible from a web browser.
# 
#     allow inbound SSH traffic on the server that is running the manager (this may be already set on your cloud provider)
# 
# These are the ports you need to expose for each service:

# | Service 	| Type 	| Protocol 	| Port |
# ---
# | web 	| HTTP 	| TCP           | 80 |
# | visualizer 	| HTTP 	| TCP           | 8080 |
# | redis 	| TCP 	| TCP           | 6379 |
#---

# More resources

# The Docker Cheatsheet website:
# https://dockercheatsheet.painlessdocker.com/

# On GitHub:
#https://github.com/wsargent/docker-cheat-sheet

# Docker's website:
#https://www.docker.com/get-started
