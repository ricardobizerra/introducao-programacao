# cálculo do fatorial
def fatorial(i):

    resultado = 0

    if i <= 1:
        resultado = 1

    else:
        resultado = i * fatorial(i - 1)

    return resultado


# gerando sequencia de fatoriais
def sequencia_fatorial(n):

    resultado = []

    for b in range(n):
        resultado.append(fatorial(b))

    return resultado


# termo de fibonacci
def fibonacci(j):

    resultado = 0

    if j == 1:
        resultado = 0

    elif j == 2:
        resultado = 1

    else:
        resultado = fibonacci(j - 1) + fibonacci(j - 2)

    return resultado


# gerando sequencia de fibonacci
def sequencia_fibonacci(k):

    resultado = []

    for a in range(1, k + 1):
        resultado.append(fibonacci(a))

    return resultado


# entradas e inicialização de variável
senha_alterada = input()
qtd_palavras = int(input())
palavra_igual = False

# loop de comparação das palavras
for y in range(qtd_palavras):

    palavra_comparacao = input()
    nova_palavra = ''

    for letra in palavra_comparacao:

        # passo 1 - aplicação do mod 11
        operacao = (ord(letra) - 97) % 11

        # passo 2
        seq_fibonacci_operacao = sequencia_fibonacci(operacao)
        seq_fatorial_operacao = sequencia_fatorial(operacao)

        # passo 3 - análise dos cenários
        if operacao == 0:
            nova_palavra += '1'

        elif operacao % 2 != 0:

            for x in range(operacao):
                char = (seq_fibonacci_operacao[x] * seq_fatorial_operacao[x]) % 26
                nova_palavra += chr(char + 97)

        else:

            for x in range(operacao):
                char = (seq_fibonacci_operacao[x] + seq_fatorial_operacao[x]) % 26
                nova_palavra += chr(char + 97)

    # checar se a palavra transformada é igual à senha

    if nova_palavra == senha_alterada:
        palavra_igual = True

# outputs
if palavra_igual:
    print('Achamos! Achamos a senha.')

else:
    print('É... Temos que procurar mais.')
