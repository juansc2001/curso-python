class banco:  # Definição da classe
    def __init__(self, saldo, cpf):  # Construtor que inicializa os atributos
        self.saldo = saldo  # Atributo 'saldo' recebe o valor passado
        self.cpf = cpf      # Atributo 'cpf' recebe o valor passado

    def saque(self, valor_saque):  # Método para realizar saque
        if valor_saque > self.saldo:  # Verifica se o saldo é suficiente
            print("saldo insuficiente")
        else:
            print(f"{valor_saque} sacado")  # Mostra o valor sacado



banco_do_juan = banco(100, 123)  # Criação do objeto (uma conta bancária com saldo 100 e CPF 123)
banco_do_juan.saque(100)  # Realiza o saque de 100


