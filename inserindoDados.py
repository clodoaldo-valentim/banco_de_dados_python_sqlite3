import sqlite3 #importa o sqlite3
from sqlite3 import Error
##########Criar conexão
def ConexaoBanco():
    caminho = "C:\\Users\\Clodoaldo Valentim\\Documents\\python\\banco_python\\agenda.db"#o caminho do BD
    con = None # Inicializa a variável de conexão como None
    try:# Tenta executar o bloco de código
        con = sqlite3.connect(caminho)# Tenta estabelecer a conexão com o banco de dados usando o caminho especificado
    except Error as ex:# Se ocorrer um erro, captura a exceção
        print(ex)# Imprime a mensagem de erro
    return con # Retorna a conexão estabelecida (ou None se houver erro)
vcon = ConexaoBanco()# Chama a função de conexão e armazena o objeto de conexão na variável vcon
nome = input("Digite o nome: ")# Solicita o nome do usuário e armazena na variável nome
telefone = input("Digite o telefone: ")
email = input("Digite o email: ")
vsql = "INSERT INTO contato(nome, telefone, email) VALUES('"+nome+"','"+telefone+"','"+email+"');"# Constrói a instrução SQL para inserir os dados na tabela contato

def inserir(conexao, sql):# Define a função inserir que recebe uma conexão e uma instrução SQL como parâmetros
    try:# Tenta executar o bloco de código  
        c = conexao.cursor()# Cria um cursor para a conexão, permitindo a execução de comandos SQL
        c.execute(sql)# Executa a instrução SQL fornecida
        print("Dado cadastrado")# Informa que o dado foi cadastrado com sucesso
        conexao.commit()# Confirma (commita) a transação, salvando as alterações no banco de dados
    except Error as ex:# Se ocorrer um erro, captura a exceção
        print(ex) # Imprime a mensagem de erro      
inserir(vcon, vsql)# Chama a função inserir, passando a conexão e a instrução SQL para inserir os dados
        
vcon.close()# Fecha a conexão com o banco de dados

###################### Mais explicações ###############################

#from sqlite3:Especifica o módulo de onde você está importando. Neste caso, sqlite3 é o módulo que contém classes e funções para interagir com bancos de dados SQLite.

#import Error:Especifica a classe ou função específica que você deseja importar do módulo sqlite3. Aqui, Error é uma classe que representa exceções específicas relacionadas ao SQLite.
#None é um valor especial em Python que representa a ausência de um valor ou um valor nulo.

#A linha con = sqlite3.connect(caminho) é usada para estabelecer uma conexão com um banco de dados SQLite. 

#O bloco try em Python é usado para capturar e tratar exceções que podem ocorrer durante a execução do código. Ele permite que você execute um bloco de código e, se ocorrer uma exceção, você pode capturá-la e tratá-la adequadamente, evitando que o programa seja interrompido abruptamente. 

#c = conexao.cursor():Cria um cursor a partir do objeto de conexão. Um cursor é um objeto que permite a execução de comandos SQL e a recuperação de resultados de consultas.conexao.cursor() retorna um cursor que será usado para executar a instrução SQL.

#c.execute(sql) executa a instrução SQL. No caso, essa instrução é uma inserção de dados na tabela contato.






####################################################################
        
