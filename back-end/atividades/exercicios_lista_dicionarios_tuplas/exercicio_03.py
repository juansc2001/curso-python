#exercicio 03

#Crie um sistema de consulta de bônus dos funcionários

# Seu sistema deve:

# - Pegar o valor de vendas do funcinoário por meio de um input

#- Calcular o bônus do funcionário de acordo com a seguinte regra:

#- Se o funcionário vendeu mais de 1000 unidades, ele ganha R$2 de bonus para cada unidade vendida

# - Se o funcionário vendeu mais de 5000 unidades, ele ganha R$2 de bônus para cada unidade + um valor fixo de R$1000





#variavel responsavel por Pegar o valor de vendas do funcinoário
coleta_vendas_do_funcionario = ""


while(type(coleta_vendas_do_funcionario) != int):#trata os dados coletados do usurario 
    print("por favor coloque um numero")
    try:#tenta obter a resposta do usuario
        coleta_vendas_do_funcionario = int(input("quantas unidades o funcionario vendeu? "))
    except ValueError:
        print("resposta invalida")
    



unidades_vendidas = coleta_vendas_do_funcionario #variavel responsavel por guardar a quantidade de vendas do funcionario 
funcionario_bonus = 0 #variavel responsavel por coletar o bonus do funcionario

    
#calcula o bonus do funcionario
if(unidades_vendidas > 1000 and unidades_vendidas < 5001):
    funcionario_bonus = 2 * unidades_vendidas

elif(unidades_vendidas > 5000):
    funcionario_bonus =  (2 * unidades_vendidas) +1000



print(f"o funcionario tem {funcionario_bonus} de bonus")