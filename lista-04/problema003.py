def traduzir(numero):

    if 0 <= numero <= 25:
        caractere = numero + 97

    elif 26 <= numero <= 49:
        caractere = numero + 71

    elif 50 <= numero <= 75:
        caractere = numero + 15

    elif 76 <= numero <= 99:
        caractere = numero - 11

    # espaço, quando numero for igual a 100
    else:
        caractere = 32

    letra = chr(caractere)

    return letra


entrada = input()

lista_numeros = entrada.split(' ')

no_string = False

for num in lista_numeros:

    if not(0 <= int(num) <= 100):
        print('Infelizmente os números nao dizem nada')
        no_string = True

if not no_string:

    string = ''

    for n in lista_numeros:
        string += traduzir(int(n))

    print(string)
