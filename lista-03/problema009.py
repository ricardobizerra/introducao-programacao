# incializando listas, numeros de maior soma e senha
matriz = []

maior_soma_horizontal = -1
maior_soma_vertical = -1
maior_soma_diagonal = -1

par_maior_soma_horizontal = []
par_maior_soma_vertical = []
par_maior_soma_diagonal = []

senha = ''

# tamanho da matriz
n = int(input())

for i in range(n):

    linha = input()
    linha = linha.split(' ')

    matriz.append(linha)

# comparando matriz horizontal

for a in range(n):

    for b in range(n - 1):

        soma_horizontal = int(matriz[a][b]) + int(matriz[a][b + 1])

        if soma_horizontal > maior_soma_horizontal:

            maior_soma_horizontal = soma_horizontal
            par_maior_soma_horizontal = [matriz[a][b], matriz[a][b + 1]]

        else:
            par_maior_soma_horizontal = par_maior_soma_horizontal

# comparando matriz vertical

for c in range(n):

    for d in range(n - 1):

        soma_vertical = int(matriz[d][c]) + int(matriz[d + 1][c])

        if soma_vertical > maior_soma_vertical:

            maior_soma_vertical = soma_vertical
            par_maior_soma_vertical = [matriz[d][c], matriz[d + 1][c]]

        else:
            par_maior_soma_vertical = par_maior_soma_vertical

# comparando matriz diagonal principal

for k in range(n - 1):

    soma_diagonal = int(matriz[k][k]) + int(matriz[k + 1][k + 1])

    if soma_diagonal > maior_soma_diagonal:

        maior_soma_diagonal = soma_diagonal
        par_maior_soma_diagonal = [matriz[k][k], matriz[k + 1][k + 1]]

# gerando senha
for num in par_maior_soma_horizontal:
    senha = senha + num

for num in par_maior_soma_vertical:
    senha = senha + num

for num in par_maior_soma_diagonal:
    senha = senha + num

# output
print('Falei que era fácil Dustinzinho...')
print('Pegando todas os números que formam as combinações dos pares de cada sentido temos...')
print(f'Password: {senha}')
