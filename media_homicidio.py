# Ativar ambiente virtual (exemplos - descomente se necessário):
# venv\Scripts\activate
# .\venv\Scripts\activate
# venv\Scripts\activate.ps1

import pandas as pd
import numpy as np
# pip install scipy
from scipy.stats import trim_mean

def get_medias(df_dados_brutos):
    # Médias simples
    media_populacao = df_dados_brutos['População'].mean()
    media_homicidios = df_dados_brutos['Taxa Homicidios'].mean()

    # Médias aparadas (truncated mean)
    proporcao_corte = 0.1  # Corte de 10% em cada ponta
    media_aparada_populacao = trim_mean(df_dados_brutos['População'], proportiontocut=proporcao_corte)
    media_aparada_homicidios = trim_mean(df_dados_brutos['Taxa Homicidios'], proportiontocut=proporcao_corte)

    # Medianas
    mediana_populacao = df_dados_brutos['População'].median()
    mediana_homicidios = df_dados_brutos['Taxa Homicidios'].median()

    # Média ponderada (homicídios ponderados pela população)
    media_ponderada = np.average(df_dados_brutos['Taxa Homicidios'], weights=df_dados_brutos['População'])

    # Criar DataFrame com os resultados
    df_medias = pd.DataFrame({
        'População': [media_populacao, media_aparada_populacao, mediana_populacao, np.nan],
        'Taxa Homicidios': [media_homicidios, media_aparada_homicidios, mediana_homicidios, media_ponderada]
    }, index=['Média', 'Média Aparada', 'Mediana', 'Média Ponderada'])

    return df_medias

# Leitura do arquivo
df_dados_brutos = pd.read_csv('taxa_homicidios.csv')
print(df_dados_brutos)
# Cálculo das médias
df_medias = get_medias(df_dados_brutos)
print(df_medias.to_string(float_format="%.2f"))


        
def estimativas_variabilidade(dados_brutos, media):
    """
   Estimativas de Variabilidade
   Indica o quão espalhados/dispersos os dados estão em relação ao centro (média, mediana, moda)
      Desvios
      Diferença entre os valores observados e uma estimativa de localização (média, mediana, moda)
      - Desvio: tx_homicidio - media
      - Desvio Absoluto: |tx_homicidio - media|
      - Desvio Absoluto Médio: soma dos desvios / num desvios
      - Variância: soma(desvio^2) / num desvios - 1
      - Desvio Padrão: Raiz quadrada da variância
      Estatísticas de Ordem
      Estatísticas baseadas em dados ordenados (order)
      - Amplitude: valor máximo - valor mínimo
      - Percentil: Divide os valores em porcentagens           [10%, 20%, 30%, 40%, 50%, 60%, 70%, 80%, 90%, 100%]
      - Quantil: Mesmo que percentil, mas com casas decimais   [0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]
      - Quartil: Divide os valores em quatro partes iguais     [Q1 = 25%, Q2 = 50%, Q3 = 75%]
      - Amplitude Interquartil: Q3 - Q1
      - Mediana: Divide os valores em duas partes iguais       [med = Q2]
         Percentis
   """

estimativas_variabilidade(df_dados_brutos['Taxa homicidios'], np.mean(df_dados_brutos['Taxa homicidios']))
