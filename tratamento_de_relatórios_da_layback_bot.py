# Importações

import pandas as pd
import input_arquivos
import quantidadeLinhas
import salvarArquivoCSV

# informações do arquivo de Upload

# df = input_arquivos.main().upload()
df = input_arquivos.main()
# for fn in df.keys():
#   print('\nUser carregando arquivo: "{name}" com o tamanho {lenght} bytes'. format(name=fn, lenght=len(df[fn])))
#   arquivo = fn

######################################################################################################################
# Usando os dados do upload

#dados=pd.read_csv('report-Over 0,5 No Segundo Tempo.csv')
dadosOriginais=pd.read_csv(df)

######################################################################################################################
# Verificando/visualizando Informações dos dados:

# dadosOriginais.head(5)

# dadosOriginais

######################################################################################################################
# # Pegandos os valores apenas dos Indices:
#
# qtdIndex = dadosOriginais
# for row in qtdIndex.index:
#     print(row)

print(f"\nArquivo Original tem {quantidadeLinhas.qtdLinhasIndices(dadosOriginais)} Tupla (linhas) ou Índices")

"""Total de **Colunas** = 28

'ID do Bot',
'Nome do Bot',
'ID da ordem',
- 'Data',<br>
'Stake',
- 'Odd',
- 'Tipo', <br>
'P/L',
- 'Seleção', <br>
'ID da Seleção',
-'Evento', <br>
'ID do Evento',
'Mercado',
'ID do Mercado',
'Tipo do Mercado',
'Placar Casa',
'Placar Fora',
- 'Tempo de jogo',
- 'Competição',<br>
'Liquidez',
- 'Tipo de operação',<br>
'Odd Pre Casa',
'Odd Pre Visitante',
'Odd Pre Empate',
'Odd Pre Over 2.5',
'Odd Pre Under 2.5',
'Histórico',
'Estatísticas'

**- Colunas Mais usadas**

"""

######################################################################################################################
# Variáveis:

dadosData = dadosOriginais['Data'] # Data e Hora
dadosOdds = dadosOriginais['Odd'] # Odds de Entrada e Saída(quando houver)
dadosTipo = dadosOriginais['Tipo'] # BACK ou LAY
dadosSelecao = dadosOriginais['Seleção'] # Mercado da Operação
dadosEvento = dadosOriginais['Evento'] # Times no evento casa e visitante
dadosTempoJogo = dadosOriginais['Tempo de jogo'] # Minuto do Back (in), minuto lay (out)
dadosCompeticao = dadosOriginais['Competição'] # Torneio
dadosTipoOperacao = dadosOriginais['Tipo de operação'] # Informa o motivo da entreda e principalmente da saída, pode ajudar na ajuste do método

######################################################################################################################
# Pegando TORNEIO da Operação
# Status = OK!

torneioDaEntrada = []

contadorTorneio = 1
while contadorTorneio < len(dadosOriginais): #Estimativa, pois pode ser que os ultimos jogos não entrem na conta
  if dadosCompeticao[contadorTorneio] and dadosTipo[contadorTorneio] == 'BACK':
      # print("Entrada + saida")
      torneioDaEntrada.append(dadosCompeticao[contadorTorneio])
  contadorTorneio += 1

# print(times)
# print(torneioDaEntrada)
# print(len(torneioDaEntrada))

######################################################################################################################
# Tratamento 4: Pegando os TIMES da operação
# Status = OK!

timesNoEvento = []

contadorTimes = 1
while contadorTimes < len(dadosOriginais): #Estimativa pis pode ser que os ultimos jogos não entrem na conta
  if dadosEvento[contadorTimes] and dadosTipo[contadorTimes] == 'BACK':
      # print("Entrada + saida")
      timesNoEvento.append(dadosEvento[contadorTimes])
  contadorTimes += 1

# print(times)
# print(timesNoEvento)
# print(len(timesNoEvento))

######################################################################################################################
#Tratamento 4.1: para separação dos times.

#Esbolçando:
separando = timesNoEvento[0].split(" v ")
# print(separando)

separandoCasa = separando[0]
separandoVisitante = separando[1]

# print(f"Casa: {separandoCasa} - Visitante: {separandoVisitante}\n")

#Percorendo os times e adicionando na lista:

listaTimesDaCasa = []
listaTimesEmVisitante = []

contadorSeparacaoTimes = 0
while contadorSeparacaoTimes <= 352: #Estimativa pois pode ser que os ultimos jogos não entrem na conta
  separandotimes = timesNoEvento[contadorSeparacaoTimes].split(" v ")
  listaTimesDaCasa.append(separandotimes[0])
  listaTimesEmVisitante.append(separandotimes[1])
  contadorSeparacaoTimes += 1

