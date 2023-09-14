# Variávies usandas como base - TESTE
import pandas as pd
import input_arquivos

df = input_arquivos.main()
dadosOriginais=pd.read_csv(df)

# variáveis:
dadosData = dadosOriginais['Data'] # Data e Hora
dadosOdds = dadosOriginais['Odd'] # Odds de Entrada e Saída(quando houver)
dadosTipo = dadosOriginais['Tipo'] # BACK ou LAY
dadosSelecao = dadosOriginais['Seleção'] # Mercado da Operação
dadosEvento = dadosOriginais['Evento'] # Times no evento casa e visitante
dadosTempoJogo = dadosOriginais['Tempo de jogo'] # Minuto do Back (in), minuto lay (out)
dadosCompeticao = dadosOriginais['Competição'] # Torneio
dadosTipoOperacao = dadosOriginais['Tipo de operação'] # Informa o motivo da entreda e principalmente da saída, pode ajudar na ajuste do método
