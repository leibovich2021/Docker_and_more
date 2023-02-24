Docker

for install:
https://www.digitalocean.com/community/tutorials/how-to-install-and-use-docker-on-ubuntu-20-04


command:

sudo systemctl status docker
docker ps 
docker ps -a
docker images
docker run hello-world
ifconfig
docker run -it tomcat
docker run -it -p 1234:8080 tomcat
docker search httpd
docker run -d --name tomcat -p 1234:8080 -d tomcat
