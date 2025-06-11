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
