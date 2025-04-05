from processamento_dados import Dados
#Extract

path_json = 'data_raw/dados_empresaA.json'
path_csv = 'data_raw/dados_empresaB.csv'

dados_empresaA = Dados(path_json, 'json')
print(f'Nome colunas empresa A:{dados_empresaA.nomeColunas}')
print(f'Quantidade de linhas empresa A: {dados_empresaA.qtdLinhas}\n')

dados_empresaB = Dados(path_csv, 'csv')
print(f'Nome colunas empresa B:{dados_empresaB.nomeColunas}')
print(f'Quantidade de linhas empresa B: {dados_empresaB.qtdLinhas}\n')

#Transform

key_mapping = {'Nome do Item': 'Nome do Produto',
                'Classificação do Produto': 'Categoria do Produto',
                'Valor em Reais (R$)': 'Preço do Produto (R$)',
                'Quantidade em Estoque': 'Quantidade em Estoque',
                'Nome da Loja': 'Filial',
                'Data da Venda': 'Data da Venda'
                }

dados_empresaB.renomeiaColunas(key_mapping)
print(f'Nomes utilizados na fusão de dados:{dados_empresaB.nomeColunas}')

dadosFusao = Dados.combinaInfo(dados_empresaA, dados_empresaB)
print(f'Quantidade de registros após fusão de dados: {dadosFusao.qtdLinhas}')

#Load
path_salvar = 'data_processed/dados_combinados.csv'
dadosFusao.salvaDados(path_salvar)
print(f'\nNovo arquivo unificado foi gerado: {path_salvar}\nPara abrir segure ctrl e clique no caminho do arquivo')