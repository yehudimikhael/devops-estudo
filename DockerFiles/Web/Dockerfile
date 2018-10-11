FROM ubuntu
MAINTAINER Yehudi Brito 

RUN adduser --disabled-login --disabled-password nginx && apt-get update && apt-get install nginx -y && apt-get clean
COPY nginx.conf /etc/nginx/nginx.conf
ADD rallyCarioca/ /var/www/html/

WORKDIR /etc/nginx
ENTRYPOINT ["/etc/init.d/nginx", "start"]
#ENTRYPOINT [ "systemct start " ]
CMD [ "/bin/bash"]


EXPOSE 80