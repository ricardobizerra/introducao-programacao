# dicionários
armas = {
    'chifre': 2,
    'cajado': 4,
    'espada': 6,
    'grande espada': 8,
    'dardo': 12
}

armaduras = {
    'pesada': 0,
    'media': 1,
    'leve': 3
}

grupo = {
    'bobby': (armas['grande espada'], armaduras['media']),
    'diana': (armas['dardo'], armaduras['leve']),
    'eric': (armas['grande espada'], armaduras['pesada']),
    'hank': (armas['espada'], armaduras['media']),
    'presto': (armas['cajado'], armaduras['leve']),
    'sheila': (armas['espada'], armaduras['leve']),
    'uni': (armas['chifre'], armaduras['leve'])
}

# inputs
adversario = input()

# alocar pontos de vida
if adversario == 'Vingador':
    vida_adversario = 30

elif adversario == 'Tiamat':
    vida_adversario = 20

elif adversario == 'Vingador das Sombras':
    vida_adversario = 14

else:
    vida_adversario = 9

# turnos
turnos = int(input())

# variável de seguimento da luta
luta_finalizada = False

# luta
while not luta_finalizada:

    atacante = input().lower()

    # encerra luta caso o ataque seja do mestre
    if atacante == 'mestre dos magos':
        luta_finalizada = True
        print('Muito obrigado amigo, que nos vejamos novamente um dia')

    else:
        # atualiza pontos de vida e progresso do adversário a cada golpe
        vida_adversario -= grupo[atacante][0]
        turnos -= grupo[atacante][1] + 1

        # output de finalização para morte do adversário
        if vida_adversario <= 0 and not luta_finalizada:
            luta_finalizada = True
            print(f'{atacante.capitalize()} executou o ultimo golpe em {adversario}, estamos livres!')

        # output de finalização para final dos turnos
        if turnos <= 0 and not luta_finalizada:
            luta_finalizada = True
            print(f'Oh nao, {adversario} e muito forte, este e o fim!')
