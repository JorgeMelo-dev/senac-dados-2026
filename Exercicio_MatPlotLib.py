'''

import pandas as pd
import matplotlib.pyplot as plt

df = pd.DataFrame(
    {'dias': ['Segunda', 'Terça', 'Quarta', 'Quinta', 'Sexta'],
     'Venda': [500, 200, 1000, 150, 1950]})

plt.plot(df['dias'], df['Venda'], marker='o', linestyle='-', color='blue')
plt.title('Vendas por Dias')
plt.xlabel('Dia da Semana')
plt.ylabel('Valor Vendido')
plt.show()

'''

'''

import pandas as pd
import matplotlib.pyplot as plt

df = pd.DataFrame(
    {'dias': ['Segunda', 'Terça', 'Quarta', 'Quinta', 'Sexta'],
     'Venda': [500, 200, 1000, 150, 1950]})

plt.bar(df['dias'], df['Venda'], color='blue')
plt.title('Vendas por Dias')
plt.xlabel('Dia da Semana')
plt.ylabel('Valor Vendido')
plt.show()

'''

'''

import pandas as pd
#import numpy as np
import matplotlib.pyplot as plt

dados = 'https://www.ispdados.rj.gov.br/Arquivos/BaseDPEvolucaoMensalCisp.csv'
df = pd.read_csv(dados, sep=';', encoding='latin1')

df_aaapai = df.groupby('cisp')['aaapai'].sum().reset_index()
df_aaapai['cisp'] = df_aaapai['cisp'].astype(str)

plt.figure(figsize=(15,10))
plt.bar(df_aaapai['cisp'], df_aaapai['aaapai'], color='blue')
plt.title('Apreensão de Menores por Delegacias')
plt.show()

'''

'''

import pandas as pd
import matplotlib.pyplot as plt

dados = 'https://www.ispdados.rj.gov.br/Arquivos/BaseDPEvolucaoMensalCisp.csv'
df = pd.read_csv(dados, sep=';', encoding='latin1')

max_ano = max(df['ano'])
#df = df.loc[(df['ano'] > 2024) & (df['regiao'] == 'Capital')]
df = df.loc[(df['ano'] >= max_ano - 1) & (df['ano'] < max_ano)]
df_estelionato = df.groupby('mes_ano')['estelionato'].sum().reset_index()
df_estelionato['mes_ano'] = df_estelionato['mes_ano'].astype(str)

plt.figure(figsize=(15,10))
plt.plot(df_estelionato['mes_ano'], df_estelionato['estelionato'], color='blue')
plt.title('Evolução de Estelionato por Mês')
plt.show()

'''

