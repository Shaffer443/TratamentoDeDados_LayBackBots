# Pegandos os valores apenas dos Indices:

def linhaPorLinha(arquivo):
    qtdIndex = arquivo
    for row in qtdIndex.index:
        print(row)

def qtdLinhasIndices(arquivo):
    qtdIndex = arquivo
    return len(qtdIndex)