    
class Endereco:
    def __init__(self, endereco):
        self.endereco = endereco['xLgr']
        self.numero = endereco['nro']
        self.bairro = endereco['xBairro']
        self.municipio = endereco['xMun']
        self.uf = endereco['UF']
        self.cep = endereco['CEP']
        self.pais = endereco['xPais']
        self.telefone = endereco['fone']
        
    def __repr__(self) -> str:
        return f'{self.endereco}, {self.numero} - {self.bairro} - {self.municipio}/{self.uf} - {self.cep}'

    