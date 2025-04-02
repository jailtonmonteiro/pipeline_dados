# Leitura de dados -------------------------------------------------------------------------
def leituraJson(path_json):
    import json
    dados_json = []
    with open(path_json, 'r') as file:
        dados_json = json.load(file)
    return dados_json

def leituraCsv(path_csv):
    import csv
    dados_csv = []
    with open(path_csv, 'r') as file:
        spamreader = csv.DictReader(file, delimiter=',')
        for row in spamreader:
            dados_csv.append(row)
    return dados_csv

def leituraDados(path, tipoArquivo):
    dados = []

    if tipoArquivo == 'json':
        dados = leituraJson(path)
    elif tipoArquivo == 'csv':
        dados = leituraCsv(path)
    return dados

# Transformação dos Dados ------------------------------------------------------------------
def getColumns(dados):
    return list(dadosCsv[0].keys())


def renomeiaColunas(dados, key_mapping):
    new_dados_csv = []
    for old_dict in dados:
        dict_temp = {}
        for old_key, value in old_dict.items():
            dict_temp[key_mapping[old_key]] = value
        new_dados_csv.append(dict_temp)
    return new_dados_csv

# Unindo dados -----------------------------------------------------------------------------
def combinaInfo(dadoJson, new_dados_csv):
    combined_list = []
    combined_list.extend(dadoJson)
    combined_list.extend(new_dados_csv)
    
    return combined_list


# Preechendo campos indisponiveis ------------------------------------------------------------

def prencheNull(combined_list):
    nome_colunas = list(combined_list[-1].keys())
    dados_combinados_tabela = [nome_colunas]
    for row in combined_list:
        linha = []
        for coluna in nome_colunas:
            linha.append(row.get(coluna, 'Indisponivel'))
        dados_combinados_tabela.append(linha)
    return dados_combinados_tabela

def salvaDados(path):
    import csv
    with open(path_dados_combinados, 'w') as file:
        writer = csv.writer(file)
        writer.writerows(dados_combinados_tabela)


path_json = 'data_raw/dados_empresaA.json'
path_csv = 'data_raw/dados_empresaB.csv'


# Leitura de dados -------------------------------------------------------------------------
dadosCsv = leituraDados(path_csv, 'csv')
dadosJson = leituraDados(path_json, 'json')

print(f'Primeiro item dados CSV: {dadosCsv[0]}')
print(f'Primeiro item dados Json: {dadosJson[0]}')

# Transformação dos Dados ------------------------------------------------------------------
key_mapping = {'Nome do Item': 'Nome do Produto',
               'Classificação do Produto': 'Categoria do Produto',
               'Valor em Reais (R$)': 'Preço do Produto (R$)',
               'Quantidade em Estoque': 'Quantidade em Estoque',
               'Nome da Loja': 'Filial',
               'Data da Venda': 'Data da Venda'
               }

dadosCsv = renomeiaColunas(dadosCsv, key_mapping)
nomeColunasCsv = getColumns(dadosCsv)

# Unindo dados -----------------------------------------------------------------------------

listaCombinada = combinaInfo(dadosJson, dadosCsv)
dados_combinados_tabela = prencheNull(listaCombinada)


# Salvando de dados -------------------------------------------------------------------------

path_dados_combinados = 'data_processed/dados_combinados_mai.csv'
salvaDados(path_dados_combinados)