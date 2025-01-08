# Exercício 2

# Crie um sistema de consulta de preços

# Seu sistema deve:

# - Pedir para o usuário o nome de um produto

#- Caso o produto exista na lista de produtos, o programa deve retornar o preço do produto como resposta

# Ex: O produto celular custa R$1500

# - Caso o produto não exista na lista de produtos, o programa deve printar uma mensagem para o usuário tentar novamente



itens_preco = {"bola":3, "xadrez":30, "carrinho": 15} #dicionario que guarda o preço dos itens 

#coleta o nome do produto que ira ser consultado 
consultar_item = input("digite o nome do produto para saber seu preço: ")

lista_de_itens = list(itens_preco.keys()) #guarda todos os itens do dicionario em uma lista



#verifica se o item consultado existe no dicionario 
for item in lista_de_itens:

    item_existe = False #guarda o valor se o item existe no dicionario 
    if(item == consultar_item):
        item_existe = True
        break



if(item_existe == True):#caso o item esteja no dicionario imprime o preço
    print(f"o produto {consultar_item} custa R${itens_preco[consultar_item]}")
else:
    print("o usuario deve tentar novamente mais tarde")#o item pesquisado não existe no dicionario de itens 







#geito que eu considero errado de resolver o exercicio, mais que é implementado de forma simples 
''' 

itens_preco = {"bola":3, "xadrez":30} #dicionario que guarda o preço dos itens 

#coleta o nome do produto que ira ser consultado 
consultar_item = input("digite o nome do produto para saber seu preço: ")


try:#tenta verificar o preço do produto no dicionario 
    print(f"o produlto {consultar_item} custa R${itens_preco[consultar_item]}")

except KeyError:#protudo não existe no dicionario
    print("o usuario deve tentar novamente.") 


'''