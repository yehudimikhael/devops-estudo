FROM ubuntu


#Instalar todas as depencias 
RUN apt-get update && apt-get install -y build-essential python python-dev python-pip vim && apt-get clean


WORKDIR /app

RUN pip install flask uwsgi mysql-connector-python jsonify

COPY /app/* ./

CMD ["uwsgi", "--ini", "/app/wsgi.ini" ]

EXPOSE 5000