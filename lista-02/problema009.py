# iniciando variaveis
acertos = 0
erros = 0

# numero de conversoes
n = int(input())

for i in range(0, n):

    resultado = ''
    soma = 0
    k = 0

    operacao = input()

    if operacao == 'DEC':
        valor_inicial = input()
        valor_inicial = int(valor_inicial)
        valor_inicial = str(valor_inicial)

        palpite = int(input())

        cont = len(valor_inicial) - 1

        for k in valor_inicial:
            soma += int(k) * (2**cont)
            cont -= 1

        if palpite != soma:
            erros += 1
            print(f'Palpite Incorreto, o valor {valor_inicial} = {soma}')
        else:
            acertos += 1

    elif operacao == 'BIN':
        valor_inicial = int(input())

        palpite = input()
        palpite = int(palpite)
        palpite = str(palpite)

        quociente = valor_inicial

        if valor_inicial == 0 or valor_inicial == 1:
            resultado = valor_inicial
            resultado = str(resultado)

        else:
            while quociente != 1:
                resto = quociente % 2
                quociente = quociente // 2

                if quociente != 1:
                    resultado = str(resto) + resultado

                elif quociente == 1:
                    resultado = str(quociente) + str(resto) + resultado

        if palpite != resultado:
            erros += 1
            print(f'Palpite Incorreto, o valor {valor_inicial} = {resultado}')
        else:
            acertos += 1

if acertos > (0.5 * (acertos + erros)):
    print('Bazinga! Quem realizou esses cálculos foi o computador??')
else:
    print('Parece que realizar conversões em binário não é o seu forte')
