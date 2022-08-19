# entradas
n = int(input())
m = int(input())

# inicializando listas e variavel
elementos = []
quantidades = []
elementos_utilizados = []
soma_igual = False
string_elementos_utilizados = ''

# loop para receber elementos e quantidades, e separando-os em listas para cada um
for a in range(0, m):

    elemento_qtd = input()

    lista_elemento_qtd = elemento_qtd.split(' ')

    elementos.append(lista_elemento_qtd[0])
    quantidades.append(int(lista_elemento_qtd[1]))

# copia da lista de quantidades para nao prejudicar os outputs finais
quantidades_copy = quantidades.copy()

# loop para verificar se a soma é igual
for i in range(-1, m - 1):

    if not soma_igual:

        if i >= 0:
            quantidades_copy.pop(0)

        len_quantidades = len(quantidades_copy)

        for j in range(0, len_quantidades):

            if not soma_igual:

                # criacao das sublistas
                sublista_quantidades = quantidades_copy[0:(len_quantidades - j)]

                soma_sublista = sum(sublista_quantidades)

                if soma_sublista == n:
                    soma_igual = True

                    # associando quantidades utilizadas aos elementos utilizados
                    for k in range(0, len(sublista_quantidades)):

                        index_original_quantidade = quantidades.index(sublista_quantidades[k], k)
                        elemento_utilizado = elementos[index_original_quantidade]
                        elementos_utilizados.append(elemento_utilizado)

# string dos elementos utilizados
for elem in elementos_utilizados:
    string_elementos_utilizados = string_elementos_utilizados + elem + ' '

# outputs iniciais
if soma_igual:
    print(f'Vencemos a batalha e a humanidade foi restaurada! {string_elementos_utilizados}foram usados para deszumbificar')

else:
    print('Estou sentido algo estranho... será que também vou virar zumbi?')
