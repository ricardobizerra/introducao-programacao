# entradas
resultados = input()
sequencia_bits = input()

# inicializando variaveis e listas
pontuacao_parcial = 0
pontuacao_final = 0
pontuacao_esperada = 0
pontuacoes_parciais = []

n_vitorias = 0
n_empates = 0
n_derrotas = 0

lista_resultados = resultados.split(' ')
lista_interferencias = sequencia_bits.split(' ')
nova_lista_resultados = lista_resultados.copy()

for k in range(0, 12):

    # checando interferencias e calculando pontuacoes, vitorias, empates e derrotas
    if lista_interferencias[k] == '1':

        if lista_resultados[k] == 'V':

            print('O maldito sapo interferiu no resultado! O que parecia uma vitória garantida terminou em um empate.')
            nova_lista_resultados[k] = 'E'

            pontuacao_parcial += 1
            pontuacao_esperada += 3

            n_empates += 1

        elif lista_resultados[k] == 'E':

            print('O anfíbio da maldição interferiu no resultado! Um empate tranquilo virou uma frustrante derrota.')
            nova_lista_resultados[k] = 'D'

            pontuacao_esperada += 1

            n_derrotas += 1

        else:

            print('O que já era ruim, se tornou uma humilhante derrota. Desgraçado desse sapo!')

            n_derrotas += 1

    else:

        if lista_resultados[k] == 'V':

            pontuacao_parcial += 3
            pontuacao_esperada += 3

            n_vitorias += 1

        elif lista_resultados[k] == 'E':

            pontuacao_parcial += 1
            pontuacao_esperada += 1

            n_empates += 1

        else:
            n_derrotas += 1

    # lista de pontuacoes parciais por fatia de jogos
    if k == 3:
        pontuacoes_parciais.append(pontuacao_parcial)
        pontuacao_parcial = 0

    elif k == 7:

        pontuacoes_parciais.append(pontuacao_parcial)
        pontuacao_parcial = 0

    elif k == 11:

        pontuacoes_parciais.append(pontuacao_parcial)

# calculo da pontuacao final e outputs de fatias de jogos
for n in range(0, 3):

    n_fatia = n + 1
    pontuacao_final += pontuacoes_parciais[n]

    if pontuacoes_parciais[n] > 7:
        print(f'A pontuação na {n_fatia}ª fatia de 4 jogos está com uma gordurinha de {pontuacoes_parciais[n] - 7} pontos.')

    elif pontuacoes_parciais[n] == 7:
        print(f'A pontuação na {n_fatia}ª fatia de 4 jogos está dentro do planejado.')

    else:
        print(f'A pontuação na {n_fatia}ª fatia de 4 jogos está abaixo da planejada em {7 - pontuacoes_parciais[n]} pontos.')

# calculo e output de pontos perdidos
pontos_perdidos = pontuacao_esperada - pontuacao_final

if pontos_perdidos > 0:
    print(f'A maldição do sapo fez o Vascão perder {pontos_perdidos} pontos. Um número preocupante, que pode fazer diferença.')

elif pontos_perdidos == 0:
    print('A maldição parece que não teve impacto relevante! Não houve nenhuma perda de pontos.')

# outputs de pontuacao atingida
if pontuacao_final >= 21:
    print(f'Na reta final do campeonato, o Vasco garantiu um total de {pontuacao_final} pontos, com {n_vitorias} vitórias, {n_empates} empates e {n_derrotas} derrotas, e alcançou o tão esperado acesso. O Clube do Fomento Corporal vibra num SJ lotado!')

else:
    print(f'Na reta final do campeonato, o Vasco fez somente {pontuacao_final} pontos, com {n_vitorias} vitórias, {n_empates} empates e {n_derrotas} derrotas, e não conseguiu o acesso. Mais um ano de série B e sofrimento. Mob, o clube e a torcida estão completamente desolados.')
