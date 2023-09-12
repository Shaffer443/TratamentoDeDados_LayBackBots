# Salvar arquivo com saida em .csv

import os
import os.path
import time
import sys

agora = time.localtime()

dadosNomeArquivo = []

# Configurando a pasta PAI:

diretorioParaSalvar = "/home/shaffer443/Downloads"
os.chdir(f'{diretorioParaSalvar}') # Diretório Pai, referencia para salvar

#Salvando o arquivo
def salvar(arquivoSalvando,nomeDoArquivo):
    arquivo = open(f"{nomeDoArquivo}","w+")
    arquivo.write(f"{arquivoSalvando}")
    arquivo.close()


def verificandoDados(nomeDoArquivo):
    contador = 0
    while contador < len(sys.argv):
        if sys.argv[contador] == nomeDoArquivo:
            print(f"{sys.argv[contador]}")
            break
            return sys.argv[contador]
        contador += 1



def diaSemana(tm_wday):
    diaDaSemana = ['Segunda', 'Terça', 'Quarta', 'Quinta', 'Sexta', 'Sábado', 'Domingo']
    nomeDoDiaNaSemana = diaDaSemana[tm_wday]
    return nomeDoDiaNaSemana

def mes(tm_mon):
    nomeMes = ['Janeiro','Fevereiro','Março','Abril', 'Maio', 'Junho', 'Julho', 'Agosto','Setembro', 'Outrubro', 'Novembro', 'Dezembro']
    nomeDoMes = nomeMes[tm_mon - 1]
    return nomeDoMes


def dadosHoraeData(agora):
    print(f"\n{agora}")
    diaRestantes = agora.tm_yday - 365
    dia = diaSemana(agora.tm_wday)
    data = agora.tm_mday
    mes_ = mes(agora.tm_mon)
    ano_ = agora.tm_year
    hora = agora.tm_hour
    min = agora.tm_min
    diasCorridos = agora.tm_yday
    diasRestantes = diaRestantes
    # print(f"Dia Da Semana: {diaSemana(agora.tm_wday)}")
    # print(f"Data: {agora.tm_mday}")
    # print(f"Mês: {mes(agora.tm_mon)}")
    # print(f"Ano: {agora.tm_year}")
    # print(f"Hora: {agora.tm_hour} h")
    # print(f"Minuto: {agora.tm_min} min")
    # print(f"Quantidade de dias corridos no Ano: {agora.tm_yday} dia(s)")
    # print(f"Quantidade de dias para terminar o Ano: {diaRestantes} dia(s)")
    return dia, data, mes_,ano_,hora,min, diasCorridos, diasRestantes



contador = 0
while contador < 8:
    dadosNomeArquivo.append(dadosHoraeData(agora)[contador])
    contador += 1

# dadosNomeArquivo= {'Dia': dadosHoraeData(agora)[0],
#                        'Data': dadosHoraeData(agora)[1],
#                        'Mês': dadosHoraeData(agora)[2],
#                        'Ano': dadosHoraeData(agora)[3],
#                        'Hora': dadosHoraeData(agora)[4],
#                        'Minutos': dadosHoraeData(agora)[5]}

# def salvarEmCSV(dataframe):
#     # Especifique o nome do arquivo CSV para salvar
#     nome_arquivo = f"{dadosNomeArquivo[0]}_{dadosNomeArquivo[1]}_{dadosNomeArquivo[2]}_{dadosNomeArquivo[3]}_{dadosNomeArquivo[4]}_{dadosNomeArquivo[5]}dados.csv"
#     criacaoArquivo= open(f"{nome_arquivo}",'w')
#     for tuplas in dataframe.readlines():
#         criacaoArquivo.write(f"{tuplas}\n")
#     criacaoArquivo.close()


def dataframeParaCSV(dataframe):
    nome_arquivo = f"{dadosNomeArquivo[0]}_{dadosNomeArquivo[1]}_{dadosNomeArquivo[2]}_{dadosNomeArquivo[3]}_{dadosNomeArquivo[4]}_{dadosNomeArquivo[5]}_dados"
    # saving the dataframe no Diretório "/Downloads"
    return dataframe.to_csv(f"{nome_arquivo}.csv",index=False)


# Chamdas para testes do script:

# dadosHoraeData(agora)