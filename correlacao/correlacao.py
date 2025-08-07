import pandas as pd
import matplotlib.pylab as plt
import seaborn as sns

# Arquivos de dados
ATIVOS_CSV = 'data/sp500_data.csv.gz'
SETORES_CSV = 'data/sp500_sectors.csv'

# Leitura dos dados
df_ativos = pd.read_csv(ATIVOS_CSV, index_col=0)
df_setores = pd.read_csv(SETORES_CSV, index_col=1)

print(df_ativos.head())
print(df_setores.head())

# Lista de símbolos do setor de telecomunicações
telecom_symbols = df_setores[df_setores['sector'] == 'telecommunications_services']['symbol'].tolist()

# Preços das empresas de telecom a partir de 2012-07-01
df_telecom = df_ativos.loc[df_ativos.index >= '2012-07-01', telecom_symbols]
print(df_telecom.head())

# Correlação das empresas de telecom
telecom_corr = df_telecom.corr()
print(telecom_corr.head())

# Lista de símbolos de ETFs
etf_symbols = df_setores[df_setores['sector'] == 'etf']['symbol'].tolist()

# Preços de ETFs a partir de 2012-07-01
df_etf = df_ativos.loc[df_ativos.index >= '2012-07-01', etf_symbols]
print(df_etf.head())

# Correlação dos ETFs
etf_corr = df_etf.corr()
print(etf_corr.head())

# Plotando
fig, (telecomax, etfax) = plt.subplots(1, 2, figsize=(14, 6))

sns.heatmap(telecom_corr,vmin=-1, vmax=1,cmap=sns.diverging_palette(20, 220, as_cmap=True),ax=telecomax)
telecomax.set_title("Correlação - Telecomunicações")

sns.heatmap(etf_corr,vmin=-1, vmax=1,cmap=sns.diverging_palette(20, 220, as_cmap=True),ax=etfax)
etfax.set_title("Correlação - ETFs")

plt.tight_layout()
plt.show()