contadorSeparacaoTimes_2 = 353
while contadorSeparacaoTimes_2 <= len(timesNoEvento): #Estimativa pois pode ser que os ultimos jogos não entrem na conta
  separandotimes = timesNoEvento[contadorSeparacaoTimes].split(" vs ")
  listaTimesDaCasa.append(separandotimes[0])
  listaTimesEmVisitante.append(separandotimes[1])
  contadorSeparacaoTimes_2 += 1


print(f"\nLista dos Times Jogando em CASA:")
# print(listaTimesDaCasa)
print(f"Quantidade dos times da CASA: {len(listaTimesDaCasa)}\n")

print(f"Lista dos Times Jogando em VISITANTE:")
# print(listaTimesEmVisitante)
print(f"Quantidade dos times da VISITANTE: {len(listaTimesEmVisitante)}")

######################################################################################################################
# Tratamento 3: Pegando apenas a DATA da operação
# Status = OK!

dataEventoSimples = []

# Entradas

for qtd in dadosData:
  # print(qtd[:10])
  data = qtd[:10]
  dataEventoSimples.append(data)


# print(dataEventoSimples)
# print(len(dataEventoSimples))

######################################################################################################################
# Tratamento 4: Dados Odds.

# Dados de Cada Partida no arquivo

# dadosOdds = dados['Odd']
# dadosOddsTorneio = dados['Competição']
# valoresDadosOdds =
entradas = []
saidas = []

# print(dadosOdds.values)
#print(dadosOdds.index)

contadorTorneio = 0

contadorIndice = 0
for valores in dadosOdds:
    if  contadorIndice % 2 == 0:
      entradas.append(valores)
    if contadorIndice % 2 != 0:
      saidas.append(valores)
    contadorIndice += 1
      # print(index,valor, sep=" - ")

# print(f"Valores das Entradas = {entradas} com {len(entradas)} dados")
# print(f"Valores da saidas = {saidas} com {len(saidas)} dados")

print(f"\nOdds Média de Entrada: {sum(entradas)/len(entradas):.2f}")
print(f"Odds Média de Saída: {sum(saidas)/len(saidas):.2f}")

######################################################################################################################
# Tratamento 02: Tempo de Exposição na Operação
# Pegando o tempo APENAS de exposição no RED. Já que no caso de Green o mercado desaparece, impossiilitando entrenda de "lay". logo Ela não existe para o mercado de Over 0,5
# Status = OK!

# PARA JOGOS COM saidas (Usando o LAY):
minutoEntrada = []
minutoSaida = []
tempoExpostoNaOperacao = []

contador = 1
while contador < len(dadosOriginais): #Estimativa pis pode ser que os ultimos jogos não entrem na conta
  if dadosEvento[contador-1] == dadosEvento[contador]:
    if dadosTipo[contador-1] == 'BACK' and dadosTipo[contador] == 'LAY':
      minutoEntrada.append(dadosTempoJogo[contador-1])
      minutoSaida.append(dadosTempoJogo[contador])
      # print("Entrada + saida")
  contador += 1


# Exposição
contadorExp = 0
while contadorExp < len(minutoEntrada): #Estimativa pis pode ser que os ultimos jogos não entrem na conta
  exposicao = minutoSaida[contadorExp] - minutoEntrada[contadorExp]
  tempoExpostoNaOperacao.append(exposicao)
  contadorExp += 1


# print(minutoEntrada)
# print(minutoSaida)
# print("\n")
# print(tempoExpostoNaOperacao)

print("\n")
print("Entradas filtradas contendo minuto de Entrada(BACK) e de Saída (LAY)")
print("OBS: Nem todos os jogos há Saída em lay, já que o método quando GREEN encerra o mercado, impossibilitando saída(lay).")
print(f"Quantidades de Entradas: {len(minutoEntrada)}")
print(f"Quantidades de Saídas (Usando o Lay): {len(minutoSaida)}")
print(f"Quantidade de jogos com minutagem de exposição de tempo: {len(tempoExpostoNaOperacao)}")

# Média de tempo de exposição por jogo:

mediaExposicao = sum(tempoExpostoNaOperacao)/len(tempoExpostoNaOperacao)
print(f"Média de minutagem em exposição de tempo: {round(mediaExposicao)} minutos")

######################################################################################################################
# Tratamento 01: Green's e Red's
# Status = OK!

green = 0
red = 0

resultadoOperacao = []

contador = 1
while contador < len(dadosOriginais): #Estimativa pis pode ser que os ultimos jogos não entrem na conta
  if dadosEvento[contador-1] == dadosEvento[contador]:
    if dadosTipo[contador-1] == 'BACK' and dadosTipo[contador] == 'LAY':
      # print("Entrada + saida")
      resultadoOperacao.append('Red')
      red += 1
  else:
    if dadosEvento[contador] and dadosTipo[contador-1] == 'BACK':
      if dadosTipo[contador-1] == 'BACK' and dadosTipo[contador] != 'LAY':
        # print("Só Entrada")
        resultadoOperacao.append('Green')
        green += 1
  contador += 1

