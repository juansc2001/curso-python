# a empresa solicita uma demanda para controle de transações bancarias, onde deverao ser 
# apresentadas as principais operações como saque, deposito,transferencia,entre contas

class banco:

    def __init__(self,saldo,cpf):#aqui eu defino os atributos da classe
        self.saldo = self.saldo
        self.cpf = 123
    
    def saque(self):

        if(saldo < 0):
            print("saldo insuficiente")
        else:
            valor_saque = input("quanto você deseja sacar?")
            if(valor_saque > self.saldo):
                print("saldo insuficiente")
            else:
                self.saldo -= self.saldo - valor_saque
                print("valor sacado")



juan_banco = banco(juan_banco,10,123)
