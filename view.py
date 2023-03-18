import sqlite3 as lite 

conexao = lite.connect('dados.db')
 
 


def inserir_form(i):
    with conexao:
        cur = conexao.cursor()
        query = "INSERT INTO produtos(nome, barra, descricao, valor, marca, data_da_compra, estoque, imagem) VALUES(?,?,?,?,?,?,?,?)"
        cur.execute(query, i)


def atualizar_form(i):
    with conexao:
        cur = conexao.cursor()
        query = "UPDATE produtos SET nome=?, barra=?, descricao=?, valor=?,marca=?,data_da_compra=?,estoque=?,imagem=? WHERE id=?"
        cur.execute(query, i)



def deletar_form(i):
    with conexao: 
        cur = conexao.cursor()
        query = "DELETE FROM produtos WHERE id=?"
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
        query = "SELECT * FROM PRODUTOS WHERE id=?"
        cur.execute(query,id)
        
        rows = cur.fetchall()
        for  row in rows:
            ver_dados_individual.append(row)
    return ver_dados_individual
    


        