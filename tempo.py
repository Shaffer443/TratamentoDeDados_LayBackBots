import variaveis
import funcoes

# Tratamento 02: Tempo de Exposição na Operação em LAY
# Pegando o tempo APENAS de exposição no RED. Já que no caso de Green o mercado desaparece, impossiilitando entrenda de "lay". logo Ela não existe para o mercado de Over 0,5
# Status = PRECISA DE AJUSTES!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

# PARA JOGOS COM saidas (Usando o LAY):
def dadosTempo():
    minutoEntrada = []
    minutoSaida = []
    tempoExpostoNaOperacao = []


    contador = 1
    contadorBACK_LAY = 0
    while contador < len(variaveis.dadosOriginais): #Estimativa pois pode ser que os ultimos jogos não entrem na conta
      # if dadosEvento[contador-1] == dadosEvento[contador]:
        if variaveis.dadosTipo[contador-1] == 'BACK' and variaveis.dadosTipo[contador] == 'LAY':
          # print(f"BACK:{contador}-{dadosTipo[contador] == 'BACK'}")
          # print(f"LAY:{contador}-{dadosTipo[contador] == 'LAY'}")
          minutoEntrada.append(variaveis.dadosTempoJogo[contador-1])
          minutoSaida.append(variaveis.dadosTempoJogo[contador])
          contadorBACK_LAY += 1
          # print("Entrada + saida")
        contador += 1


    # Exposição
    contadorExp = 0
    while contadorExp < len(minutoEntrada): #Estimativa pois pode ser que os ultimos jogos não entrem na conta
      exposicao = minutoSaida[contadorExp] - minutoEntrada[contadorExp]
      tempoExpostoNaOperacao.append(exposicao)
      contadorExp += 1


    print(minutoEntrada)
    print(minutoSaida)
    print("\n")
    print(tempoExpostoNaOperacao)

    print("\n")
    print(f"Quantidades de Entradas: {len(minutoEntrada)}")
    print(f"Quantidades de Saídas (Usando o Lay): {len(minutoSaida)}")
    print(f"Quantidade de jogos com minutagem de exposição de tempo: {len(tempoExpostoNaOperacao)}")

    print(f"Número de pares BACK + LAY: {contadorBACK_LAY}")

    return minutoEntrada, minutoSaida, tempoExpostoNaOperacao