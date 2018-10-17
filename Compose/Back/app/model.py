import mysql.connector
import os
con = mysql.connector.connect(user='noc', password='concrete123..', host=os.environ.get('DB_HOST'), database='inscricao')
cur = con.cursor()
check = 0
def db_create():

#Se nao existe cria a tabela
    
#Criar os dados na tabela
    try: 
        cur.execute("CREATE TABLE IF NOT EXISTS competidores(id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255), phone VARCHAR(15), vehicle VARCHAR(15))")
        data =  [
            ('Fred', '(21)12345678', 'Hilux'),
            ('Vilma', '(22)9876367', 'L200'),
            ('Carlos', '(23)9993871', 'Ranger')
            ]
        cur.executemany("""INSERT INTO competidores
            (name, phone, vehicle)values (%s, %s, %s)""", data)
        con.commit()        
    except:
        print("dados existem")
        db_select()
        pass
        return 0
    con.close()
    check = 1

def db_select():
    if check == 0:
        db_create()
    else:
        cur.execute("SELECT * FROM competidores")
        result = cur.fetchall()
        return result
    con.close()