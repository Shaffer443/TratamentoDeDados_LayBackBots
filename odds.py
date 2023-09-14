import variaveis
import funcoes

#ODDs Dos JOGOS LAY - ENTRADA E SAIDAS
# Tratamento 4: Dados Odds.
#status: OK

def mainOdds():
    entradas_LAY = []
    entradas_LAY_tratadas = []

    saidas_LAY = []
    saidas_LAY_tratadas = []

    contadorIndice = 0
    for valores in variaveis.dadosOdds:
        if variaveis.dadosTipo[contadorIndice] == 'BACK' and variaveis.dadosTipo[contadorIndice+1] == 'LAY':
          entradas_LAY.append(valores)
        if variaveis.dadosTipo[contadorIndice] == 'LAY' and variaveis.dadosTipo[contadorIndice-1] == 'BACK':
          saidas_LAY.append(valores)
        contadorIndice += 1


    # for e in entradas_LAY:
    #   print(f"{e:.2f}", end=",")
    #   # entradas_LAY_tratadas.append(e)
    print(f"Valores das Entradas(BACK) = {entradas_LAY} \ncom {len(entradas_LAY)} dados")

    # for s in saidas_LAY:
    #   print(f"{s:.2f}", end=",")
    #   # saidas_LAY_tratadas.append(s)
    print(f"\nValores da Saída(LAY) = {saidas_LAY} \ncom {len(saidas_LAY)} dados")


    print(f"\nOdds Média de Entrada: {sum(entradas_LAY)/len(entradas_LAY):.2f}")
    print(f"Odds Média de Saída: {sum(saidas_LAY)/len(saidas_LAY):.2f}")

    return entradas_LAY, saidas_LAY