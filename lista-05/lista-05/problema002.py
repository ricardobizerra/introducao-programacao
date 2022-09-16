# função para verificar qtd de parênteses
def verificar_parenteses(expressao, contador_abre, contador_fecha):

    if len(expressao) == 0:
        return [contador_abre, contador_fecha]

    else:

        if expressao[-1] == '(':
            contador_abre += 1

        elif expressao[-1] == ')':
            contador_fecha += 1

        return verificar_parenteses(expressao[:-1], contador_abre, contador_fecha)


# quantidade de sentenças
n = int(input())

# entrada e output das sentenças
for i in range(n):
    # entrada
    sentenca = input()
    cont_abre_parenteses = 0
    cont_fecha_parenteses = 0

    ocorrencias = verificar_parenteses(sentenca, cont_abre_parenteses, cont_fecha_parenteses)

    # output
    if ocorrencias[0] == ocorrencias[1]:
        print("Essa sentença está com os parênteses balanceados, HOORAY!")

    elif ocorrencias[0] > ocorrencias[1]:
        print("A quantidade de parênteses '(' está maior que a de ')', vamos descartá-la")

    else:
        print("")
