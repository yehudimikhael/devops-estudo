FROM mysql

ENV MYSQL_DATABASE="inscricao"
ENV MYSQL_ROOT_PASSWORD="root"
ENV MYSQL_HOST="localhost"
ENV MYSQL_USER="noc"
ENV MYSQL_PASSWORD="concrete123.."
ENV MYSQL_MY_DATABASE="inscricao"


#GRANT ALL PRIVILEGES 
COPY ./source.sql /usr/sql/source.sql
#Shell para dar permissao conexao remota do usuario noc
COPY ./entrypoint.sh    /usr/sql/entrypoint.sh
RUN chmod +x /usr/sql/entrypoint.sh

 
EXPOSE 3306
CMD [ "sh", "/usr/sql/entrypoint.sh" ]
CMD [ "mysqld" ]
