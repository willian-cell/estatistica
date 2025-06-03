import pandas as pd
import numpy as np
import math 

# -- estudo de caso 01: idade dos alunos

def analisar_dados_estatisticos(dados_brutos, nome_do_conjunto):
    print(f"\n -- análise Estatistica para: {nome_do_conjunto} ---")

    rol = sorted(dados_brutos)
    print("rol de dados")
    print(f"{rol}")


    # 2. tamanho de amostra (n)
    n = len(rol)
    print("\n2. Tamanho da Amostra (n):")
    print(f"n = {n}")

    # 3. Valor Máximo e Mínimo

    x_min = rol[0]
    x_max = rol[-1]
    print("\n Utilizando a fubnçãop sorted(dados_brutos):")
    print(f" Maximo: {x_max}")
    print(f" Mínimo: {x_min}")


    # 4. Amplitude Total (AT)

    at = x_max - x_min
    print(f"\n Amplitude Total (AT): {at:.2f}")

    # 5. Números de classes (K) Intervaos de idade:

    k = math.ceil(math.sqrt(n)) # ceil aredonda raiz quadrada pra cima
    print(f"\n  Número de Classes (K) = {k}")

    # 6 amplitude das classes (H)
    h= at/k
    print(f"\n Amplitude das Classes: {h}")

    # Arredondar amplitude das classes
    num_casas_decimais = 0
    if at < k:
        num_casas_decimais = 1
        if at * 10 < k:
            num_casas_decimais = 2

    h = np.ceil(h*(10**num_casas_decimais)) / (10**num_casas_decimais)
    print(f"\n h: {int(h)}")

dados_idades = [21, 21, 21, 22, 22, 22, 23, 23, 23, 23, 24, 24, 25, 25, 25, 26, 27, 27, 28, 28, 30, 30, 31, 31, 31]
df_idades = analisar_dados_estatisticos(dados_idades, "Idades dos Alunos")
# print(df_idades.to_string())