'''

import pandas as pd
import matplotlib.pyplot as plt

df_dias = pd.DataFrame(
                        {'Dias': ['Segunda', 'Terça', 'Quarta', 'Quinta', 'Sexta'],
                        'Venda': [500, 200, 1000, 150, 1950]})

df_produto = pd.DataFrame(
                            {'Produto': ['PÃO', 'QUEIJO', 'PRESUNTO'],
                            'Vendas': [120, 90, 150]})


# Cria uma figura com 4 áreas de gráficos (2 linhas x 2 colunas)
fig, axs = plt.subplots(2, 2, figsize=(12, 8))
# axs é uma matriz 2x2 de objetos Axes, onde cada posição representa um gráfico específico:
# axs[0, 0] → linha 0, coluna 0 → canto superior esquerdo
# axs[0, 1] → linha 0, coluna 1 → canto superior direito
# axs[1, 0] → linha 1, coluna 0 → canto inferior esquerdo
# axs[1, 1] → linha 1, coluna 1 → canto inferior direito

# Gráfico 1: Linha - Vendas por dia da semana
axs[0, 0].plot(df_dias['Dias'], df_dias['Venda'], marker='o', linestyle='-', color='#FF8C00')
# axs[0, 0] acessa o primeiro gráfico (linha 0, coluna 0)
# .plot() desenha uma linha conectando os valores de venda por dia
axs[0, 0].set_title('Vendas por Dia da Semana')   # Título do gráfico
axs[0, 0].set_xlabel('Dia da Semana')    # Rótulo do eixo X
axs[0, 0].set_ylabel('Valor Vendido')    # Rótulo do eixo Y

# Gráfico 2: Barras verticais - Vendas por produto
axs[0, 1].bar(df_produto['Produto'], df_produto['Vendas'], color='green')
# axs[0, 1] acessa o segundo gráfico (linha 0, coluna 1)
# .bar() desenha barras verticais para cada produto
axs[0, 1].set_title('Vendas por Produto')       # Título do gráfico
axs[0, 1].set_xlabel('Produto')                 # Rótulo do eixo X
axs[0, 1].set_ylabel('Vendas')                  # Rótulo do eixo Y

# Gráfico 3: Barras horizontais - Vendas por produto
axs[1, 0].barh(df_produto['Produto'], df_produto['Vendas'], color='orange')
# axs[1, 0] acessa o terceiro gráfico (linha 1, coluna 0)
# .barh() desenha barras horizontais para os produtos
axs[1, 0].set_title('Vendas por Produto (Horizontal)')  # Título do gráfico
axs[1, 0].set_xlabel('Vendas')                          # Rótulo do eixo X
axs[1, 0].set_ylabel('Produto')                         # Rótulo do eixo Y


# Gráfico 4: Quadro de texto explicativo
axs[1, 1].axis('off')  # axs[1, 1] acessa o quarto gráfico (linha 1, coluna 1)
# .axis('off') oculta os eixos para transformar o espaço em um quadro de texto

# Inserção de texto explicativo no gráfico 4
axs[1, 1].text(0.1, 1, 'Resumo da Aula:', fontsize=14, color='black')
# .text(x, y, texto) insere texto na posição (10% largura, 100% altura)
# fontsize define o tamanho da fonte, color define a cor

axs[1, 1].text(0.1, 0.6, '- subplots usa matriz de eixos', fontsize=12)
# Explica que plt.subplots() retorna uma matriz de objetos Axes
# Cada gráfico é acessado por sua posição: axs[linha, coluna]
axs[1, 1].text(0.1, 0.7, 'Senac Rio de Janeiro', fontsize=12)

axs[1, 1].text(0.1, 0.5, '- mais controle sobre cada gráfico', fontsize=12)
# Destaca que podemos configurar cada gráfico individualmente

axs[1, 1].text(0.1, 0.4, '- ideal para projetos mais complexos', fontsize=12)
# Mostra que subplots são úteis para dashboards e relatórios com múltiplas visualizações

# Ajusta os espaços entre os gráficos para evitar sobreposição
plt.tight_layout()

# Exibe todos os gráficos juntos
plt.show()

'''

