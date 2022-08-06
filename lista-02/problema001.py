# numero de rodadas
n = int(input())

# while, enquanto n não é maior que 0
while not (n > 0):
    n = int(input())

# inicializando variaveis de numero de vitorias
vitorias_sheldon = 0
vitorias_raj = 0

for n in range(1, n+1):
    escolha_sheldon = input()
    escolha_raj = input()

    if (escolha_sheldon == 'lagarto' and escolha_raj == 'spock') or (escolha_sheldon == 'spock' and escolha_raj == 'tesoura') or (escolha_sheldon == 'tesoura' and escolha_raj == 'lagarto'):
        vitorias_sheldon += 1

    elif (escolha_raj == 'lagarto' and escolha_sheldon == 'spock') or (escolha_raj == 'spock' and escolha_sheldon == 'tesoura') or (escolha_raj == 'tesoura' and escolha_sheldon == 'lagarto'):
        vitorias_raj += 1

    # em caso de empate, nenhum dos dois recebe vitoria
else:

    if vitorias_sheldon > vitorias_raj:
        print('BAZINGA! EU SOU O SENHOR DA SALA!')

    elif vitorias_raj > vitorias_sheldon:
        print('ENGOLE ESSA, SHELDON!')

    # valido tambem caso ocorram apenas empates, já que, nesse caso, vitorias_sheldon == vitorias_raj == 0
    elif vitorias_sheldon == vitorias_raj:
        print('Oh não, precisamos de outra rodada.')
