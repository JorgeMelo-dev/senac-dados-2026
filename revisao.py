import pandas as pd

dados = 'https://www.ispdados.rj.gov.br/Arquivos/BaseDPEvolucaoMensalCisp.csv'
df = pd.read_csv(dados, encoding='latin-1', sep=';')   

# Exibir as colunas do DataFrame
print(df.columns)

# Exibir as primeiras 10 linhas do DataFrame
print(df.head(10))

# Exibir as últimas 10 linhas do DataFrame
print(df.tail(10))

# Agrupando os dados por 'cisp' e somando a coluna 'furto_celular'
df_furto_celular_cisp = df.groupby('cisp')['furto_celular'].sum().reset_index()
print(df_furto_celular_cisp)

