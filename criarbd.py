import sqlite3 as lite

conexao = lite.connect('dados.db')

with conexao:
    cur = conexao.cursor()
    cur.execute("DELETE FROM produtos WHERE id=3")
    #cur.execute("ALTER TABLE produtos ADD COLUMN estoque INTEGER")
    #cur.execute("CREATE TABLE produtos(id INTEGER PRIMARY KEY AUTOINCREMENT, nome TEXT, barra TEXT, descricao TEXT, valor DECIMAL, marca TEXT, data_da_compra DATE, estoque INTEGER, imagem TEXT)")
