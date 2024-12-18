"""
estruturas de decisao

classificação
    >simples
    >composta
    >encadeada
    >aninhadas

operadores:
    == (igual a)
    != (diferente de)
    < (menor que)
    > (mair que)
    <= (menor igual a)
    >= (maior igual a)

"""

print("simples - é dada por uma unica decisão")

idade = 18

if (idade >= 18):{
    print("maior de idade")
}

#repete o traço 20x
print(20*"-")

print("composta - é dada por uma unica decisao e uma resposta padrao")

if (idade >= 18):
    print("maior de idade")
else:
    print("menor de idade")


#repete o traço 20x
print(20*"-")

print("encadeada- é dada por mais de uma decisão em uma resposta padrão")

if (idade >= 18):
    print("maior de idade")

elif(idade <= 18):
    print("menor de idade")
    
else:
    print("você é extraterrestre, bem vindo XD")


#repete o traço 20x
print(20*"-")

print("aninhada - possui uma estrutura de decisao dentro da outra")

classificacao = 16
ingresso = False 

if classificacao >= 16:
    if ingresso == True:
        print("você pode assistir ao filme")
    else:
        print("você nao pode assistir ao filme")
else:
    print("você não pode assistir ao filme")

