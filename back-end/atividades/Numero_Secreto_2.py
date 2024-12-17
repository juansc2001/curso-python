"""
escolher numero 

pegar do usuario 

decidir de ele acertou o numero 


1quantidade de vezes que o usuario pode tentar (

escolha a dificuldade que o jogador quer

entre os 3 facil mediu e dificil 


guardar o nivel que o jogador escolheu 





)

marcar os pontos do jogador 

mudar a pontuação de acordo com os niveis 







informar o jogador quantos pontos ele tem

informar o jogador quantas tentativas ainda restam 
"""
pontos_inicio_jogador = 100

numero_sorteado = 50

numero_usuario = int( input("escolha um numero: ") )

dificuldade = input("escolha uma dificuldade: facil, normal ou dificil")

if(dificuldade == "facil"):
    print("você tem 30 tentativas")
    tentativas = 30
    pontos_jogador = -10

elif(dificuldade == "normal"):
    print("você tem 15 tentativas")
    tentativas = 15
    pontos_jogador = -20


elif(dificuldade == "dificil"):
    print("você tem 5 tentativas")
    tentativas = 5
    pontos_jogador = -50  






#verifica se o usuario acertou ou não 
if(numero_sorteado == numero_usuario):
    print(f"você acertou, sua pontuação total é de {pontos_inicio_jogador}")

elif(numero_sorteado >= numero_usuario):
    print(f"você errou, o numero escolhido é maior, sua pontuação atual é de {tentativas}")
    
    #subitrair ponto_inicio_jogador pelo pontos_jogador 
    #subitrair tentativas que o jogador pelo pontos_jogador 

    print(f"você tem {pontos_jogador} pontos")

elif(numero_sorteado <= numero_usuario):
    print(f"você errou, o numero escolhido é menor, sua pontuação atual é de {tentativas}")

    #subitrair ponto_inicio_jogador pelo pontos_jogador

else:
    print("comando invalido!")
