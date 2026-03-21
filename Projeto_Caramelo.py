import pandas as pd
import numpy as np

pd.options.display.float_format = '{:,.2f}'.format

#dados = 'C:/Users/melo.jorge/Documents/Aula_09032026/senac-dados-2026/CARAMELO.csv'
dados = 'C:/Jorge/Python/PowerBI/BaseDados/CARAMELO.csv'
df = pd.read_csv(dados, sep=';', encoding='latin1')

# Converter coluna para numérico (tratando vírgula como decimal)
df['Valor de Venda'] = pd.to_numeric(df['Valor de Venda'].str.replace(',', '.'), errors='coerce')

# Agrupamento por loja
df_Loja = df.groupby('Loja')['Valor de Venda'].sum().reset_index()

# Garantir que a coluna seja numérica (decimal)
df_Loja['Valor de Venda'] = pd.to_numeric(df_Loja['Valor de Venda'], errors='coerce')
print(df_Loja)

# Gravar resultado em CSV
df_Loja.to_csv('C:/Jorge/Python/PowerBI/BaseDados/df_Loja.csv', 
               sep=';', 
               index=False, 
               encoding='latin1')

# Converter para array NumPy
array_Loja = df_Loja['Valor de Venda'].to_numpy(dtype=float)

# Quartis
q1_Loja = np.percentile(array_Loja, 25)
q2_Loja = np.percentile(array_Loja, 50)  # Mediana
q3_Loja = np.percentile(array_Loja, 75)

# Estatísticas
media = np.mean(array_Loja)
mediana = np.median(array_Loja)
distancia = ((media - mediana) / mediana) * 100
iqr_Loja = q3_Loja - q1_Loja

# Limites para outliers
limite_superior = q3_Loja + (1.5 * iqr_Loja)
limite_inferior = q1_Loja - (1.5 * iqr_Loja)

# Impressão formatada
print(f'\nPrimeiro quartil (Q1): {q1_Loja:.2f}')
print(f'Segundo quartil (Q2, Mediana): {q2_Loja:.2f}')
print(f'Terceiro quartil (Q3): {q3_Loja:.2f}')

print(f"Media = {media:.2f}")
print(f"Mediana = {mediana:.2f}")
print(f"Distancia = {distancia:.2f}%")#

print(f'IQR = {iqr_Loja:.2f}')
print(f'Limite Superior = {limite_superior:.2f}')
print(f'Limite Inferior = {limite_inferior:.2f}')

# Outliers
outliers_Loja = df_Loja.loc[df_Loja['Valor de Venda'] >= limite_superior]
outliers_Loja = outliers_Loja.sort_values(by='Valor de Venda', ascending=False)

print("\nOutliers encontrados:")
print(outliers_Loja)
