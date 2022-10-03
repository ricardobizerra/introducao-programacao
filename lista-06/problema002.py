# analisa e retorna as posições
def ataque_kuroko(dicionario, alvo):

    lista = []

    for k in range(len(dicionario)):
        lista.append(dicionario[k][f'jogador {k}'])

    for m in range(len(lista)):

        for n in range(len(lista)):

            if m != n and lista[m] + lista[n] == alvo:
                return [m, n]


lista_companheiros = input()
lista_companheiros = lista_companheiros[1:-1].split(',')

# criação da lista de dicionários com as posições
dict_companheiros = []

for i in range(len(lista_companheiros)):
    lista_companheiros[i] = int(lista_companheiros[i])

    dict_companheiros.append({f'jogador {i}': lista_companheiros[i]})

numero_alvo = int(input())

# garantir ordem crecente
retorno = ataque_kuroko(dict_companheiros, numero_alvo)

if retorno[0] < retorno[1]:
    print([retorno[0], retorno[1]])

else:
    print([retorno[1], retorno[0]])
