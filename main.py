from pessoa import Pessoa
from endereco import Endereco
from conta import Conta

norton = Pessoa("Norton Silva Junior", '859.259.858-96', '85.596.698-5', 'Maria Joaquina', 'Norton Silva')
endereco = Endereco(norton.nome, norton.cpf, norton.rg, norton.nome_mae, norton.nome_pai, 
                    'SP', 'São Paulo', 'Paulista', 'Paulista', 3200)
conta = Conta(norton.nome, norton.cpf, norton.rg, norton.nome_mae, norton.nome_pai,
               endereco.estado, endereco.cidade, endereco.bairro, endereco.rua, endereco.logradouro, 
              '8459875-1', 0.0)

conta.extrato()
conta.depositar(800)
conta.extrato()
conta.depositar(200)
conta.extrato()
conta.sacar(1101.0)
conta.extrato()
conta.depositar(5000.0)
conta.extrato()
conta.depositar(5000.1)
conta.extrato()
