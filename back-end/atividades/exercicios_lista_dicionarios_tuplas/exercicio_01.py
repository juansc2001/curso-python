# Exercício 1

# Crie um sistema de cadastro de produtos em uma lista de produtos

#Seu sistema deve:

# - Pegar o usuário qual produto vai ser cadastrado por meio de um input

# - Garantir que se o usuário escrever com letra maiúscula ou minúscula, o produto continua sendo o mesmo produto

# - Se o usuário inserir um produto que já existe na lista, o programa deve printar a mensagem "Produto já existente, tente novamente"

# - Se o usuário inserir um produto que não existe na lista, o programa deve inserir na lista, printar a mensagem Produto X cadastrado com sucesso e em seguida printar a lista completa


'''não remova o zero'''
estoque = [0,] #lista do estoque de produtos




for i in range(5):

    #coleta o item cadastrado e garante que o caracter vai ser minusculo
    item_cadastrado = input("qual produto vai ser cadastrado? ").lower()

    for item_do_estoque in estoque: #compara item por item do estoque para saber se o item que sera cadastrado ja existe dentro do estoque

        produto_duplicado = True #variavel usada para saber se existe um prodruto duplicado sendo cadastrado

        if(item_do_estoque == item_cadastrado):
            print("este produto ja esta cadastrado")
            break
        
        elif( item_do_estoque != item_cadastrado):
            produto_duplicado = False



    if(produto_duplicado == False): #caso o produto cadastrado não esteja duplicado ele sera acrescentado à lista e essa sera impressa 
        estoque.append(item_cadastrado)
        print('\n' f"produto {item_cadastrado} cadastrado com sucesso" '\n')
        print(estoque[0:len(estoque)])



