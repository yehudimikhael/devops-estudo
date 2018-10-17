import mysql.connector

con = mysql.connector.connector(user='noc', password='concrete123..', host='docker-mysql', database='inscricao')
cur = con.cursor()

def db_create():

#Se nao existe cria a tabela
    cur.execute("CREATE TABLE IF NOT EXISTS competidores(id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255), phone VARCHAR(15), vehicle VARCHAR(15))")


#Criar os dados na tabela
    try: 
       data =  [
            ('Fred', '(21)12345678', 'Hilux'),
            ('Vilma', '(22)9876367', 'L200'),
            ('Carlos', '(23)9993871', 'Ranger')
            ]
    cur.executemany("""INSERT INTO competidores
            (name, phone, vehicle)values (%s, %s, %s)""", data)
    con.commit()
    con.close()
    
    except:
        print("dados existem")
        pass
        return 0
    con.close()

def db_select():
    cur.execute("SELECT * FROM competidores")
    array = []
    for data in cur:
        array.append(data)
    return array