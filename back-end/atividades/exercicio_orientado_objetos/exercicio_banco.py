#Exercício POO
'''
A empresa solicita uma demanda para o controle de transações bancárias, onde deverão ser apresentadas as principais operações como saque, depósito, transferência, entre contas
'''


class banco :

    def __init__(self,cpf,saldo = 0):

        self.cpf = cpf
        self.saldo = saldo
    

    def saque(self,sacando):
        
        if(self.saldo < sacando):
            print("saldo insuficiente")
            print(f"saldo atual de {self.saldo}")
        else:
            self.saldo -= sacando
            print("saque efetuado")
            print(f"saldo atual de {self.saldo}")



    def deposito(self,valor_depositado):
        self.saldo += valor_depositado
        print(f"valor depositado, saldo atual de {self.saldo}")        

    def transferencia(self,valor_transferencia):

        self.saldo -= valor_transferencia
        print("transferencia realizada")
        print(f"saldo atual de {self.saldo}")

        return valor_transferencia


juan_banco = banco(123,100)


juan_banco.saque(5)

juan_banco.deposito(50)

juan_banco.transferencia(40)
        
    
    