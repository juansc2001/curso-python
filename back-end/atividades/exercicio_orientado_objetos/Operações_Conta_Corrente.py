'''

Criar um projeto em Python que faça as operações de uma conta corrente (consulta, depositar, sacar e transferir). Deve possuir agência, número da conta corrente, nome do cliente e o saldo da conta.
Na operação de transferência,  o método deverá imprimir a mensagem "Transferência concluída" caso o cliente tenha saldo suficiente para fazer esta operação. Caso contrário, não permitir fazer a transferência.
O cliente só poderá sacar se o valor do saque for maior ou igual que ele possui na conta. Caso contrário, imprimir "Saldo insuficiente".
O depósito só poderá ser realizado caso o valor depositado for maior ou igual à 0 (zero).
O método Consultar retornará o saldo do momento da consulta.

'''


# Criar um projeto que faça as operações de uma conta corrente (consulta, depositar, sacar e transferir)

#  Deve possuir agência, número da conta corrente, nome do cliente e o saldo da conta.

#


class conta_corrente:

    def __init__(self,agencia,numero_conta_corrente,nome,saldo):
        self.agencia = agencia
        self.numero_conta_corrente = numero_conta_corrente
        self.nome = nome
        self.saldo = saldo
    

    def consultar(self):
        print(f"saldo atual de {self.saldo}")

    def depositar(self,valor):
        
        if(valor > 0):
            self.saldo += valor


    def sacar(self,valor):
        
        if(valor <= self.saldo):
            self.saldo -= valor
        else:
            print("Saldo insuficiente")

    def transferir(self,pagador,valor,recebedor):       

        if(self.saldo >= valor):
            recebedor.saldo += valor
            pagador.saldo -= valor
            
            print("Transferência concluída")
        else:
            print("Transferência não permitida")



juan_bank = conta_corrente('santander',123456,"juan_bank",200)
gustavo_bank = conta_corrente('santander',123456,"juan_bank",200)
ricardo = conta_corrente('itau',9373,'ricardo_bank',500)

gustavo_bank.consultar()
gustavo_bank.saldo

juan_bank.transferir(juan_bank,50,gustavo_bank)
juan_bank.transferir(juan_bank,150,ricardo)


gustavo_bank.consultar()
juan_bank.consultar()
