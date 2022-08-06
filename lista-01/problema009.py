nome_da_quadrilha = input()
passo_1 = input()
passo_2 = input()
passo_3 = input()
passo_4 = input()
passo_5 = input()

if (
        passo_1 == 'Cumprimento' or passo_1 == 'Balancê' or passo_1 == 'Passeio' or passo_1 == 'Túnel' or passo_1 == 'Serrote' or passo_1 == 'Casamento' or passo_1 == 'Despedida') and (
        passo_2 == 'Cumprimento' or passo_2 == 'Balancê' or passo_2 == 'Passeio' or passo_2 == 'Túnel' or passo_2 == 'Serrote' or passo_2 == 'Casamento' or passo_2 == 'Despedida') and (
        passo_3 == 'Cumprimento' or passo_3 == 'Balancê' or passo_3 == 'Passeio' or passo_3 == 'Túnel' or passo_3 == 'Serrote' or passo_3 == 'Casamento' or passo_3 == 'Despedida') and (
        passo_4 == 'Cumprimento' or passo_4 == 'Balancê' or passo_4 == 'Passeio' or passo_4 == 'Túnel' or passo_4 == 'Serrote' or passo_4 == 'Casamento' or passo_4 == 'Despedida') and (
        passo_5 == 'Cumprimento' or passo_5 == 'Balancê' or passo_5 == 'Passeio' or passo_5 == 'Túnel' or passo_5 == 'Serrote' or passo_5 == 'Casamento' or passo_5 == 'Despedida') and not (
        passo_1 == passo_2 == passo_3 == passo_4 == passo_5):
    pontuacao = 0

    if passo_1 == 'Cumprimento':
        pontuacao += 100
    if passo_1 == 'Balancê':
        pontuacao += 50
    if passo_1 == 'Passeio':
        pontuacao += 70
    if passo_1 == 'Serrote':
        pontuacao += 100
    if passo_1 == 'Túnel':
        pontuacao = 0.9 * pontuacao

    if passo_2 == 'Cumprimento':
        pontuacao += 10
    if passo_2 == 'Balancê':
        pontuacao += 50
    if passo_2 == 'Passeio':
        pontuacao += 70
    if passo_2 == 'Serrote':
        pontuacao += 100
    if passo_2 == 'Túnel':
        pontuacao = 0.9 * pontuacao

    if passo_3 == 'Cumprimento':
        pontuacao += 10
    if passo_3 == 'Balancê':
        pontuacao += 50
    if passo_3 == 'Passeio':
        pontuacao += 70
    if passo_3 == 'Serrote':
        pontuacao += 100
    if passo_3 == 'Túnel':
        pontuacao = 0.9 * pontuacao

    if passo_4 == 'Cumprimento':
        pontuacao += 10
    if passo_4 == 'Balancê':
        pontuacao += 50
    if passo_4 == 'Passeio':
        pontuacao += 70
    if passo_4 == 'Serrote':
        pontuacao += 100
    if passo_4 == 'Túnel':
        pontuacao = 0.9 * pontuacao

    if passo_5 == 'Cumprimento':
        pontuacao += 10
    if passo_5 == 'Balancê':
        pontuacao += 50
    if passo_5 == 'Passeio':
        pontuacao += 70
    if passo_5 == 'Serrote':
        pontuacao += 100
    if passo_5 == 'Despedida':
        pontuacao += 35
    if passo_5 == 'Túnel':
        pontuacao = 0.9 * pontuacao

    if passo_1 == 'Casamento' or passo_2 == 'Casamento' or passo_3 == 'Casamento' or passo_4 == 'Casamento' or passo_5 == 'Casamento':
        pontuacao = 2 * pontuacao

    if pontuacao == 0:
        print(
            f'Poxa, {nome_da_quadrilha}. Por utilizarem de algum passo não permitido vocês tiveram a pontuação zerada.')
    else:
        print(f'Parabéns, {nome_da_quadrilha}! Bela apresentação. A pontuação foi de {pontuacao:.1f}!')
else:
    print(f'Poxa, {nome_da_quadrilha}. Por utilizarem de algum passo não permitido vocês tiveram a pontuação zerada.')