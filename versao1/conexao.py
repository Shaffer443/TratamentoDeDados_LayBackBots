import mysql.connector
from mysql.connector import errorcode
from mysql.connector import (connection)


conexao_bot_teste_layback_over05segundotempo = connection.MySQLConnection(user='InputDados', password='@Klu1424',
                                                                    host='192.168.1.1', database='metodo_Over05_2tempo')

try:
    conexao = conexao_bot_teste_layback_over05segundotempo
except mysql.connector.Error as err:
  if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
    # print("Something is wrong with your user name or password")
    print("\nFalha de conexão. Alguma coisa errada com seu nome de usuário ou senha")
  elif err.errno == errorcode.ER_BAD_DB_ERROR:
    # print("Database does not exist")
    print("\nBanco de dados não existe")
  else:
    print(err)
else:
  print(f"\nConexão BD MYSQL  - OK")

#######################################################################################################################

def inserindoDados(dados): #INATIVO. SEM FUNCIONAR
        # Criar um objeto cursor para executar consultas SQL
        cursor = conexao.cursor()

        inserindoDadosSQL = ("INSERT INTO bot_teste_layback_over05segundotempo" 
                             "(ID_BotTeste, _data, competicao, time_casa, time_visitante, oddsEntrada, minutoEntrada, oddsSaida, minutoSaida, resultado, tempoOperacao, 'alteracoes')"
                             "VALUES (%d, %s, %s, %s, %s, %f, %d, %f, %d, %s, %d, );")

        # Insert information
        dadosInput = dados
        print(f"\n{dadosInput}")

        # Executar a consulta
        cursor.execute(inserindoDadosSQL, dadosInput)

        # Make sure data is committed to the database
        conexao.commit()

        cursor.close()
        conexao.close()
        # print(f"\nDados inseridos na tabela {tabela} ...... SUCESSO")
        # print(f"\nFalha ao passar os dados para o banco de dados {tabela} ...... ERRO")

