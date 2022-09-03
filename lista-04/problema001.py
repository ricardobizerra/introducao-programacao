# função que faz a operação
def operacao(lista, valor_m, valor_x):

    if valor_x == 1:
        valor_operacao = lista[0]

    else:

        # primeira operação
        if valor_m == 'S':
            valor_operacao = lista[0] + lista[1]

        elif valor_m == 'sub':
            valor_operacao = lista[0] - lista[1]

        elif valor_m == 'M':
            valor_operacao = lista[0] * lista[1]

        else:
            valor_operacao = lista[0] / lista[1]

        # loop para realizar operações a partir do primeiro resultado
        if valor_x > 2:

            if valor_m == 'S':

                for j in range(2, valor_x):
                    valor_operacao += lista[j]

            elif valor_m == 'sub':

                for j in range(2, valor_x):
                    valor_operacao -= lista[j]

            elif valor_m == 'M':

                for j in range(2, valor_x):
                    valor_operacao = valor_operacao * lista[j]

            else:

                for j in range(2, valor_x):

                    valor_operacao = valor_operacao / lista[j]

    return valor_operacao


# operação
nova_operacao = 1

while nova_operacao == 1:

    m = input()
    x = int(input())

    lista_operandos = []

    for i in range(x):
        operando = int(input())
        lista_operandos.append(operando)

    print(operacao(lista_operandos, m, x))

    nova_operacao = int(input())
