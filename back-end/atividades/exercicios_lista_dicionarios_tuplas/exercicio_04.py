
# # Exercício 3
# '''
# Dada a lista de preços de produtos, uma loja resolveu fazer um reajuste nos preços dos produtos.
# calcule o novo valor dos produtos com base nas seguintes regras:
# Preços até 1.000 vão ter um reajuste de 10% (ou seja, o novo preço será 110% do preço atual)
# Preços até maiores que 1.000 até 2.000 vão ter reajuste de 15%
# Preços acima de 2.000 vão ter reajuste de 20%
# precos = {"celular": 1500, "camera": 1000, "fone de ouvido": 800, "monitor": 3000}
# '''



precos = {"celular": 1500, "camera": 1000, "fone de ouvido": 800, "monitor": 3000}

lista_mercadorias = list(precos.keys())#guarda na variavel lista_mercados, cada key do dicionario 

print(f"dicionario desatualizado {precos.items()} \n \n")

for itens in lista_mercadorias:#faz o reajuste de preço de cada item do dicionario 
    
    valor = int(precos[itens])#guarda o preço de cada item do dicionario
    
    
    if(valor <= 1000):
        #vão ter um reajuste de 10% (ou seja, o novo preço será 110% do preço atual)
        valor_atualizado = valor + (1000 * 0.10)
        precos[itens] = valor_atualizado
    
    elif(valor > 1000 and valor <= 2000):
        #vão ter reajuste de 15%
        valor_atualizado = valor + (1000 * 0.15)
        precos[itens] = valor_atualizado


    elif(valor > 2000):
        #vão ter reajuste de 20%
        valor_atualizado = valor + (1000 * 0.20)
        precos[itens] = valor_atualizado


print(precos.items())

