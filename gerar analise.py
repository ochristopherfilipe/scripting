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

# mostrando o nome do script
print ('O nome do nosso script é', sys.argv[0])

# definindo o mes como o argumento do script de 'gerar script'
mes = sys.argv[1]
 
print('O mês de Referência é', mes)

# Definindo sinasc como a base de dados e definindo 'mes' como argumento
sinasc = pd.read_csv('SINASC_RO_2019_'+mes+'.csv')

# Criando uma pasta para salvar as figuras de saída com base na data máxima e visualizando o nome da pasta:
max_data = sinasc.DTNASC.max()[:7]

os.makedirs('./output/figs/'+max_data, exist_ok=True)


# Plotando e salvando os gráficos desejados com a função 'plota_pivot_table' para cada mes:
    plota_pivot_table(sinasc, 'IDADEMAE', 'DTNASC', 'count', 'Quantidade de Nascimentos', 'Data de Nascimento')
    plt.savefig('./output/figs/'+max_data+'/quantidade_de_nascimento.png')

    plota_pivot_table(sinasc, 'IDADEMAE', ['DTNASC', 'SEXO'], 'mean', 'media idade mae','data de nascimento','unstack')
    plt.savefig('./output/figs/'+max_data+'/media idade mae por sexo.png')

    plota_pivot_table(sinasc, 'PESO', ['DTNASC', 'SEXO'], 'mean', 'media peso bebe','data de nascimento','unstack')
    plt.savefig('./output/figs/'+max_data+'/media peso bebe por sexo.png')

    plota_pivot_table(sinasc, 'PESO', 'ESCMAE', 'median', 'apgar1 medio','gestacao','sort')
    plt.savefig('./output/figs/'+max_data+'/media apgar1 por escolaridade mae.png')

    plota_pivot_table(sinasc, 'APGAR1', 'GESTACAO', 'mean', 'apgar1 medio','gestacao','sort')
    plt.savefig('./output/figs/'+max_data+'/media apgar1 por gestacao.png')

    plota_pivot_table(sinasc, 'APGAR5', 'GESTACAO', 'mean', 'apgar5 medio','gestacao','sort')
    plt.savefig('./output/figs/'+max_data+'/media apgar5 por gestacao.png')
