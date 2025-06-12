import pandas as pd
import numpy as np
from faker import Faker


# instancia do Faker para gerar nomes
fake = Faker('pt_BR')

# Condições dos dados [População]

media_notas = 70
desvio_padrao_notas = 10
num_alunos = 100
notas = np.random.normal(loc=media_notas, scale=desvio_padrao_notas, size=num_alunos)

print(f"notas random: {notas}")

notas = np.clip(notas, 0 , 100)
# --- Cálculos das Medidas ---
# 1. Média
media = np.mean(notas)
# 2. Mediana
mediana = np.median(notas)
# 3. desvios (Simples)
desvios = notas - media
# 4. desvio padrão
#Ex: 60(notas) - 70(media) = |10|(desvio)
desvios_absolutos = np.abs(notas - media)
# 5. Variância Individual
# Ex: 80(nota) - 70(media) = 10 * 10 = 100(variancia) 
variancias_individuais = (notas - media)**2
variancia = np.var(notas, ddof=1) # para variância amostral (n-1)
# 6. Desvio Padrão
desvio_padrao = np.std(notas)
# 7. Desvio Absoluto (Mediana)
desvios_abs_em_relacao_individuais = np.abs(notas - mediana)