import pandas as pd

dados = 'https://www.ispdados.rj.gov.br/Arquivos/BaseDPEvolucaoMensalCisp.csv'
df = pd.read_csv(dados, encoding='latin-1', sep=';')   

# Exibir as colunas do DataFrame
#print(df.columns)

# Exibir as primeiras 10 linhas do DataFrame
#df.head(10)

# Exibir as últimas 10 linhas do DataFrame
#df.tail(10)

# Agrupando os dados por 'cisp' e somando a coluna 'furto_celular'
df_furto_celular_cisp = df.groupby('cisp')['furto_celular'].sum().reset_index()
print(df_furto_celular_cisp)

print(df.info())
#print(df.describe())
#print(df.shape())   

# Exibir as primeiras 5 linhas do DataFrame
#print(df.iloc[0:5])

#print(df.loc[df['munic'] == 'Rio de Janeiro'])

#df_2024 = df.loc[df['ano'] == 2024]
#df_2024_furto_celular_cisp = df_2024.groupby('cisp')['pessoas_desaparecidas'].count().reset_index()
#print(df_2024_furto_celular_cisp)   

# Filtrar os dados para o ano de 2020 e a região da Baixada Fluminense
baixada_2020 = df.loc[(df['ano'] == 2020) & (df['regiao'] == 'Baixada Fluminense')]
print(baixada_2020)
