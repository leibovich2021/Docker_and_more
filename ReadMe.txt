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






command:

sudo systemctl status docker
docker version
ifconfig

docker search (name image)

docker pull (name image) = save image in my local computer
docker run (name images) = how run container

docker ps = check what container runing
docker ps -a = check what container run
docker images = show images

docker build .

docker rm (container id)
docker container prune   =  delete all container
docker rmi $(docker images -q)
docker stop $(docker ps -a -q) = stop all containers
docker rm $(docker ps -a -q) = remove all containers
docker rmi -f $(docker images -a -q) = remove all images




exmaple: 


docker run -it (name image)
docker run -d --name (Name) -p (port:80) -d (name image)
docker run hello-world
docker run -d --name tomcat -p 1234:8080 -d tomcat
docker run -it tomcat
docker run -it -p 1234:8080 tomcat
