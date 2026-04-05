import pandas as pd

# 1. Criando a função de lógica de negócio
def categorizar_etnia(etnia):
    if etnia == 'Branca':
        return 'brancas'
    elif etnia in ['Parda', 'Preta', 'Amarela', 'Indígena']:
        return 'não branca'
    else:
        return 'outras'

# 2. Aplicando a lógica ao DataFrame
# Criamos uma nova coluna 'ETNIA_CATEGORIA' baseada na coluna original
dados['ETNIA_CATEGORIA'] = dados['COR/RACA/ETNIA'].apply(categorizar_etnia)

# 3. Conferindo o resultado do novo agrupamento
print("Distribuição após o agrupamento:")
print(dados['ETNIA_CATEGORIA'].value_counts())