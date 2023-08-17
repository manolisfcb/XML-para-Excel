from endereco import Endereco

emit =  {'CNPJ': '60409075055054',
     'xNome': 'NESTLE BRASIL LTDA',
     'xFant': 'NESTLE BRASIL LTDA',
     'enderEmit': {'xLgr': 'AV ARTHUR ANTONIO SENDAS',
                   'nro': 'SN',
                   'xBairro': 'PARQUE ANALANDIA',
                   'cMun': '3305109',
                   'xMun': 'Sao Joao de Meriti', 
                   'UF': 'RJ',
                   'CEP': '25585021',
                   'xPais': 'Brasil',
                   'fone': '08007777737'},
     'IE': '11931936', 
     'CRT': '3'}


class Entidad:
    def __init__(self, emit):
        self.tipo = 'CNPJ' if emit['CNPJ'] else 'CPF'
        self.identificacao = emit['CNPJ'] if emit['CNPJ'] else emit['CPF'] 
        self.nome = emit['xNome']
        self.fantasia = emit['xFant']
        self.inscricao_estadual = emit['IE']
        self.regime_tributario = emit['CRT']
        self.endereco = Endereco(emit['enderEmit'])
   
    def __repr__(self):
        return f'{self.nome} - {self.tipo}: {self.identificacao} \n{self.endereco}'

    
empresa = Entidad(emit)

print(empresa)