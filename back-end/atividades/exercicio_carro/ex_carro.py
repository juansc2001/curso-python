
class Carro:

    def __init__(self,modelo,ano,marca,cor):
        
        self.modelo = modelo
        self.ano = ano
        self.marca = marca
        self.cor = cor

    def imprecao_data(self):
        lista_carros = f" modelo: {self.modelo} ano: {self.ano} marca: {self.marca} cor: {self.cor}"
        
        return lista_carros



lista_de_carros = []

for i in range(2):
    modelo =input("qual é o modelo do carro: ")
    ano = input("qual é o ano do carro: ")
    marca = input("qual é a marca do carro: ")
    cor = input("qual é a cor do carro: ")

    carro = Carro(modelo,ano,marca,cor)
    lista_de_carros.append(carro.imprecao_data())


print(lista_de_carros)



