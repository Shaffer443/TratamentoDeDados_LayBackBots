import variaveis

# Nomes dos Times nas Partidas:

#LISTA BASE:

def mainTimes():
    timesNoEventoComLAY = []

    contadorTimesLAY = 1
    while contadorTimesLAY < len(variaveis.dadosOriginais): #Estimativa pis pode ser que os ultimos jogos não entrem na conta
      if variaveis.dadosEvento[contadorTimesLAY] and variaveis.dadosTipo[contadorTimesLAY] == 'LAY':
          # print("Entrada + saida")
          timesNoEventoComLAY.append(variaveis.dadosEvento[contadorTimesLAY])
      contadorTimesLAY += 1

    # print(times)
    # print(f"{timesNoEventoComLAY}\n")
    print(f"Total de Jogos: {len(timesNoEventoComLAY)}")
    return timesNoEventoComLAY


#Tratamento 4.1 (LAY): para separação dos times (Casa - Visitante).

def timesCasa_Visitante(dadosTimes):

    # #Esbolçando:
    # separandoComLAY = dadosTimes[0].split(" v ")
    # print(separandoComLAY)
    #
    # separandoCasa_ComLAY = separandoComLAY[0]
    # separandoVisitante_ComLAY = separandoComLAY[1]
    #
    # print(f"Casa: {separandoCasa_ComLAY} - Visitante: {separandoVisitante_ComLAY}\n")

    #Dados importantes:
    com_v = 0
    for v in dadosTimes:
      if " v " in v:
        com_v += 1

    com_vs = 0
    for vs in dadosTimes:
       if " vs " in vs:
        com_vs += 1

    # print(f"Total de jogos com 'v' no texto: {len(timesNoEventoComLAY)}")
    print(f"Total de jogos com 'v' no texto: {com_v}")
    print(f"Total de jogos com 'vs' no texto: {com_vs}")

    #Percorendo os times e adicionando na lista:

    listaTimesDaCasa_ComLAY = []
    listaTimesEmVisitante_ComLAY = []

    contadorSeparacaoTimes_ComLAY  = 0
    while contadorSeparacaoTimes_ComLAY  < com_v: #Estimativa pois pode ser que os ultimos jogos não entrem na conta
      separandotimes_ComLAY  = dadosTimes[contadorSeparacaoTimes_ComLAY].split(" v ")
      listaTimesDaCasa_ComLAY.append(separandotimes_ComLAY[0])
      listaTimesEmVisitante_ComLAY.append(separandotimes_ComLAY[1])
      contadorSeparacaoTimes_ComLAY += 1

    contadorSeparacaoTimes_2_ComLAY = com_v
    while contadorSeparacaoTimes_2_ComLAY  < len(dadosTimes): #Estimativa pois pode ser que os ultimos jogos não entrem na conta
      separandotimes_2_ComLAY = dadosTimes[contadorSeparacaoTimes_2_ComLAY].split(" vs ")
      listaTimesDaCasa_ComLAY.append(separandotimes_2_ComLAY[0])
      listaTimesEmVisitante_ComLAY.append(separandotimes_2_ComLAY[1])
      contadorSeparacaoTimes_2_ComLAY += 1


    print("\nLista dos Times Jogando em CASA:\n")
    print(listaTimesDaCasa_ComLAY)

    print("\nLista dos Times Jogando em VISITANTE:\n")
    print(listaTimesEmVisitante_ComLAY)

    print(f"\nQuantidade dos times da CASA: {len(listaTimesDaCasa_ComLAY)}")
    print(f"Quantidade dos times da VISITANTE: {len(listaTimesEmVisitante_ComLAY)}")

    return listaTimesDaCasa_ComLAY, listaTimesEmVisitante_ComLAY