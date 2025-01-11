#Faça um programa que use a função valorPagamento para determinar o valor a ser pago por uma prestação de uma conta.
#O programa deverá solicitar ao usuário o valor da prestação e o número de dias em atraso e passar estes valores para a função valorPagamento,
#que calculará o valor a ser pago e devolverá este valor ao programa que a chamou. O programa deverá então exibir o valor a ser pago na tela.
#Após a execução o programa deverá voltar a pedir outro valor de prestação e assim continuar até que seja informado um valor igual a zero para
#a prestação. Neste momento o programa deverá ser encerrado, exibindo o relatório do dia, que conterá a quantidade e o valor total de prestações
#pagas no dia. O cálculo do valor a ser pago é feito da seguinte forma. Para pagamentos sem atraso, cobrar o valor da prestação. Quando houver atraso,
#cobrar 3% de multa, mais 0,1% de juros por dia de atraso.





# 1- função valorPagamento para determinar o valor a ser pago por uma prestação de uma conta

# 2- solicitar ao usuário o valor da prestação e o número de dias em atraso e passar estes valores para a função valorPagamento

# 3- função calculará o valor a ser pago e devolverá este valor ao programa que a chamou

# 4- O programa deverá então exibir o valor a ser pago na tela

# 5- Após a execução o programa deverá voltar a pedir outro valor de prestação

# 6- até que seja informado um valor igual a zero para
#a prestação. Neste momento o programa deverá ser encerrado, exibindo o relatório do dia

# 7- relatorio deve conter a quantidade e o valor total de prestações
#pagas no dia.

# 8- 0 calculo deve ser feito da seguinte forma: Para pagamentos sem atraso, cobrar o valor da prestação. Quando houver atraso,
#cobrar 3% de multa, mais 0,1% de juros por dia de atraso.



def valor_pagamento(valor_prestacao, dias_atrasados): #

    multa = dias_atrasados/1000
    

    if(dias_atrasados <= 0):
        pagar_valor = valor_prestacao

    elif(dias_atrasados > 0):
        pagar_valor += valor_prestacao * (0.03 + multa)
    
    return pagar_valor



get_valor_prestacao = input("valor da prestação: ")
get_dias_atrasados = input("quantos dias de atraso: ")


valor_pagamento(get_valor_prestacao,get_dias_atrasados)