totalOperacoes = green + red

print("\nAproximadamente:")
print(f"Total de Entradas = {totalOperacoes}. Com um total aproximado de Green's = {green} e Red's = {red}")
# print(resultadoOperacao)

# Proporcionalidade das Entradas:

def aproveitamentoPersonalidades(totalEntradas, comparativo):
  aproveitamento = (comparativo/totalEntradas)*100
  # print(aproveitamento)
  return aproveitamento

aproveitamentoGreen = aproveitamentoPersonalidades(totalOperacoes, green)
aproveitamentoRed = aproveitamentoPersonalidades(totalOperacoes, red)

print(f"Aproveitamento Green's: {aproveitamentoGreen:.2f}%\n")

######################################################################################################################
# Geração do Dicionário das Entradas:
# Status = Parcialmente. Faltas dados para sincronizar com os dados na tabela SGBD.


contadorJson = 0
while contadorJson < len(minutoEntrada): # Pegando números contabilizados de partidas
  dfEntradas = {
              'ID': contadorJson,
              'Data': dataEventoSimples[contadorJson],
              'Competição': torneioDaEntrada[contadorJson],
              'Evento': timesNoEvento[contadorJson],
              'Odd de Entrada': entradas[contadorJson],
              'Minuto Entrada': minutoEntrada[contadorJson], #Observar que pq nem todas as entradas há saidas de dados de tempo(minutos)
              'Odd de Saida': saidas[contadorJson],
              'Minuto Saida': minutoSaida[contadorJson],
              'Red ou Green': resultadoOperacao[contadorJson]
              }
  # print(dfEntradas) #acha todos que tem minutos de saída. POde haver jogos que não há esse tempo de saída.
  # dados_pre_para_DF = dfEntradas
  contadorJson += 1


# print(dfEntradas)

#Só os dados (sem ser dicionário):

listaGeralFinalParaDF = []

contadorDados = 0
while contadorDados < len(minutoEntrada): # Pegando números contabilizados de partidas
  dfEntradasDados = [contadorDados,
                    dataEventoSimples[contadorDados],
                    torneioDaEntrada[contadorDados],
                    # timesNoEvento[contadorDados], #informa os dois times em uma só tupla
                    listaTimesDaCasa[contadorDados],
                    listaTimesEmVisitante[contadorDados],
                    entradas[contadorDados],
                    minutoEntrada[contadorDados], #Observar que pq nem todas as entradas há saidas de dados de tempo(minutos)
                    saidas[contadorDados],
                    minutoSaida[contadorDados],
                    resultadoOperacao[contadorDados],
                    tempoExpostoNaOperacao[contadorDados]]
  listaGeralFinalParaDF.append(dfEntradasDados)
  # print(dfEntradasDados) #acha todos que tem minutos de saída. POde haver jogos que não há esse tempo de saída.
  # dados_pre_para_DF = dfEntradas
  contadorDados += 1

######################################################################################################################
# Compilação dos resultdos para um novo após o filtro Data Frame
# Ideia de poder usar como JSON

dfDadosGerais = {'Total de Operações': totalOperacoes,
                 'Total Greens': green,
                 'Total Reds': red,
                 'Aproveitamento': "{:.2f}%".format(aproveitamentoGreen),
                 'Proporcionalidade': "Criar" }

dfEntradas = {'ID': contador,
              'Data': dataEventoSimples,
              'Competição': torneioDaEntrada,
              'Evento': timesNoEvento,
              'Odd de Entrada': entradas,
              'Minuto Entrada': minutoEntrada, # Tratar Falha, pois terá chogos que não havera saida, pq foi Green. Todos terão entradas mas não todos saidas e sua ordem.
              'Odd de Saida': saidas,
              'Minuto Saida': minutoSaida,
              'Tempo de Operação': tempoExpostoNaOperacao,
              'Red ou Green': resultadoOperacao
              }

# print(dfDadosGerais)
# print("\n")
# print(dfEntradas)

######################################################################################################################
#### Data Frames Finais: ####

novaDFGeral = pd.DataFrame(listaGeralFinalParaDF, columns=['ID', 'DATA','COMPETIÇÂO','CASA', 'VISITANTE', 'Odd de Entrada','Minuto Entrada', 'Odd de Saida', 'Minuto Saida', 'Red ou Green', 'Média de Exposição'])
print(novaDFGeral)
## Salvandoo em arquivo:

escolhaSalvar = int(input("\nDeseja salvar o DATA FRAME filtrado em arquivo .csv?(1-Sim) "))
if escolhaSalvar == 1:
    try:
        print("Arquivo criado com sucesso no diretório /Downloads")
        salvarArquivoCSV.dataframeParaCSV(novaDFGeral)
    except:
        print("Falha na criação do arquivo ...... ERRO")

