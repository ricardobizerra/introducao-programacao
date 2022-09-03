# funções de operações
def soma(m1, m2, tamanho):

    matriz_modificada = []

    for a in range(tamanho):

        matriz_modificada.append([])

        for b in range(tamanho):

            elemento = int(m1[a][b]) + int(m2[a][b])
            matriz_modificada[a].append(elemento)
    
    return matriz_modificada


def subtracao(m1, m2, tamanho):

    matriz_modificada = []

    for a in range(tamanho):

        matriz_modificada.append([])

        for b in range(tamanho):

            elemento = int(m1[a][b]) - int(m2[a][b])

            matriz_modificada[a].append(elemento)
    
    return matriz_modificada


def multiplicacao_matriz(m1, m2, tamanho):

    matriz_modificada = []

    for a in range(tamanho):

        matriz_modificada.append([])

        for b in range(tamanho):

            elemento = 0

            for c in range(tamanho):

                fator = int(m1[a][c]) * int(m2[c][b])

                elemento += fator

            matriz_modificada[a].append(elemento)

    return matriz_modificada


def multiplicacao_escalar(inteiro, matriz, tamanho):

    matriz_modificada = []

    for a in range(tamanho):

        matriz_modificada.append([])

        for b in range(tamanho):

            elemento = inteiro * int(matriz[a][b])
            matriz_modificada[a].append(elemento)

    return matriz_modificada


# tamanho das matrizes
tamanho_matriz = int(input())

# primeira matriz
matriz1 = []

for i in range(tamanho_matriz):

    linha = input()
    elementos = linha.split(' ')

    matriz1.append(elementos)

# segunda matriz
matriz2 = []

for j in range(tamanho_matriz):

    linha = input()
    elementos = linha.split(' ')

    matriz2.append(elementos)

# quantidade de operações
qtd_operacoes = int(input())

resultado = []

# recebendo operações
for k in range(qtd_operacoes):

    operacao = input()
    operacao = operacao.split(' ')

    # definindo quais as matrizes serão utilizadas na operação

    if operacao[2] == 'm1':
        operando1 = matriz1
    
    elif operacao[2] == 'm2':
        operando1 = matriz2

    else:
        operando1 = int(operacao[2])
    
    if operacao[4] == 'm1':
        operando2 = matriz1
    
    elif operacao[4] == 'm2':
        operando2 = matriz2

    else:
        operando2 = int(operacao[4])

    # condicional para as operações

    resultado = []

    if operacao[3] == '+':
        resultado = soma(operando1, operando2, tamanho_matriz)
    
    elif operacao[3] == '-':
        resultado = subtracao(operando1, operando2, tamanho_matriz)
    
    elif operacao[3] == '.':
        resultado = multiplicacao_matriz(operando1, operando2, tamanho_matriz)
    
    elif operacao[3] == '*':

        if operando1 == matriz1 or operando1 == matriz2:
            escalar = operando2
            resultado = multiplicacao_escalar(escalar, operando1, tamanho_matriz)

        else:
            escalar = operando1
            resultado = multiplicacao_escalar(escalar, operando2, tamanho_matriz)
    
    # recebimento do resultado pela matriz

    if operacao[0] == 'm1':
        matriz1 = resultado
    
    else:
        matriz2 = resultado

# imprimindo o resultado da última operação
for m in range(tamanho_matriz):

    for n in range(tamanho_matriz):

        if n != tamanho_matriz - 1:
            print(resultado[m][n], end=' ')

        else:
            print(resultado[m][n])
