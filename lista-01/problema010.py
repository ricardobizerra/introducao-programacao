nome_1 = input()
pontos_1 = int(input())
nome_2 = input()
pontos_2 = int(input())
nome_3 = input()
pontos_3 = int(input())

pontos_primeiro = 0
nome_primeiro = ''
pontos_segundo = 0
nome_segundo = ''
pontos_terceiro = 0
nome_terceiro = ''

if (pontos_1 < pontos_2) and (pontos_1 < pontos_3):

    pontos_primeiro = pontos_1
    nome_primeiro = nome_1

    if pontos_2 < pontos_3:
        pontos_segundo = pontos_2
        nome_segundo = nome_2
        pontos_terceiro = pontos_3
        nome_terceiro = nome_3

    elif pontos_3 < pontos_2:
        pontos_segundo = pontos_3
        nome_segundo = nome_3
        pontos_terceiro = pontos_2
        nome_terceiro = nome_2

    else:

        if nome_2 < nome_3:
            pontos_segundo = pontos_2
            nome_segundo = nome_2

            pontos_terceiro = pontos_3
            nome_terceiro = nome_3

        else:
            pontos_segundo = pontos_3
            nome_segundo = nome_3

            pontos_terceiro = pontos_2
            nome_terceiro = nome_2

elif pontos_2 < pontos_3:

    pontos_primeiro = pontos_2
    nome_primeiro = nome_2

    if pontos_1 < pontos_3:

        pontos_segundo = pontos_1
        nome_segundo = nome_1

        pontos_terceiro = pontos_3
        nome_terceiro = nome_3

    elif pontos_3 < pontos_1:

        pontos_segundo = pontos_3
        nome_segundo = nome_3

        pontos_terceiro = pontos_1
        nome_terceiro = nome_1

    else:

        if nome_1 < nome_3:

            pontos_segundo = pontos_1
            nome_segundo = nome_1

            pontos_terceiro = pontos_3
            nome_terceiro = nome_3

        else:

            pontos_segundo = pontos_3
            nome_segundo = nome_3

            pontos_terceiro = pontos_1
            nome_terceiro = nome_1

elif pontos_3 < pontos_2:

    pontos_primeiro = pontos_3
    nome_primeiro = nome_3

    if pontos_1 < pontos_2:

        pontos_segundo = pontos_1
        nome_segundo = nome_1

        pontos_terceiro = pontos_2
        nome_terceiro = nome_2

    elif pontos_2 < pontos_1:

        pontos_segundo = pontos_2
        nome_segundo = nome_2

        pontos_terceiro = pontos_1
        nome_terceiro = nome_1

    else:

        if nome_1 < nome_2:

            pontos_segundo = pontos_1
            nome_segundo = nome_1

            pontos_terceiro = pontos_2
            nome_terceiro = nome_2

        else:

            pontos_segundo = pontos_2
            nome_segundo = nome_2

            pontos_terceiro = pontos_1
            nome_terceiro = nome_1

if pontos_3 > pontos_1 == pontos_2 < pontos_3:

    if nome_1 < nome_2:

        pontos_primeiro = pontos_1
        nome_primeiro = nome_1

        pontos_segundo = pontos_2
        nome_segundo = nome_2

    else:

        pontos_primeiro = pontos_2
        nome_primeiro = nome_2

        pontos_segundo = pontos_1
        nome_segundo = nome_1

    pontos_terceiro = pontos_3
    nome_terceiro = nome_3

if pontos_2 > pontos_1 == pontos_3 < pontos_2:

    if nome_1 < nome_3:

        pontos_primeiro = pontos_1
        nome_primeiro = nome_1

        pontos_segundo = pontos_3
        nome_segundo = nome_3

    else:

        pontos_primeiro = pontos_3
        nome_primeiro = nome_3

        pontos_segundo = pontos_1
        nome_segundo = nome_1

    pontos_terceiro = pontos_2
    nome_terceiro = nome_2

if pontos_1 > pontos_2 == pontos_3 < pontos_1:

    if nome_2 < nome_3:

        pontos_primeiro = pontos_2
        nome_primeiro = nome_2

        pontos_segundo = pontos_3
        nome_segundo = nome_3

    else:

        pontos_primeiro = pontos_3
        nome_primeiro = nome_3

        pontos_segundo = pontos_2
        nome_segundo = nome_2

    pontos_terceiro = pontos_1
    nome_terceiro = nome_1

if pontos_1 == pontos_2 == pontos_3:

    if (nome_1 < nome_2) and (nome_1 < nome_3):

        pontos_primeiro = pontos_1
        nome_primeiro = nome_1

        if nome_2 < nome_3:

            pontos_segundo = pontos_2
            nome_segundo = nome_2

            pontos_terceiro = pontos_3
            nome_terceiro = nome_3

        else:

            pontos_segundo = pontos_3
            nome_segundo = nome_3

            pontos_terceiro = pontos_2
            nome_terceiro = nome_2

    elif nome_2 < nome_3:

        pontos_primeiro = pontos_2
        nome_primeiro = nome_2

        if nome_1 < nome_3:

            pontos_segundo = pontos_1
            nome_segundo = nome_1

            pontos_terceiro = pontos_3
            nome_terceiro = nome_3

        else:

            pontos_segundo = pontos_3
            nome_segundo = nome_3

            pontos_terceiro = pontos_1
            nome_terceiro = nome_1

    else:

        pontos_primeiro = pontos_3
        nome_primeiro = nome_3

        if nome_1 < nome_2:

            pontos_segundo = pontos_1
            nome_segundo = nome_1

            pontos_terceiro = pontos_2
            nome_terceiro = nome_2

        else:

            pontos_segundo = pontos_2
            nome_segundo = nome_2

            pontos_terceiro = pontos_1
            nome_terceiro = nome_1

print(f'{nome_primeiro} {pontos_primeiro}')

print(f'{nome_segundo} {pontos_segundo}')

print(f'{nome_terceiro} {pontos_terceiro}')
