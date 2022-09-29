class Pessoa:
    def __init__(self, nome, cpf, rg, nome_mae, nome_pai):
        self._nome = nome
        self._cpf = cpf
        self._rg = rg
        self._nome_mae = nome_mae 
        self._nome_pai = nome_pai
        
    def __str__(self):
        return f'Nome: {self._nome}\nCPF: {self._cpf}\nRG: {self._rg}\nNome da mãe: {self._nome_mae}\nNome do pai: {self._nome_pai}'

    @property
    def nome(self):
        return self._nome.title()
    
    @property
    def cpf(self):
        return self._cpf
    
    @property
    def rg(self):
        return self._rg
    
    @property
    def nome_mae(self):
        return self._nome_mae.title()
    
    @property
    def nome_pai(self):
        return self._nome_pai.title()
