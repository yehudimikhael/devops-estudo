FROM ubuntu
MAINTAINER Yehudi Brito 

RUN \
   apt-get update && apt-get install nginx -y && \
   apt-get clean &&echo "\ndaemon off;" >> /etc/nginx/nginx.conf && \
   chown -R www-data:www-data /var/lib/nginx
COPY nginx.conf /etc/nginx/nginx.conf 
ADD rallyCarioca/ /var/www/html/
WORKDIR /etc/nginx
ENTRYPOINT [ "nginx"]

EXPOSE 80 443

