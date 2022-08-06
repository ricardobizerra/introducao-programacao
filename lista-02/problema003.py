desejado = int(input())

soma = 0
progresso = 1

while progresso > 0:
    progresso = int(input())

    while progresso == 0:
        progresso = int(input())

    for i in range(1, progresso + 1):
        soma += i

if soma < desejado:
    print('Ainda falta um pouco...')

elif soma == desejado:
    print('Parabéns!!! Você é o mais inteligente')

elif soma > desejado:

    if soma < 20*desejado:
        print('Parece que o gêniozinho passou um pouco do local...')

    elif 20*desejado <= soma <= 100*desejado:
        print('Acho que sua grande inteligência fez você se perder um pouco no caminho, onde estamos?')

    else:
        print('Hum... acho que o gêniozinho não tem mesmo doutorado ein...')
