


valor = int( input("informe um valor"))


if (valor < 10 or valor > 100):
    print("valor invalido")
else:
    for contador in range(valor + 1):
        print(contador)
