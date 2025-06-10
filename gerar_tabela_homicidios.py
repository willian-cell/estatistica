import pandas as pd
from faker import Faker
import random 

fake = Faker('en_US')
# fake = Faker('pt_BR')

num_registros = 10

# função pra gerar o dataframe
def gerar_dados_brutos(num_registros):
    dados_brutos = []
    lista_cidades = set() # evitar repetiçoes da mesma cidade

    while len(dados_brutos) < num_registros:
        nome_cidade = fake.city()
        if nome_cidade not in lista_cidades:
            lista_cidades.add(nome_cidade)
            # gerando população aleatoria entre 10k e 5 Milhões
            populacao = fake.random_int(min=10000, max=5000000)
            # gerando taxa de homicidio entre 1.0 e 15.0 arredondado e uma casa decimal
            taxa_homicidios = round(random.uniform(1.0, 15.0), 1) #funçaõ pra arredondar números

            dados_brutos.append({
                "Cidade": nome_cidade,
                "População": populacao,
                "Taxa Homicidios": taxa_homicidios
            })

    return pd.DataFrame(dados_brutos)

df = gerar_dados_brutos(num_registros)
print("Dados Gerados:")
print(df)

output_csv_file = "taxa_homicidios.csv"
df.to_csv(output_csv_file, index=False)
