import pandas as pd
import numpy as np
import math 

# -- estudo de caso 01: idade dos alunos

def analisar_dados_estatisticos(dados_brutos, nome_do_conjunto):
    print(f"-- análise Estatistica para: {nome_do_conjunto} ---")

    rol = sorted(dados_brutos)
    print("rol de dados")
    print(f"{rol}")


    # 2. tamanho de amostra (n)
    n = len(rol)
    print("\n2. Tamanho da Amostra (n):")
    print(f"n = {n}")



dados_idades = [21, 21, 21, 22, 22, 22, 23, 23, 23, 23, 24, 24, 25, 25, 25, 26, 27, 27, 28, 28, 30, 30, 31, 31, 31]
df_idades = analisar_dados_estatisticos(dados_idades, "Idades dos Alunos")
# print(df_idades.to_string())