import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score, mean_squared_error

HOUSE_CSV = 'data/house_sales.csv'
df_house = pd.read_csv(HOUSE_CSV, sep='\t')

predictors = ['SqFtTotLiving', 'SqFtLot', 'Bathrooms', 'Bedrooms', 'BldgGrade']
outcome = 'AdjSalePrice'

print(df_house[predictors].head())
print(df_house[outcome].head())

# Instância do modelo de regressão linear
house_lm = LinearRegression()

# Treinar o modelo, processo de ajuste
house_lm.fit(df_house[predictors], df_house[outcome])

print(f'Intercepto: {house_lm.intercept_:.3f}')
print('Coeficientes')

for name, coef in zip(predictors, house_lm.coef_):
    print(f' {name}: {coef}')

# havaliar a qualidade do modelo
fitterd = house_lm.predict(df_house[predictors])

# RMSE (Root Mean Squared Error)
# é uma medida da magnitude dos erros entre os valores previstos
RMSE = np.sqrt(mean_squared_error(df_house[outcome]), fitterd)

r2 = r2_score(df_house[outcome], fitterd)
print(f'RMSE: {RMSE:.0f}')
print(f'r2: {r2:.4f}')