# Exercício 2

#Agora edite o programa anterior para fazer com que, caso não exista o produto, o programa pergunte se o usuário quer cadastrar o produto

#Se ele responder sim, o programa deve pedir o nome do produto e a preco do produto e cadastrar no dicionário de preços

#Em seguida do cadastro bem sucedido, o programa deve printar o dicionário de precos atualizado





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



if(item_existe == False):#cadastra um novo produto caso tal não exista
    opçao_de_cadastro = input("você deseja cadastrar um novo produto? Y para sim N para nao")
    if(opçao_de_cadastro == "Y"):
        cadastrar_novo_produto = input("digite o nome do produto: ")
        valor_do_produto = input("digite o valor do produto: ")
        itens_preco[cadastrar_novo_produto] = valor_do_produto
        print("cadastro bem sucedido \n", list(itens_preco.items()))

    else:
        print("desligando sistema")

