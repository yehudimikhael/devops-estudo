#!/bin/bash
sleep 30
pass="root"
mysql -u root -p$pass < /usr/sql/source.sql
#mysqld < /usr/sql/source.sql
