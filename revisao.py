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

# guardar o ativo sendo usado
ativo = 'IBM'

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


# Estatistica de variabilidade
desvio_absoluto = np.abs(df[ativo] - media)
desvio_absoluto_medio = np.mean(desvio_absoluto)
variancia = np.var(df[ativo], ddof=1)
desvio_padrao = np.std(df[ativo], ddof=1)
print("*"*30 )
print("# Estatistica de variabilidade")
print(f"\nEstimativas de Variabilidade para: {ativo}\
      \nDesvio Absoluto Médio: {desvio_absoluto_medio:.4f}")
print(f"Desvio Padrão: {desvio_padrao:.4f}")

print(f"*" * 50)

# Graficos
serie_as_dataframe = pd.DataFrame(df[ativo])

# # Histograma
# plt.figure()
# sns.histplot(data=serie_as_dataframe)
# plt.xlabel("variação percentual diária")
# plt.ylabel("Ocorrencias de alterações")
# plt.title("Histograma")

# # Barras 
# plt.figure()
# sns.boxplot(data = serie_as_dataframe)
# plt.ylabel("variação percentual diária")
# plt.title("Boxplot")

# plt.figure()
# sns.kdeplot(data = serie_as_dataframe)
# plt.title("Densidade")
# plt.xlabel("Ocorrencias")
# plt.ylabel("Densidade")
# plt.show()

# Criar uma figura com 3 subplots (um em cima do outro)
fig, axes = plt.subplots(3, 1, figsize=(10, 12))  # 3 linhas, 1 coluna

# Histograma
sns.histplot(data=serie_as_dataframe, ax=axes[0], kde=False, color='skyblue')
axes[0].set_title("Histograma")
axes[0].set_xlabel("Variação percentual diária")
axes[0].set_ylabel("Ocorrências")

# Boxplot
sns.boxplot(data=serie_as_dataframe, ax=axes[1], orient='h', color='lightgreen')
axes[1].set_title("Boxplot")
axes[1].set_xlabel("Variação percentual diária")
axes[1].set_ylabel("")

# Densidade (KDE)
sns.kdeplot(data=serie_as_dataframe, ax=axes[2], fill=True, color='orange')
axes[2].set_title("Distribuição de Densidade (KDE)")
axes[2].set_xlabel("Variação percentual diária")
axes[2].set_ylabel("Densidade")


# Ajustar layout para evitar sobreposição
plt.tight_layout()
plt.show()