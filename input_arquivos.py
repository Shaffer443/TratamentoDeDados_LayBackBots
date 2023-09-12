# Para importar os arquivos (.csv, .xlsx)

# importações:

import pandas as pd
import json
import csv
import os

def excel(arquivo):
    dados_excel = pd.read_excel(arquivo)
    print("\n")
    print(dados_excel)
    return dados_excel

def CSV(caminho,arquivo):
    # dadosNoArquivoCSV = []
    # Caminho do diretório onde o arquivo CSV está localizado
    diretorio = caminho

    # Nome do arquivo CSV que você deseja abrir
    nome_arquivo = arquivo

    # Caminho completo para o arquivo CSV
    caminho_arquivo = os.path.join(diretorio, nome_arquivo)

    # Verifica se o arquivo existe
    if not os.path.exists(caminho_arquivo):
        print(f'O arquivo {nome_arquivo} não foi encontrado no diretório {diretorio}.')
    else:
        # Abre o arquivo CSV e lê seu conteúdo
        with open(caminho_arquivo, 'r') as arquivo_csv:
            leitor_csv = csv.reader(arquivo_csv)

            # Itera pelas linhas do arquivo CSV e imprime o conteúdo
            # linho 0 é o nome da colunas
            contandoLinhas = 0
            for linha in leitor_csv:
                print(f"\n{contandoLinhas} - {linha}")
                # arquivando = linha
                # dadosNoArquivoCSV.append(arquivando)
                contandoLinhas += 1
            # print(f"\n{dadosNoArquivoCSV}")
            return caminho_arquivo


def uploadDoArquivo():
    print("\n1 - .CSV: nomedoarquivo.csv")
    print("2 - .XLSX (Execel): nomedoarquivo.csv")
    escolha = int(input("Escolha o tipo do arquivo para upload: "))

    if escolha == 1:
        return excel()
    if escolha == 2:
        return CSV()
    else:
        print("Erro. Escolha do arquivo ......FALHOU")

def diretorio():
    while True:
        print("\n")
        escolhaDiretorio = int(input("""Informe o diretório:
        1 - Diretório será: "/home/shaffer443/Downloads" (padrão)
        2 - Outro Diretório(Digitar o endereço)\n 
        Digite o número: """))

        if escolhaDiretorio == 1:
            return "/home/shaffer443/Downloads"
            break
        if escolhaDiretorio == 2:
            caminho = input("Digite o caminho (modelo: /home/shaffer443/Downloads): ")
            return caminho
            break
        else:
            print("Erro. Número inxesitente")
            print("informe o número existente.")

def arquivosNoDiretorio(caminhodiretorio):
    while True:
        # Diretório que você deseja listar
        diretorio = caminhodiretorio

        # Lista os arquivos no diretório
        arquivos = os.listdir(diretorio)

        # Itera pela lista de arquivos e imprime seus nomes
        print("\n")
        for arquivo in arquivos:
            print(arquivo)

        nomeDoArquivo = input("\nDigite o nome do arquivo: ")

        if nomeDoArquivo != "":
            return nomeDoArquivo
            break
        else:
            print("Arquivo não inserido.")
            print("Tente Novamente...")

######################################################################################################################

### Main deste script: ###

def main():
    # Diretório onde você deseja iniciar a busca
    diretorio_inicial = diretorio()

    # Nome do arquivo que você deseja encontrar
    nome_arquivo = arquivosNoDiretorio(diretorio_inicial)

    # Função para buscar o arquivo
    def buscar_arquivo(diretorio, nome_arquivo):
        for root, dirs, files in os.walk(diretorio):
            if nome_arquivo in files:
                return os.path.join(root, nome_arquivo)

        return None

    caminho_arquivo = buscar_arquivo(diretorio_inicial, nome_arquivo)

    if caminho_arquivo:
        print(f'O arquivo {nome_arquivo} foi encontrado em: {caminho_arquivo}')
        return CSV(diretorio_inicial, nome_arquivo)
    else:
        print(f'O arquivo {nome_arquivo} não foi encontrado no diretório {diretorio_inicial}.')





