from pessoa import Pessoa

class Endereco(Pessoa):
    def __init__(self,nome, cpf, rg, nome_mae, nome_pai, 
                 estado, cidade, bairro, rua, logradouro):
        super().__init__(nome, cpf, rg, nome_mae, nome_pai)
        self._estado = estado
        self._cidade = cidade
        self._bairro = bairro
        self._rua = rua
        self._logradouro = logradouro
        
    def __str__(self):
        return f'Estado: {self._estado}\nCidade: {self._cidade}\nBairro: {self._bairro}\nRua: {self._rua}\nLogradouro: {self._logradouro}'
             
    @property
    def estado(self):
        return self._estado
        
    @property
    def cidade(self):
        return self._cidade
        
    @property
    def bairro(self):
        return self._bairro
        
    @property
    def rua(self):
        return self._rua
        
    @property
    def logradouro(self):
        return self._logradouro
        
    @estado.setter
    def estado(self, estado):
        self._estado = estado
        
    @cidade.setter
    def cidade(self, cidade):
        self._cidade = cidade
        
    @bairro.setter
    def bairro(self, bairro):
        self._bairro = bairro
        
    @rua.setter
    def rua(self, rua):
        self._rua = rua
        
    @logradouro.setter
    def logradouro(self, logradouro):
        self._logradouro = logradouro
        
