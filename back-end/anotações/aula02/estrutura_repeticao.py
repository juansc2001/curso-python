"""
o que é uma estrutura de repetição?
    é algo que acontece rotineiramente, ou seja, algo que se repete

"""
#cuidado ao usar o while, pois podemos gerar um loop infinito
#para controlar o while utilizamos um contador
print("repetição com while(equanto)")

contador = 0

#repete 10 vezes 
while(contador <= 10):
    print(f"volta ao mundo {contador}")
    contador += 1

print(15*"-")


print("for - lista")


#cria uma lista
caixa_fruta = ["maça","Banana", "pera"]

for fruta in caixa_fruta:
    print(f"a fruta é: {fruta}")



print(15*"-")

print("for - simples")

#conta de 0 a 9
for contar_loops in range(0,10):
    print(f"contagem {contar_loops}")


for i in range(10):
    if i == 5:
        break  # Interrompe o laço quando i é 5
    if i % 2 == 0:
        continue  # Pula os números pares
    print("Número impar:", i)
