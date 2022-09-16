# cálculo do fatorial
def fatorial(i):

    resultado = 0

    if i <= 1:
        resultado = 1

    else:
        resultado = i * fatorial(i - 1)

    return resultado


# conferindo quantidades de maiúsculas e minúsculas
def analise_expressao(expressao, cont_upper, cont_lower):

    resultado = 0

    if len(expressao) == 0:

        if cont_upper >= cont_lower:
            resultado = cont_upper

        else:
            resultado = cont_lower

    else:

        if expressao[-1].isupper():
            cont_upper += 1

        else:
            cont_lower += 1

        resultado = analise_expressao(expressao[:-1], cont_upper, cont_lower)

    return resultado


# análise do char
def letra_dimensao(expressao, valor_r, expressao_upper, expressao_lower):

    resultado = ''

    if len(expressao) == 0:

        if len(expressao_upper) >= len(expressao_lower):
            resultado = expressao_upper[valor_r]

        else:
            resultado = expressao_lower[valor_r]

    else:

        if expressao[-1].isupper():
            expressao_upper = expressao[-1] + expressao_upper

        else:
            expressao_lower = expressao[-1] + expressao_lower

        resultado = letra_dimensao(expressao[:-1], valor_r, expressao_upper, expressao_lower)

    return resultado


# entrada da string
frase = input()

# cálculo de num
n = len(frase)
k = analise_expressao(frase, 0, 0)

num = int((fatorial(n))/(fatorial(k) * fatorial(n - k)))

# cálculo de char
r = num % k
char = letra_dimensao(frase, r, '', '')

# output
dimensao = char + '-' + str(num)

if char.isupper():
    print(f'Morty!!! Morty!!! Vamos para a dimensão {dimensao}, Morty!!! Vai ser legal, Morty!!! Rick e Morty na dimensão {dimensao} para sempre, Morty!!! Wubba lubba dub dub!!!')

else:
    print(f'Oh geez, Rick!!! Eu não sei se ir pra dimensão {dimensao} é uma boa ideia... Eu estou com medo, Rick!!! Oh geez!!!')
