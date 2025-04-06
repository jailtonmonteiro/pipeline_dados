import json
import csv

class Dados:

    def __init__(self, dados):
        self.dados = dados
        self.nomeColunas = self.__getColumns()
        self.qtdLinhas = self.__sizeData()

    def __leituraJson(path):
        dados_json = []
        with open(path, 'r') as file:
            dados_json = json.load(file)
        return dados_json

    def __leituraCsv(path):
        dados_csv = []
        with open(path, 'r') as file:
            spamreader = csv.DictReader(file, delimiter=',')
            for row in spamreader:
                dados_csv.append(row)
        return dados_csv

    @classmethod
    def leituraDados(cls, path, tipoDados):
        dados = []

        if tipoDados == 'json':
            dados = cls.__leituraJson(path)
        elif tipoDados == 'csv':
            dados = cls.__leituraCsv(path)
        return cls(dados)
    
    def __getColumns(self):
        return list(self.dados[-1].keys())
    
    def renomeiaColunas(self, key_mapping):
        new_dados = []
        for old_dict in self.dados:
            dict_temp = {}
            for old_key, value in old_dict.items():
                dict_temp[key_mapping[old_key]] = value
            new_dados.append(dict_temp)
        
        self.dados = new_dados
        self.nomeColunas = self.__getColumns()

    def __sizeData(self):
        return len(self.dados)
    
    def combinaInfo(dadosA, dadosB):
        dadosUnidos = []
        dadosUnidos.extend(dadosA.dados)
        dadosUnidos.extend(dadosB.dados)

        return Dados(dadosUnidos)
    
    def transformaTabela(self):
        dadosCombinadosTabela = [self.nomeColunas]
        for row in self.dados:
            linha = []
            for coluna in self.nomeColunas:
                linha.append(row.get(coluna, 'Indisponivel'))
            dadosCombinadosTabela.append(linha)
        return dadosCombinadosTabela
    

    def salvaDados(self, path):

        dadosCombinadosTabela = self.transformaTabela()

        with open(path, 'w') as file:
            writer = csv.writer(file)
            writer.writerows(dadosCombinadosTabela)