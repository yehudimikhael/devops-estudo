FROM ubuntu


#Instalar todas as depencias 
RUN apt-get update && apt-get install -y build-essential python python-dev python-pip vim iputils-ping && apt-get clean


WORKDIR /app

RUN pip install flask uwsgi mysql-connector-python jsonify

COPY /app/* ./
COPY entrypoint.sh ./

CMD [ "sh", "/app/entrypoint.sh" ]


EXPOSE 5000