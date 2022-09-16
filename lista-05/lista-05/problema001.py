# funções
def soma_digitos(numero):

    resultado = 0
    digito = numero

    if 0 <= numero <= 9:
        digito = numero
        resultado += digito

    else:
        divisoes = 0

        while not(0 <= digito <= 9):

            digito = digito // 10
            divisoes += 1

        resultado += digito + soma_digitos(numero - (10**divisoes)*digito)

    resultado = int(resultado)

    return resultado


def mdc(termo1, termo2):

    resultado = 0

    # algoritmo de euclides
    if termo2 == 0:
        resultado = termo1

    else:
        if termo1 > termo2:
            termo2, termo1 = termo1, termo2

        if termo1 > 0:

            resto = termo2 % termo1
            termo2 = resto

        resultado = mdc(termo1, termo2)

    return resultado


# entradas
num1 = int(input())
num2 = int(input())
num3 = int(input())

# soma dos dígitos
soma1 = soma_digitos(num1)
soma2 = soma_digitos(num2)
soma3 = soma_digitos(num3)

# mdc
mdc_somas = mdc(mdc(soma1, soma2), soma3)

print(f'O MDC obtido é: {mdc_somas}')
