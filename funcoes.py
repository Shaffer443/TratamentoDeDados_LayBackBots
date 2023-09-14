import variaveis

# Função base:

def colhendoDadoscomLAY (dadosAlvo, listaAlvo):
  contadorTimesLAY = 1
  while contadorTimesLAY < len(variaveis.dadosOriginais): #Estimativa pis pode ser que os ultimos jogos não entrem na conta
    if dadosAlvo[contadorTimesLAY] and variaveis.dadosTipo[contadorTimesLAY] == 'LAY':
        # print("Entrada + saida")
        listaAlvo.append(dadosAlvo[contadorTimesLAY])
    contadorTimesLAY += 1

# Sem uso:
def colhendoODDScomLAY():
  contadorIndice = 1
  for valores in variaveis.dadosOdds:
      if  contadorIndice % 2 == 0 and variaveis.dadosTipo[contadorIndice ] == 'BACK' and variaveis.dadosTipo[contadorIndice+1] == 'LAY':
        entradas_LAY.append(valores)
      if contadorIndice % 2 != 0 and variaveis.dadosTipo[contadorIndice ] == 'LAY' and variaveis.dadosTipo[contadorIndice-1] == 'BACK':
        saidas_LAY.append(valores)
      contadorIndice += 1