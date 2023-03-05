Docker

for install:
https://www.digitalocean.com/community/tutorials/how-to-install-and-use-docker-on-ubuntu-20-04


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

exmaple: 


docker run hello-world
docker run -d --name tomcat -p 1234:8080 -d tomcat
docker run -it tomcat
docker run -it -p 1234:8080 tomcat
