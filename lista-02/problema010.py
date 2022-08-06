qtd_estrelas = int(input())

if qtd_estrelas <= 0:
    print('Isso está quebrado, acho que Howard pode me ajudar.')

elif 3 > qtd_estrelas > 0:
    print('Acho que bebi demais, eu juro que tinha mais estrelas!')

else:

    a = 1
    b = 2
    soma_dist = 0
    cont_nao_pertence = 0

    last_star_x = float(input())
    last_star_y = float(input())

    qtd_estrelas -= 1

    while qtd_estrelas != 0:

        # calculo da distancia

        star_x = float(input())
        star_y = float(input())

        dist = ((int(last_star_x) - int(star_x)) ** 2 + (int(last_star_y) - int(star_y)) ** 2) ** (1/2)

        print(f'Distância [star{a} <-> star{b}]: {int(dist)}')

        a += 1
        b += 1
        qtd_estrelas -= 1

        last_star_x = star_x
        last_star_y = star_y

        # verificando se faz parte de fibonacci

        verificacao_fibonacci = 0
        nao_pertence = False
        num_anterior = 0
        num_posterior = 1

        while int(dist) >= verificacao_fibonacci:

            if int(dist) == verificacao_fibonacci:
                nao_pertence = False
            else:
                nao_pertence = True

            verificacao_fibonacci = num_anterior + num_posterior

            num_anterior = num_posterior
            num_posterior = verificacao_fibonacci

        if nao_pertence:
            cont_nao_pertence += 1

        # fazendo a soma

        soma_dist += int(dist)

    # checando se a soma resulta num primo

    k = 1
    primo = False
    ocorrencia_primo = 0

    if soma_dist != 0 and soma_dist != 1:

        while k <= soma_dist:

            if soma_dist % k == 0:
                ocorrencia_primo += 1

            k += 1

        if ocorrencia_primo == 2:
            primo = True

        else:
            primo = False

    # condicionais de output

    if cont_nao_pertence == 0:
        if not primo:
            print('Yes! Eu consegui!')

        else:
            print('Oh my god! Eu vou ganhar o Nobel primeiro que Sheldon!')

    elif cont_nao_pertence == 1:
        print('Oh, não! Eu quase consegui!')

    elif cont_nao_pertence >= 2:
        if not primo:
            print('Eu vou acabar como o Stuart :/')

        else:
            print('Pelo menos o programa está funcionando...')
