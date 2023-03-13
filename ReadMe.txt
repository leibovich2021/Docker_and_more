Docker

for install:
https://www.digitalocean.com/community/tutorials/how-to-install-and-use-docker-on-ubuntu-20-04

For work docker in Windows or Mac we need download Docker Desktop(Virtual m)

==============
Client = terminal
Deamon  = server
Host  =  local computer
Container
Image
Repository
Registry
===============

Container 1 = Image 1


1 Image = & Container




===============

command:

sudo systemctl status docker
docker version
ifconfig

ping 8.8.8.8  = how check if conatiner have access to internet
or ping (name site)
ls -la = show all file in container

docker search (name image)

docker pull (name image) = save image in my local computer
docker run (name images) = how run container

docker run -i -t = interactive terminal
docker run -it (name images) = enter into image
docker run -it busybox
docker run -d nginx = detached
docker run nginx
docker run -d --name (Name) nginx  = add name

docker container inspect (number container)
or
docker container inspect (number container) | grep IPAddress

docker exec -it (name container/id) (name process)
docker exec -it 8cbe6b4701f7 bash

docker ps = show what container runing
docker ps -a = show what container run and stop 
docker images = show images



docker stop (name container)
docker stop $(docker ps -a -q) = stop all containers
docker rm (container id)
docker container prune   =  delete all container
docker rmi $(docker images -q)
docker rm $(docker ps -a -q) = remove all containers
docker rmi -f $(docker images -a -q) = remove all images


docker run -p 8080:80 (name image) = -p = publish
docker run -d -p 8083:80 nginx

how chang html page in nginx:
docker run -v ${PWD}:/usr/share/nginx/html nginx
${PWD} = adderss new file html
docker run -v ${PWD}:/usr/share/nginx/html -p 8089:80 -d  nginx

to enter into container
docker exec -it (number container) bash


exmaple: docker run -it --rm busybox  = auto delete containter after stoped


docker run -it (name image)
docker run -d --name (Name) -p (port:80) -d (name image)
docker run hello-world
docker run -d --name tomcat -p 1234:8080 -d tomcat
docker run -it tomcat
docker run -it -p 1234:8080 tomcat

==========================================================

CreateImage:
1 DockerFile = 1 Image

docker build .
docker build -f = file name
docker build . -t denis:1.1.23.1 = number version(latest)
docker build . -t my-calendar
docker run -it my-calendar
docker build . -t my-calendar:2.0.0


FROM python:latest or alpine(min version)
WORKDIR /app (dir)
COPY . . = make Copy
CMD ["python", "main.py"]


