Docker

for install:
https://www.digitalocean.com/community/tutorials/how-to-install-and-use-docker-on-ubuntu-20-04


==============
Client terminal
Deamon  server
Host    local computer
Container
Image
Repository
Registry
===============



command:

sudo systemctl status docker
docker ps 
docker ps -a
docker images
docker build .
docker rm (container id)
docker container prune   =  delete all container
docker run (number images)
docker run -it (name image)
ifconfig
docker search httpd
docker rmi $(docker images -q)


stop all containers:
docker stop $(docker ps -a -q)

remove all containers:
docker rm $(docker ps -a -q)

remove all images:
docker rmi -f $(docker images -a -q)


exmaple: 

docker run -d --name (Name) -p (port:80) -d (name image)
docker run hello-world
docker run -d --name tomcat -p 1234:8080 -d tomcat
docker run -it tomcat
docker run -it -p 1234:8080 tomcat
