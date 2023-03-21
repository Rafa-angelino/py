# import sqlite3 as lite

# conexao = lite.connect('dados.db')

# with conexao:
#     cur = conexao.cursor()
#     #cur.execute("DELETE FROM produtos WHERE id=3")
#     #cur.execute("ALTER TABLE produtos ADD COLUMN estoque INTEGER")
#     #cur.execute("CREATE TABLE produtos(id INTEGER PRIMARY KEY AUTOINCREMENT, nome TEXT, barra TEXT, descricao TEXT, valor DECIMAL, marca TEXT, data_da_compra DATE, estoque INTEGER, imagem TEXT)")


import mysql.connector as sqlConnect
from mysql.connector import Error
 
connection = sqlConnect.connect(host="localhost",
    user="root",
    passwd="rafinha292002",
    db="cadastro")
 
with connection:
    try:
        if connection.is_connected():
            cursor = connection.cursor()
            cursor.execute("select database();")
            db = cursor.fetchone()
            print("Você está conectado ao banco de dados: ", db)
    except Error as e:
        print("Erro ao conectar ao MySQL", e)
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()
            print("A conexão MySQL está fechada")


