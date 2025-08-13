import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Configurações gerais do app
st.set_page_config(page_title="Análise de Variações Diárias", layout="wide")
st.title(" WBO - Tecnologia: Analisador Dinâmico ")

# Upload do arquivo ou uso do caminho fixo
data = 'data/sp500_data.csv.gz'

if data is not None:
    df = pd.read_csv(data)

    # Limpeza dos dados
    df = df.drop(columns=['ADS'])
    df = df.rename(columns={'Unnamed: 0': 'Data'})
    df['Data'] = pd.to_datetime(df['Data'])
    df = df.set_index('Data')

    st.success("Dados carregados com sucesso!")

    # Informações básicas
    data_inicio = df.index.min()
    data_fim = df.index.max()

    st.markdown(f"**Período de coleta:** {data_inicio.strftime('%d/%m/%Y')} à {data_fim.strftime('%d/%m/%Y')}")
    st.markdown(f"**Quantidade de variações coletadas:** {len(df)}")

    # Seleção do ativo
    ativos = df.columns.tolist()
    st.subheader("🔎 Selecione ou digite o ativo para análise")

    col1, col2 = st.columns([2, 3])
    with col1:
        ativo_selecionado = st.selectbox("Escolha um ativo disponível:", ativos)

    with col2:
        ativo_digitado = st.text_input("Ou digite o nome do ativo:", value=ativo_selecionado)

    # Confirma se o ativo digitado é válido
    if ativo_digitado in ativos:
        ativo = ativo_digitado
    else:
        st.error(f"O ativo '{ativo_digitado}' não foi encontrado nos dados.")
        st.stop()

    # Análise estatística
    maior_valor = df[ativo].max()
    data_maior = df[ativo].idxmax()
    menor_valor = df[ativo].min()
    data_menor = df[ativo].idxmin()
    media = df[ativo].mean()
    mediana = df[ativo].median()
    moda = df[ativo].mode()

    st.subheader(f"Estatísticas para o ativo: {ativo}")
    col1, col2 = st.columns(2)
    with col1:
        st.metric("Maior Variação", f"{maior_valor:.4f}", f"{data_maior.strftime('%d/%m/%Y')}")
        st.metric("Menor Variação", f"{menor_valor:.4f}", f"{data_menor.strftime('%d/%m/%Y')}")
    with col2:
        st.metric("Média", f"{media:.4f}")
        st.metric("Mediana", f"{mediana:.4f}")
        if not moda.empty:
            st.write("Modas:", moda.values)
        else:
            st.write("Amodal")

    # Estatísticas de variabilidade
    st.subheader("Estatísticas de Variabilidade")
    desvio_absoluto = abs(df[ativo] - media)
    desvio_absoluto_medio = desvio_absoluto.mean()
    variancia = df[ativo].var(ddof=1)
    desvio_padrao = df[ativo].std(ddof=1)

    col3, col4 = st.columns(2)
    with col3:
        st.metric("Desvio Absoluto Médio", f"{desvio_absoluto_medio:.4f}")
        st.metric("Variância", f"{variancia:.4f}")
    with col4:
        st.metric("Desvio Padrão", f"{desvio_padrao:.4f}")

    # Gráfico de linha - Série Temporal
    st.subheader("Série Temporal")
    fig, ax = plt.subplots(figsize=(12, 4))
    sns.lineplot(data=df[ativo], ax=ax)
    ax.set_title(f"Variação diária de {ativo}")
    ax.set_ylabel("Valor")
    st.pyplot(fig)

    # Análises gráficas agrupadas: Histograma, Boxplot e Densidade
    st.subheader("Distribuições Estatísticas")

    serie_as_dataframe = df[ativo].dropna()  # remover possíveis NaNs
    fig2, axes = plt.subplots(3, 1, figsize=(10, 12))

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

    plt.tight_layout()
    st.pyplot(fig2)

else:
    st.warning("Por favor, carregue um arquivo `.gz` para iniciar a análise.")
