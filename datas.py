import variaveis
import funcoes

# DATA LISTA LAY:

# Tratamento 3: Pegando apenas a DATA da operação
# Status = OK!
def mainDatas():
    dataEventoSimplesLAY = []
    dataEventoSimplesLAY_Tratado = []

    funcoes.colhendoDadoscomLAY(variaveis.dadosData,dataEventoSimplesLAY )

    for qtd in dataEventoSimplesLAY:
      # print(qtd[:10])
      data = qtd[:10]
      dataEventoSimplesLAY_Tratado.append(data)

    # print("Datas Brutas:")
    # print(dataEventoSimplesLAY)

    if len(dataEventoSimplesLAY) == len(dataEventoSimplesLAY_Tratado):
      print(f"\nListas Comparadas ...... OK")
      # print(dataEventoSimplesLAY_Tratado)
      print(f"Quantidade de Datas na lista: {len(dataEventoSimplesLAY_Tratado)}")

      return dataEventoSimplesLAY_Tratado