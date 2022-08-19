# inicializando variáveis
lista_musicas = []
lista_geral_notas = []
nota_melhor_musica = -1
artista_melhor_musica = ''
nome_melhor_musica = ''

# entradas
artistas = input()
lista_artistas = artistas.split(' - ')

# loop dos artistas
for artista in lista_artistas:

    musicas = input()
    musicas_artista = musicas.split(' - ')

    # add as músicas do artista a uma lista geral de músicas
    lista_musicas.append(musicas_artista)

    nomes_notas_validas = []
    notas_musica = []
    iminencia_voto = 0

    # cria uma lista dentro da lista geral de notas para as músicas do artista
    lista_geral_notas.append([])

    # loop das músicas
    for musica in musicas_artista:

        musica_votada = False

        while not musica_votada:

            comentario = input()

            lista_comentario = comentario.split(': ')

            nome_comentario = lista_comentario[0]
            nota_comentario = lista_comentario[1]

            # checar se o comentário é uma nota válida
            if nota_comentario == '0':
                nota_valida = True

            elif nota_comentario == '1':
                nota_valida = True

            elif nota_comentario == '2':
                nota_valida = True

            elif nota_comentario == '3':
                nota_valida = True

            elif nota_comentario == '4':
                nota_valida = True

            elif nota_comentario == '5':
                nota_valida = True

            elif nota_comentario == '6':
                nota_valida = True

            elif nota_comentario == '7':
                nota_valida = True

            elif nota_comentario == '8':
                nota_valida = True

            elif nota_comentario == '9':
                nota_valida = True

            elif nota_comentario == '10':
                nota_valida = True

            else:
                nota_valida = False

            # se o comentário for válido
            if nota_valida:

                nome_ja_existia = False

                # verificando se a pessoa já votou ou tá votando pela primeira vez
                for nome in nomes_notas_validas:

                    # se já votou, apenas substitui a velha nota pela nova nota
                    if nome_comentario == nome:
                        notas_musica[0] = int(nota_comentario)
                        nome_ja_existia = True

                # add a lista de votantes, se não tinha votado
                if not nome_ja_existia:
                    nomes_notas_validas.append(nome_comentario)
                    notas_musica.append(int(nota_comentario))

                    iminencia_voto += 1

            # se dois derem notas, a música foi votada
            if iminencia_voto == 2:
                musica_votada = True
                iminencia_voto = 0

                # add a nota da música na lista geral de notas
                soma_notas_musica = sum(notas_musica)
                lista_geral_notas[lista_artistas.index(artista)].append(soma_notas_musica)

                # determinar a música de maior nota
                if soma_notas_musica > nota_melhor_musica:
                    nota_melhor_musica = soma_notas_musica
                    artista_melhor_musica = artista
                    nome_melhor_musica = musica

                nomes_notas_validas = []
                notas_musica = []

# música escolhida
escolha_musica = input()
escolha_musica = escolha_musica.split(': ')

musica_escolhida = escolha_musica[1].split(' - ')

# artista e nome da música escolhida
artista_musica_escolhida = musica_escolhida[0]
nome_musica_escolhida = musica_escolhida[1]

# buscando a nota da música escolhida
local_artista_escolhido_em_notas = lista_geral_notas[lista_artistas.index(artista_musica_escolhida)]
local_musica_escolhida_em_musicas = lista_musicas[lista_artistas.index(artista_musica_escolhida)]
nota_musica_escolhida = local_artista_escolhido_em_notas[local_musica_escolhida_em_musicas.index(nome_musica_escolhida)]

# cálculo da diferença e outputs finais
diferenca = nota_melhor_musica - nota_musica_escolhida

if diferenca == 0:
    print(f'Caraca {escolha_musica[0]} mandou bem! Essa música é a mais braba, com a nota {nota_musica_escolhida}')

else:
    print(f'Podia ter escolhido outra música, {escolha_musica[0]}. Essa é boa, mas perde em {diferenca} pontos pra a música com a melhor nota')
