import pandas as pd

# Importações Internas:
import input_arquivos
import info_DadosOriginais
import funcoes
import nomesTimes
import variaveis
import nomeTorneios
import datas
import odds
import tempo
import listaGeralDados


# Input Arquivo:
# df = input_arquivos.main()
# dadosOriginais=pd.read_csv(df)

# variáveis:
# dadosData = dadosOriginais['Data'] # Data e Hora
# dadosOdds = dadosOriginais['Odd'] # Odds de Entrada e Saída(quando houver)
# dadosTipo = dadosOriginais['Tipo'] # BACK ou LAY
# dadosSelecao = dadosOriginais['Seleção'] # Mercado da Operação
# dadosEvento = dadosOriginais['Evento'] # Times no evento casa e visitante
# dadosTempoJogo = dadosOriginais['Tempo de jogo'] # Minuto do Back (in), minuto lay (out)
# dadosCompeticao = dadosOriginais['Competição'] # Torneio
# dadosTipoOperacao = dadosOriginais['Tipo de operação'] # Informa o motivo da entreda e principalmente da saída, pode ajudar na ajuste do método

# Informações Gerais:
print("\n")
print("*"*20 + "  Informações Gerais  " + "*"*20)

print("\nDados com Data Frame:\n")
print(info_DadosOriginais.dadoComoDF(variaveis.dadosOriginais))
# print(f"\nArquivo Original tem {info_DadosOriginais.dadosColunas(dadosOriginais)} colunas.")
print(f"\nArquivo Original tem {info_DadosOriginais.qtdLinhasIndices(variaveis.dadosOriginais)} Tupla (linhas) ou Índices")

print("\n")
print("*"*20 + "  Informações Fultradas - AJUSTES | REDs  " + "*"*20)

print("\nDatas:\n")
print(datas.mainDatas())

print("\nDados Torneio:\n")
print(nomeTorneios.mainTorneio())

print("\nDados dos Times:\n")
print(nomesTimes.timesCasa_Visitante(nomesTimes.mainTimes()))

print("\nDados de Odds Entradas | Saidas\n")
print(odds.mainOdds())

print("\nDados de Tempo Entradas | Saidas | Tempo de Operação\n")
print(tempo.dadosTempo())

print("\n")
print("*"*20 + "  Lista com todos os Dados Tratados  " + "*"*20)
print(listaGeralDados.listaDados())