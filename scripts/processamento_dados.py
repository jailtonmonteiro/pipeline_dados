import json
import csv

class Dados:

    def __init__(self, path, tipoDados):
        self.__path = path
        self.__tipoDados = tipoDados
        self.dados = self.__leituraDados()
        self.nomeColunas = self.__getColumns()
        self.qtdLinhas = self.__sizeData()

    def __leituraJson(self):
        dados_json = []
        with open(self.__path, 'r') as file:
            dados_json = json.load(file)
        return dados_json

    def __leituraCsv(self):
        dados_csv = []
        with open(self.__path, 'r') as file:
            spamreader = csv.DictReader(file, delimiter=',')
            for row in spamreader:
                dados_csv.append(row)
        return dados_csv

    def __leituraDados(self):
        dados = []

        if self.__tipoDados == 'json':
            dados = self.__leituraJson()
        elif self.__tipoDados == 'csv':
            dados = self.__leituraCsv()
        elif self.__tipoDados == 'list':
            dados = self.__path
            self.__path = 'Lista em memória'
        return dados
    
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

        return Dados(dadosUnidos, 'list')
    
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