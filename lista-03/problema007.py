# inicializando variaveis e listas
responsavel_mochila = []
mochila = []
tamanho_mochila = []

# quantidade de mochilas
m = int(input())

# atribuicao de responsabilidades
nome_responsavel = input()
nomes_responsaveis = nome_responsavel.split(' ')

while len(nomes_responsaveis) != m:
    nome_responsavel = input()
    nomes_responsaveis = nome_responsavel.split(' ')

for nome in nomes_responsaveis:
    responsavel_mochila.append(nome)

# tamanhos das mochilas
for i in range(m):

    tamanho = int(input())

    while tamanho < 1:
        tamanho = int(input())

    tamanho_mochila.append(tamanho)

    # "abrindo" cada mochila
    mochila.append(['Lanterna', 'Omega 3 da top therm'])

# numero de itens a serem adicionados
n = int(input())

# nome dos itens e em qual mochila será adicionado
for j in range(n):

    nome_item = input()
    mochila_item = int(input())

    if len(mochila[mochila_item]) < tamanho_mochila[mochila_item]:
        mochila[mochila_item].append(nome_item)

    else:
        print('Mochila cheia. Não vai dar para levar.')

# entrada das ações
acao = input()

# loop de ocorrencia das ações
while acao != 'CHEGAMOS NO CIN!':

    if acao == 'Tirar da mochila' or acao == 'Guardar na mochila':
        acao_valida = True

    else:
        acao_valida = False

    if acao_valida:

        item_acao = input()
        mochila_item_acao = int(input())

        # tirar da mochila
        if acao == 'Tirar da mochila':

            if mochila[mochila_item_acao].count(item_acao) == 0:
                print(f'Você não tem {item_acao} na mochila {mochila_item_acao}.')

            else:
                print(f'{item_acao} usado com sucesso da mochila {mochila_item_acao}.')
                mochila[mochila_item_acao].remove(item_acao)

        # guardar na mochila
        else:

            if len(mochila[mochila_item_acao]) >= tamanho_mochila[mochila_item_acao]:
                print(f'Mochila {mochila_item_acao} cheia!')

            else:
                print(f'{item_acao} adicionado na mochila {mochila_item_acao}.')
                mochila[mochila_item_acao].append(item_acao)

    else:
        print('Ação inválida.')

    acao = input()

# mochilas de cada responsavel ao final das ações
for k in range(m):

    print(f'Mochila de {responsavel_mochila[k]} chegou assim:')

    for item in mochila[k]:
        print(item)
