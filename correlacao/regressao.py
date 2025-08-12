# importação das libs
import pandas as pd
import matplotlib.pylab as plt
import seaborn as sns
import numpy as np

# pip install scikit-learn
from sklearn.linear_model import LinearRegression

#2. Carregamento e preparação dos dados
EXPOSICAO_ALGODAO = 'data/LungDisease.csv'
dataframe = pd.read_csv(EXPOSICAO_ALGODAO)
print(dataframe)

# Grafico de Disperção:
# dataframe.plot.scatter(x = 'Exposure', y = 'PEFR')
# plt.show()

#3. Configuração de treinamento do modelo
preditors = ['Exposure'] # variável de analise e treino
outcome = 'PEFR' # variável de resposta depois da análise

# Instanciar o modelo
model = LinearRegression()

# treinar
model.fit(dataframe[preditors], dataframe[outcome])

# 4. Exibição dos coeficientes
# intercepto
print(f"Intercepto: {model.intercept_:.2f}")
# coeficiente angular
print(f"Coeficiente Angular: {model.coef_[0]}")

# 5. Gerar Graficos
fig, (reg) = plt.subplots(1, 1, figsize=(4, 4))

# Grafico regreção
reg = sns.regplot(x = 'Exposure', y = 'PEFR', data = dataframe, ax = reg)
plt.tight_layout()
plt.show()

