# Importando as bibliotecas necessárias
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import os
import sys

# Definindo o tema visual padrão para os seus gráficos:
sns.set_theme()  

# Definindo uma função que plota vários gráficos automaticamente:
def plota_pivot_table(df, value, index, func, ylabel, xlabel, opcao='nada'):
    if opcao == 'nada':
        pd.pivot_table(df, values=value, index=index,
                       aggfunc=func).plot(figsize=[15, 5])
    elif opcao == 'sort':
        pd.pivot_table(df, values=value, index=index,
                       aggfunc=func).sort_values(value).plot(figsize=[15, 5])
    elif opcao == 'unstack':
        pd.pivot_table(df, values=value, index=index,
                       aggfunc=func).unstack().plot(figsize=[15, 5])
    plt.ylabel(ylabel)
    plt.xlabel(xlabel)
    return None


# IDEIA PARA AUTOMATIZAR MAIS O PROCESSO:

# Lista de DataFrames dos diferentes meses
MAR19 = pd.read_csv('SINASC_RO_2019_MAR.csv')
ABR19 = pd.read_csv('SINASC_RO_2019_ABR.csv')
MAI19 = pd.read_csv('SINASC_RO_2019_MAI.csv')
JUN19 = pd.read_csv('SINASC_RO_2019_JUN.csv')
DEZ19 = pd.read_csv('SINASC_RO_2019_DEZ.csv')
# Bastaria que colocasse o mês desejado Ex.: 
# JAN20= pd.read_csv('SINASC_RO_2020_JAN.csv')

meses = [MAR19, ABR19, MAI19, JUN19, DEZ19]  # ,JAN20 ]

# Loop cria a pasta  os DataFrames de cada mês
for mes in meses:
    max_data = mes.DTNASC.max()[:7]
    
    os.makedirs('./output/figs/'+max_data, exist_ok=True)
    
# FIM DA IDEIA/



# Plotando e salvando os gráficos desejados com a função 'plota_pivot_table' para cada mes:
    plota_pivot_table(mes, 'IDADEMAE', 'DTNASC', 'count', 'Quantidade de Nascimentos', 'Data de Nascimento')
    plt.savefig('./output/figs/'+max_data+'/quantidade_de_nascimento.png')

    plota_pivot_table(mes, 'IDADEMAE', ['DTNASC', 'SEXO'], 'mean', 'media idade mae','data de nascimento','unstack')
    plt.savefig('./output/figs/'+max_data+'/media idade mae por sexo.png')

    plota_pivot_table(mes, 'PESO', ['DTNASC', 'SEXO'], 'mean', 'media peso bebe','data de nascimento','unstack')
    plt.savefig('./output/figs/'+max_data+'/media peso bebe por sexo.png')

    plota_pivot_table(mes, 'PESO', 'ESCMAE', 'median', 'apgar1 medio','gestacao','sort')
    plt.savefig('./output/figs/'+max_data+'/media apgar1 por escolaridade mae.png')

    plota_pivot_table(mes, 'APGAR1', 'GESTACAO', 'mean', 'apgar1 medio','gestacao','sort')
    plt.savefig('./output/figs/'+max_data+'/media apgar1 por gestacao.png')

    plota_pivot_table(mes, 'APGAR5', 'GESTACAO', 'mean', 'apgar5 medio','gestacao','sort')
    plt.savefig('./output/figs/'+max_data+'/media apgar5 por gestacao.png')
