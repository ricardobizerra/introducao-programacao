# inicializando variáveis
fim = False
pegou_cracha = False
ajeitando_cracha = False
rodada = 1
vezes_pegou_cracha = 0
virou_zumbi = False
chegou_na_porta = False

# inputs
voce_y = int(input())
voce_x = int(input())
zumbi_y = int(input())
zumbi_x = int(input())
cracha_y = int(input())
cracha_x = int(input())
porta_y = int(input())
porta_x = int(input())

# matriz do cin
cin = []

for i in range(0, 6):

    cin.append([])

    for j in range(0, 6):

        cin[i].append('-')

# jogo rodando

while not fim:

    # condicoes de finalização
    if zumbi_x == voce_x and zumbi_y == voce_y:
        fim = True
        virou_zumbi = True

    elif porta_x == voce_x and porta_y == voce_y:
        fim = True
        chegou_na_porta = True

    # mostrando onde cada um esta na matriz
    for i in range(0, 6):

        for j in range(0, 6):

            cin[i][j] = '-'

    # definindo onde vc, zumbi, crachá e porta estão
    cin[zumbi_y][zumbi_x] = 'Z'

    if not(zumbi_y == voce_y and zumbi_x == voce_x):
        cin[voce_y][voce_x] = 'V'

    if not (zumbi_y == cracha_y and zumbi_x == cracha_x) and not(voce_y == cracha_y and voce_x == cracha_x) and not pegou_cracha:
        cin[cracha_y][cracha_x] = 'C'

    if not (zumbi_y == porta_y and zumbi_x == porta_x) and not (voce_y == porta_y and voce_x == porta_x):
        cin[porta_y][porta_x] = 'P'

    # output por rodada
    if rodada != 1:

        # printando matriz
        for linha in cin:

            string_linha = ''

            for k in range(0, 6):

                if k == 5:
                    string_linha = string_linha + linha[k]

                else:
                    string_linha = string_linha + linha[k] + ' '

            print(string_linha)

        # condicional para nao mostrar essas frases ao final do programa
        if not fim:

            # outputs do crachá
            if ajeitando_cracha:
                print('Finalmente! Peguei o crachá')

            elif pegou_cracha and not ajeitando_cracha:
                print('Já peguei o crachá')

            elif not pegou_cracha:
                print('Ainda não achei o crachá')

            # distancia
            dist = ((voce_x - zumbi_x) ** 2 + (voce_y - zumbi_y) ** 2) ** (1 / 2)

            if int(dist) <= 3:
                print('Preciso acelerar, o zumbi tá na minha cola!')

            elif 3 < int(dist) <= 4:
                print('Consigo ver la longe o zumbi, mas é melhor acelerar!')

            elif int(dist) > 4:
                print('O zumbi está longe, mas não posso ficar parado')

            print()

    # condicionais de movimentação do zumbi
    if zumbi_x == voce_x:

        if zumbi_y > voce_y:
            zumbi_y -= 1

        elif zumbi_y < voce_y:
            zumbi_y += 1

    elif zumbi_x > voce_x:
        zumbi_x -= 1

    else:
        zumbi_x += 1

    # condicionais de movimentação de voce
    if not(zumbi_x == voce_x and zumbi_y == voce_y):

        if not pegou_cracha:

            if cracha_x == voce_x:

                if voce_y > cracha_y:
                    voce_y -= 1

                elif voce_y < cracha_y:
                    voce_y += 1

            elif voce_x > cracha_x:
                voce_x -= 1

            else:
                voce_x += 1

        elif not ajeitando_cracha:

            if porta_x == voce_x:

                if voce_y > porta_y:
                    voce_y -= 1

                elif voce_y < porta_y:
                    voce_y += 1

            elif voce_x > porta_x:
                voce_x -= 1

            else:
                voce_x += 1

    # verificando se o cracha foi pego e se está dentro da margem de 1 rodada sem mover
    if cracha_x == voce_x and cracha_y == voce_y:
        pegou_cracha = True

        ajeitando_cracha = True

        vezes_pegou_cracha += 1

        if ajeitando_cracha and vezes_pegou_cracha != 1:
            ajeitando_cracha = False

    rodada += 1

# outputs finais
if chegou_na_porta:
    print('Consegui achar a porta, agora é so passar na catraca e vazar daqui!')

elif virou_zumbi:
    print('Ferrou, agora vou virar um zumbi')
