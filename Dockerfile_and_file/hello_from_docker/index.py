FROM amazonlinux 

RUN apt-get -y update
RUN apt get -y install httpd

RUN echo "Hello World from Docker" > /var/www/html/index.html
CMD ["/usr/sbin/httpd","-D","FOREGROUND"]

EXPOSE 80
