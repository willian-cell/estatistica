import pandas as pd
import matplotlib.pylab as plt
import seaborn as sns

# https://we.tl/t-sEka2cbohP

ATIVOS_CSV = 'data/revisao.gz'
SETORES_CSV = 'data/sp500_sectors.csv'

df_ativos = pd.read_csv(ATIVOS_CSV, index_col=0)
print(df_ativos.head())
df_setores = pd.read_csv(SETORES_CSV, index_col=1)
print(df_setores.head())

# telecomunições
df_telecom = df_setores[df_setores['sector'] == 'telecommunications_services']['symbol']

print(df_telecom.head())

# tivos telecomunicações
telecom_ativos = df_ativos.loc[df_ativos.index >='2012-07-01']
print(telecom_ativos.head())

# correlação
dados_correlacionados = telecom_ativos.corr()
print(dados_correlacionados.head())