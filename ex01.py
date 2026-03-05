import pandas as pd
import numpy as np

dados = np.array([12, 15, 17, 20, 22, 25, 28, 30, 35, 40])
q1 = np.percentile(dados, 25)
q2 = np.percentile(dados, 50)
q3 = np.percentile(dados, 75) 
print(f"Primeiro Quartil (Q1): {q1}")
print(f"Segundo Quartil (Q2, Mediana): {q2}") 
print(f"Terceiro Quartil (Q3): {q3}")

dados = 'https://www.ispdados.rj.gov.br/Arquivos/BaseDPEvolucaoMensalCisp.csv'
df = pd.read_csv(dados, encoding='latin-1', sep=';')   

# Agrupando os dados por 'cisp' e somando a coluna 'furto_celular'
df_furto_celular_cisp = df.groupby('cisp')['furto_celular'].sum().reset_index()

array_furto_celular = np.array(df_furto_celular_cisp['furto_celular'])
q1_furto_celular = np.percentile(array_furto_celular, 25)
q2_furto_celular = np.percentile(array_furto_celular, 50)
q3_furto_celular = np.percentile(array_furto_celular, 75) 
print(f"\nPrimeiro Quartil (Q1): {q1_furto_celular}")
print(f"Segundo Quartil (Q2, Mediana): {q2_furto_celular}") 
print(f"Terceiro Quartil (Q3): {q3_furto_celular}")

df_menor_q1_furto_celular = df_furto_celular_cisp.loc[df_furto_celular_cisp['furto_celular'] < q1_furto_celular]
print("\nCISPs com furto de celular menor que o primeiro quartil:")
print(df_menor_q1_furto_celular)    

print("\nCISPs ordenados por furto de celular (crescente):")    
ordem_crescente = df_menor_q1_furto_celular.sort_values(by='furto_celular')
print(ordem_crescente)

print("\nCISPs ordenados por furto de celular (decrescente):")    
ordem_decrescente = df_menor_q1_furto_celular.sort_values(by='furto_celular', ascending=False)
print(ordem_decrescente)    


#df_apreensao = df.groupby('cisp')['apreensao_drogas'].sum().reset_index()
#array_apreensao = np.array(df_apreensao['apreensao_drogas'])
#q1_apreensao = np.percentile(np.array(df_apreensao['apreensao_drogas']), 25)    
