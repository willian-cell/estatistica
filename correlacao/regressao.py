# 1. Importação das libs
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
# pip install scikit-learn
from sklearn.linear_model import LinearRegression

# 2. Carregamento e preparação dos dados
EXPOSICAO_ALGODAO = 'data/LungDisease.csv'
dataframe = pd.read_csv(EXPOSICAO_ALGODAO)
print(dataframe.head())

# Gráfico de DISPERSÃO
# dataframe.plot.scatter(x = 'Exposure', y = 'PEFR')
# plt.show()

# 3. Configuração e treinamento do modelo
# Define a variáve preditora (independente), que é
# a Exposure e a variável de resultado que é o PEFR
predictors = ['Exposure']
outcome = 'PEFR'
# Instanciar o modelo
model = LinearRegression()
# Etapa d etreinamento
model.fit(dataframe[predictors], dataframe[outcome])

# 4. Exibição dos Coeficiente
# intercepto
print(f'Intercepto: {model.intercept_:.3f}')
# Coeficiente angular
print(f'Coeficiente Angular: {model.coef_[0]}')

# 5. Geração do gráfico
fig, (reg, ax, res) = plt.subplots(1, 3, figsize=(12, 4))
# Gráfico regreção
reg = sns.regplot(x = 'Exposure', y = 'PEFR', data = dataframe, ax = reg)

# Parcial
# Definir os limites dos eixos X e Y
ax.set_xlim(0, 23)
ax.set_ylim(295, 450)
# Definir os rótulos
ax.set_xlabel('Exposure')
ax.set_ylabel('PERF')
# Plotar a linha
ax.plot(dataframe['Exposure'], model.predict(dataframe[predictors]), '-')
# Adicionar o texto b0
ax.text(0.4, model.intercept_, r'$b_0$', size='larger')
x = pd.DataFrame({'Exposure': [7.5,17.5]})
y = model.predict(x)
print(y)
ax.plot((7.5, 7.5, 17.5), (y[0], y[1], y[1]), '--')

# Exibir DEltay e DeltaX no gráfico
ax.text(5, np.mean(y), r'$\Delta Y$', size='large')
ax.text(12, y[1] - 10, r'$\Delta Y$', size='large')

ax.text(12, 390, r'$b_1 = \frac{Danilo}{Willian}$', size='large')
# ax.text(12, 390, r'$b_1 = \frac{\Delta Y}{\Delta X}$', size='large')

# valores ajustados e resíduos
# Gera os valores ajustados do modelo
fitted = model.predict(dataframe[predictors])
# calcular residuos
residuals = dataframe[outcome] - fitted
res = dataframe.plot.scatter(x = 'Exposure', y = 'PEFR', ax =  res)

res.plot(dataframe.Exposure, fitted)
# Para cada valor de indice
for x, yatual, yfitted in zip(dataframe.Exposure, dataframe.PEFR, fitted):
    print(f'x: {x} - yreal: {yatual} - yreta: {yfitted}')
    res.plot((x, x), (yatual, yfitted), '--', color='C1')


plt.tight_layout()
plt.show()