'''

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

dados = 'https://www.ispdados.rj.gov.br/Arquivos/BaseDPEvolucaoMensalCisp.csv'
df = pd.read_csv(dados, sep=';', encoding='latin1')

df_furto_celular_cisp = df.groupby('cisp')['furto_celular'].sum().reset_index()

df_top_5 = df_furto_celular_cisp.head()
df_ultimos_5 = df_furto_celular_cisp.tail()

array_furto_celular = np.array(df_furto_celular_cisp['furto_celular'])
q1_furto_celular = np.percentile(array_furto_celular, 25)
q2_furto_celular = np.percentile(array_furto_celular, 50)
q3_furto_celular = np.percentile(array_furto_celular, 75)

media = np.mean(array_furto_celular)
mediana = np.median(array_furto_celular)
distancia = ((media - mediana) / mediana) * 100
iqr = q3_furto_celular - q1_furto_celular
limite_superior = q3_furto_celular + (1.5 * iqr)
limite_inferior = q1_furto_celular - (1.5 * iqr)

outliers_cisp_furto_celular = df_furto_celular_cisp.loc[df_furto_celular_cisp['furto_celular'] >= limite_superior]
outliers_cisp_furto_celular = outliers_cisp_furto_celular.sort_values(by='furto_celular', ascending=False)


# Cria uma figura com 4 áreas de gráficos (2 linhas x 2 colunas)
fig, axs = plt.subplots(2, 2, figsize=(12, 8))
# axs é uma matriz 2x2 de objetos Axes, onde cada posição representa um gráfico específico:
# axs[0, 0] → linha 0, coluna 0 → canto superior esquerdo
# axs[0, 1] → linha 0, coluna 1 → canto superior direito
# axs[1, 0] → linha 1, coluna 0 → canto inferior esquerdo
# axs[1, 1] → linha 1, coluna 1 → canto inferior direito

# Gráfico 1: Linha - Vendas por dia da semana
axs[0, 0].plot(df_top_5['cisp'], df_top_5['furto_celular'], marker='o', linestyle='-', color='#FF8C00')
# axs[0, 0] acessa o primeiro gráfico (linha 0, coluna 0)
# .plot() desenha uma linha conectando os valores de venda por dia
axs[0, 0].set_title('TOP 5')           # Título do gráfico
axs[0, 0].set_xlabel('Delegacias')     # Rótulo do eixo X
axs[0, 0].set_ylabel('Furto Celular')  # Rótulo do eixo Y


# Gráfico 2: Barras verticais - Vendas por produto
axs[0, 1].bar(df_ultimos_5['cisp'], df_ultimos_5['furto_celular'], color='green')
# axs[0, 1] acessa o segundo gráfico (linha 0, coluna 1)
# .bar() desenha barras verticais para cada produto
axs[0, 1].set_title('Últimos 5')       # Título do gráfico
axs[0, 1].set_xlabel('Delegacias')     # Rótulo do eixo X
axs[0, 1].set_ylabel('Furto Celular')  # Rótulo do eixo Y


# Gráfico 3: Barras horizontais - Vendas por produto
axs[1, 0].barh(outliers_cisp_furto_celular['cisp'], outliers_cisp_furto_celular['furto_celular'], color='orange')
# axs[1, 0] acessa o terceiro gráfico (linha 1, coluna 0)
# .barh() desenha barras horizontais para os produtos
axs[1, 0].set_title('OUTLIERS')        # Título do gráfico
axs[1, 0].set_xlabel('Delegacias')     # Rótulo do eixo X
axs[1, 0].set_ylabel('Furto Celular')  # Rótulo do eixo Y


# Gráfico 4: Quadro de texto explicativo
axs[1, 1].axis('off')  # axs[1, 1] acessa o quarto gráfico (linha 1, coluna 1)
# .axis('off') oculta os eixos para transformar o espaço em um quadro de texto

# Inserção de texto explicativo no gráfico 4
axs[1, 1].text(0.1, 1, 'Resumo da Aula:', fontsize=14, color='black')
# .text(x, y, texto) insere texto na posição (10% largura, 100% altura)
# fontsize define o tamanho da fonte, color define a cor

axs[1, 1].text(0.1, 0.9, f'Primeiro quartil (Q1): {q1_furto_celular}', fontsize=10)
axs[1, 1].text(0.1, 0.8, f'Segundo quartil (Q2, Mediana): {q2_furto_celular}', fontsize=10)
axs[1, 1].text(0.1, 0.7, f'Terceiro quartil (Q3): {q3_furto_celular}', fontsize=10)
axs[1, 1].text(0.1, 0.6, f'Media é {media}', fontsize=10)
axs[1, 1].text(0.1, 0.5, f'Mediana é {mediana}', fontsize=10)
axs[1, 1].text(0.1, 0.4, f'Distância é {distancia}', fontsize=10)
axs[1, 1].text(0.1, 0.3, f'IQR é {iqr}', fontsize=10)
axs[1, 1].text(0.1, 0.2, f'Limite Superior é {limite_superior}', fontsize=10)
axs[1, 1].text(0.1, 0.1, f'Limite Inferior é {limite_inferior}', fontsize=10)


# Ajusta os espaços entre os gráficos para evitar sobreposição
plt.tight_layout()

# Exibe todos os gráficos juntos
plt.show()

'''


'''

import pandas as pd
import matplotlib.pyplot as plt

dados = 'https://www.ispdados.rj.gov.br/Arquivos/BaseDPEvolucaoMensalCisp.csv'
df = pd.read_csv(dados, sep=';', encoding='latin1')

df_veiculos = df.groupby('mes_ano')[['furto_veiculos', 'roubo_veiculo', 'recuperacao_veiculos']].sum().reset_index()
#print(df_veiculos)

plt.figure(figsize=(15,8))
plt.scatter(df_veiculos['recuperacao_veiculos'], df_veiculos['roubo_veiculo'])
plt.xlabel('Recuperação Veículos')
plt.ylabel('Roubo Veículos')
plt.title('Disperssão de Roubo e Recuperação de Veículos')
plt.show()

'''


import pandas as pd
import matplotlib.pyplot as plt

dados = 'https://www.ispdados.rj.gov.br/Arquivos/BaseDPEvolucaoMensalCisp.csv'
df = pd.read_csv(dados, sep=';', encoding='latin1')

df_veiculos = df.groupby('mes_ano')[['furto_veiculos', 'roubo_veiculo', 'recuperacao_veiculos']].sum().reset_index()

plt.figure(figsize=(15,8))
plt.scatter(df_veiculos['recuperacao_veiculos'], df_veiculos['furto_veiculos'])
plt.xlabel('Recuperação Veículos')
plt.ylabel('Furto Veículos')
plt.title('Disperssão de Furto e Recuperação de Veículos')
plt.show()
