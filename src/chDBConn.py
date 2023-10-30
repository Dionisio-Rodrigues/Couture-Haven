from dotenv import load_dotenv
import psycopg2
import os


load_dotenv()

#Conexão com a base postgres(PostgreSQL)
postgres = psycopg2.connect(
    host=os.getenv('POSTGRES_HOST'), 
    user=os.getenv('POSTGRES_USER'),
    password=os.getenv('POSTGRES_PASS'),
    port=os.getenv('POSTGRES_PORT'),
)

#Comando para abrir cursor para executar operações no db
runner = postgres.cursor()

#Método para executar um comando sql a partir de uma string
execsql = lambda comando, runner: runner.execute(comando)

#Comando para envio do comando para o db
resultados = runner.fetchall()

#Comando para fazer das operações efetivas no db
commitOperations = postgres.commit()

#Método para fechar a conexão com o banco
fecharConexao = runner.close(), postgres.close()

#Método para receber resultado das operações no db via terminal
printar_resultados = lambda resultados: [print (resultado) for resultado in resultados]
