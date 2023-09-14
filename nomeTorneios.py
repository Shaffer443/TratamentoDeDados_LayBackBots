import variaveis
import funcoes

# Tratamento competição LAY| Ajustes:

# Pegando TORNEIO da Operação
# Status = OK!
def mainTorneio():
    torneioDaEntrada_LAY = []

    funcoes.colhendoDadoscomLAY(variaveis.dadosCompeticao,torneioDaEntrada_LAY)

    # print(times)
    # print(torneioDaEntrada_LAY)
    print(f"Quantidade de Torneios: {len(torneioDaEntrada_LAY)}")
    return torneioDaEntrada_LAY