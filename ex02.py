import pandas as pd
import numpy as np

dados = 'https://www.ispdados.rj.gov.br/Arquivos/BaseDPEvolucaoMensalCisp.csv'
df = pd.read_csv(dados, encoding='latin-1', sep=';')   

getao_atual = [2023,2024,2025,2026]
df_interior_atual = df.loc[(df['regiao'] == 'Interior') & (df['ano'].isin(getao_atual))]
                           
print("Dados do Interior para os anos atuais:")
print(df_interior_atual)
                     

