# inicializando listas
entradas = []
palavras_que_nao_repetem = []

# loop para entradas
for i in range(0, 10):

    entrada = input()

    entradas.append(entrada)

# checando e printando as palavras que nao repetiram
for entrada in entradas:

    k = 0
    vezes_aparicao_entrada = 0

    while k < len(entradas):

        if entrada == entradas[k]:
            vezes_aparicao_entrada += 1

        k += 1

    if vezes_aparicao_entrada == 1:
        palavras_que_nao_repetem.append(entrada)

print('As palavras sao:')

for palavra in palavras_que_nao_repetem:
    print(palavra)

# soma dos tamanhos das palavras que nao repetiram
soma_palavras = 0

for palavra in palavras_que_nao_repetem:
    soma_palavras += len(palavra)

print(f'A soma do tamanho das palavras é: {soma_palavras}')

# output final
print('Estou impressionado, você me venceu, pode ir embora...')
