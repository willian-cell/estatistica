# https://we.tl/t-IcAhXWihEn

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

data = 'data/revisao.gz'

df = pd.read_csv(data) 

# removemos a primeira coluna chamada ADS
df = df.drop(columns=['ADS'])

# renomear coluna especifica
df = df.rename(columns={'Unnamed: 0': 'Data'})

# Transformar o campo data para datetime e settar ele como indice
df['Data'] = pd.to_datetime(df['Data'])
df = df.set_index('Data')

# encontrar a maior e a menor data
data_inicio = df.index.min()
data_fim = df.index.max()

print(f"\nQuantidade de variações coletadas: {len(df)}\n")
print(f"Período de coleta: {data_inicio.strftime('%d/%m/%Y')} à {data_fim.strftime('%d/%m/%Y')}")
#print(df.head())

# guardar o ativo sendo usado
ativo = 'CSC'

# encontrar o valor máximo e mínimo
maior_valor = df[ativo].max()
data_maior = df[ativo].idxmax()

menor_valor = df[ativo].min()
data_menor = df[ativo].idxmin()
print(f'valor {maior_valor} - data {data_maior}\n')
print("*"*30 )

print(f'Ativo analizado: {ativo}')
print(f"Maior variação diária: {maior_valor:.4f}")
print(f"Ocorreu no dia: {data_maior.strftime('%d/%m/%Y')}")
print(f"Maior variação diária: {menor_valor:.4f}")
print(f"Ocorreu no dia: {data_menor.strftime('%d/%m/%Y')}")

# Medidas de tendencia central
media = df[ativo].mean()
mediana = df[ativo].median()
moda = df[ativo].mode()

print(f"Medidas de tendência central para {ativo}")
print(f"Média: {media:.4f}")
print(f"Mediana: {mediana:.4f}")


if len(moda) > 0:
    print(f"Modas: {moda}")
else: 
    print(f"O ativo {ativo} é amodal")