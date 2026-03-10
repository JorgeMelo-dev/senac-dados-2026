import pandas as pd
import numpy as np

dados_1sem = 'Preços semestrais - AUTOMOTIVOS_2025.01.csv'
df_1sem = pd.read_csv(dados_1sem, sep=';')
df_1sem.head(3)

dados_2sem = 'Preços semestrais - AUTOMOTIVOS_2025.02.csv'
df_2sem = pd.read_csv(dados_2sem, sep=';')
df_2sem.head(3)

df_anp = pd.concat([df_1sem, df_2sem], ignore_index= True)

df_anp['Valor de Venda'] = df_anp['Valor de Venda'].str.replace(',','.').astype(float)

df_gasolina = df_anp.loc[df_anp['Produto'] == 'GASOLINA']
df_etanol = df_anp.loc[df_anp['Produto'] == 'ETANOL']

df_media_gasolina = df_gasolina.groupby('Estado - Sigla')['Valor de Venda'].mean().reset_index()
df_media_gasolina

df_media_por_regiao_gasolina = df_gasolina.groupby('Regiao - Sigla')['Valor de Venda'].mean().reset_index()
df_media_por_regiao_gasolina

# Ordena do maior para o menor preço médio por região
ranking_regioes = df_media_por_regiao_gasolina.sort_values(by='Valor de Venda', ascending=False).head(5)
ranking_regioes

# Ordena do menor para o maior
menores_regioes = df_media_por_regiao_gasolina.sort_values(by='Valor de Venda', ascending=True).head(5)
menores_regioes

# Ordena do maior para o menor
ranking = df_media_gasolina.sort_values(by='Valor de Venda', ascending=False).head(5)

# Exibe o ranking
ranking

df_media_etanol = df_etanol.groupby('Estado - Sigla')['Valor de Venda'].mean().reset_index()
df_media_etanol

df_media_por_regiao_etanol = df_etanol.groupby('Regiao - Sigla')['Valor de Venda'].mean().reset_index()
df_media_por_regiao_etanol

ranking = df_media_etanol.sort_values(by='Valor de Venda', ascending=False).head(5)

# Exibe o ranking
ranking