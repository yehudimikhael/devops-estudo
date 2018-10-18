FROM mysql

ENV MYSQL_DATABASE="inscricao"
ENV MYSQL_ROOT_PASSWORD="root"
ENV MYSQL_HOST="localhost"
ENV MYSQL_USER="noc"
ENV MYSQL_PASSWORD="concrete123.."
ENV MYSQL_MY_DATABASE="inscricao"


#GRANT ALL PRIVILEGES 

# Add the content of the sql-scripts/ directory to your image
# All scripts in docker-entrypoint-initdb.d/ are automatically
# executed during container startup
#COPY ./source.sql /docker-entrypoint-initdb.d/

 
EXPOSE 3306
#CMD [ "sh", "/usr/sql/entrypoint.sh" ]
#CMD [ "mysqld" ]

