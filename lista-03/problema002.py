# inicializando variaveis e listas
dono_lista = input()

quantidade = int(input())

elemento_percorrido = 0
lista_nomes = []
lista_notas = []
lista_notas_decrescente = []

# tratando entradas
for i in range(0, quantidade):

    nome_nota = input().split(' - ')

    nome_filme = nome_nota[0]
    nota_filme = float(nome_nota[1])

    lista_nomes.append(nome_filme)
    lista_notas.append(nota_filme)

# ordenando por bubble-sort
lista_notas_copy = lista_notas.copy()

while elemento_percorrido != len(lista_notas_copy):

    k = 0

    for k in range(0, len(lista_notas_copy) - 1):

        if lista_notas_copy[k] < lista_notas_copy[k + 1]:

            aux = lista_notas_copy[k + 1]
            lista_notas_copy[k + 1] = lista_notas_copy[k]
            lista_notas_copy[k] = aux

    elemento_percorrido += 1
    lista_notas_decrescente = [lista_notas_copy[(len(lista_notas_copy) - elemento_percorrido)]] + lista_notas_decrescente

# outputs
print(f'Os filmes sugeridos por {dono_lista} são:')

for nota in lista_notas_decrescente:

    indice_nome = lista_notas.index(nota)
    filme = lista_nomes[indice_nome]

    print(f'{filme} - {nota}')
