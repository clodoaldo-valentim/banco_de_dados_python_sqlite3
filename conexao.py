import sqlite3
from sqlite3 import Error
##########Criar conexão
def ConexaoBanco():
    caminho = "C:\\Users\\Clodoaldo Valentim\\Documents\\python\\banco_python\\agenda.db"
    con = None
    try:
        con = sqlite3.connect(caminho)
    except Error as ex:
        print(ex)
    return con
vcon = ConexaoBanco()#chama a função que faz a conexão com o banco
#Cria tabela
vsql = """CREATE TABLE tb_contatos(id INTEGER PRIMARY KEY AUTOINCREMENT, nome VARCHAR(30), telefone VARCHAR(30), email VARCHAR(30) );"""

def criarTabela(conexao, sql):
    try:
        c = conexao.cursor()
        c.execute(sql)#executa o sql
        print("Tabela criada")
    except Error as ex:
        print(ex)
criarTabela(vcon, vsql)
        
vcon.close()
        
