#import sqlite3 as lite 

import mysql.connector as sqlConnector

conexao = sqlConnector.connect(host="localhost",
    user="root",
    passwd="rafinha292002",
    db="cadastro")
 


def inserir_form(i):
    with conexao:
        cur = conexao.cursor()
        query = "INSERT INTO produtos(nome, barra, descricao, valor, marca, data_da_compra, estoque, imagem) VALUES(%s, %s, %s, %s,%s, %s, %s, %s)"
        cur.execute(query, i)


def atualizar_form(i):
    with conexao:
        cur = conexao.cursor()
        query = "UPDATE produtos SET nome=%s, barra==%s, descricao==%s, valor==%s,marca==%s,data_da_compra==%s,estoque==%s,imagem==%s WHERE id==%s"
        cur.execute(query, i)



def deletar_form(i):
    with conexao: 
        cur = conexao.cursor()
        query = "DELETE FROM produtos WHERE id==%s"
        cur.execute(query, i)



    



def ver_dados_form():
    ver_dados=[]
    with conexao:
        cur = conexao.cursor()
        query = "SELECT * FROM PRODUTOS"
        cur.execute(query)
    
        rows = cur.fetchall()
        for  row in rows:
            ver_dados.append(row)
    return ver_dados        


        



def ver_dados_individual_form(id):
    ver_dados_individual=[]
    with conexao:
        cur = conexao.cursor()
        query = "SELECT * FROM PRODUTOS WHERE id=%s"
        cur.execute(query,id)
        
        rows = cur.fetchall()
        for  row in rows:
            ver_dados_individual.append(row)
    return ver_dados_individual
    


        