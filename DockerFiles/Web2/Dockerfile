FROM debian
MAINTAINER Yehudi Brito 

RUN apt-get update && apt-get install nginx -y
COPY nginx.conf /etc/nginx/nginx.conf 
ADD rallyCarioca/ /var/www/html/
WORKDIR /etc/nginx
ENTRYPOINT [ "/usr/sbin/nginx"]
CMD ["-g", "daemon off;"]
EXPOSE 80 

