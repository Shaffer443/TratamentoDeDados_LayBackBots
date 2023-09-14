import nomesTimes
import variaveis
import nomesTimes
import nomeTorneios
import datas
import odds
import tempo

# Composição dos DADOS LAY:

def listaDados():
    listaGeralFinalParaDF_LAY = []

    contadorDados_LAY = 1
    while contadorDados_LAY < len(nomeTorneios.mainTorneio()): # Pegando números contabilizados de partidas
      dfEntradasDados_LAY = [contadorDados_LAY,
                            # dataEventoSimplesLAY_Tratado[contadorDados_LAY],
                            datas.mainDatas()[contadorDados_LAY],
                            # torneioDaEntrada_LAY[contadorDados_LAY],
                            nomeTorneios.mainTorneio()[contadorDados_LAY],
                            # listaTimesDaCasa_ComLAY[contadorDados_LAY],
                            nomesTimes.timesCasa_Visitante(nomesTimes.mainTimes())[0][contadorDados_LAY],
                            # listaTimesEmVisitante_ComLAY [contadorDados_LAY],
                            nomesTimes.timesCasa_Visitante(nomesTimes.mainTimes())[1][contadorDados_LAY],
                            # entradas_LAY[contadorDados_LAY],
                            odds.mainOdds()[0][contadorDados_LAY],
                            # minutoEntrada[contadorDados_LAY], #Observar que pq nem todas as entradas há saidas de dados de tempo(minutos)
                            tempo.dadosTempo()[0][contadorDados_LAY],
                            # saidas_LAY[contadorDados_LAY],
                            odds.mainOdds()[1][contadorDados_LAY],
                            # minutoSaida[contadorDados_LAY],
                            tempo.dadosTempo()[1][contadorDados_LAY],
                            # resultadoOperacao[contadorDados_LAY],
                             'Ajuste',
                            tempo.dadosTempo()[2][contadorDados_LAY],
                             ]
      listaGeralFinalParaDF_LAY.append(dfEntradasDados_LAY)
      contadorDados_LAY += 1

    for jogosDF in listaGeralFinalParaDF_LAY:
      print(jogosDF)

    # print(listaGeralFinalParaDF_LAY)
    # return listaGeralFinalParaDF_LAY