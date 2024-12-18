numero_secreto = 20

#solicita o valor para o user
user_resposta = input("informe seu palpite: ")

#estrutura de decisao que decide se o usuario acertou ou não 
if(user_resposta == numero_secreto):
    print("parabens! você acertou")

elif(user_resposta > numero_secreto):
    print("você errou, seu palpite é maior que o numero secreto")

else:
    print("você errou, seu palpite é menor que o numero secreto")