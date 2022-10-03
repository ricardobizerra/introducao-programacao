# organizando cartas para ordenação
def organizar_cartas(dicionario):

    lista_ataque, lista_defesa = [], []

    for carta in dicionario.items():

        name = carta[0]
        valor_ataque, valor_defesa = carta[1]

        lista_ataque.append((name, valor_ataque))
        lista_defesa.append((name, valor_defesa))

    return lista_ataque, lista_defesa


# definindo o maior de uma lista, irá servir para ataque e defesa
def maior(lista):

    # bubble sort
    lista_copy = lista.copy()
    elemento_percorrido = 0
    lista_dec = []

    while elemento_percorrido != len(lista_copy):

        for j in range(len(lista) - 1):

            if lista_copy[j][1] < lista_copy[j + 1][1]:

                lista_copy[j], lista_copy[j + 1] = lista_copy[j + 1], lista_copy[j]

        elemento_percorrido += 1
        lista_dec = [lista_copy[(len(lista_copy) - elemento_percorrido)]] + lista_dec

    return lista_dec[0]


# entrada
n = int(input())

dicionario_cartas = dict()

for k in range(n):
    entrada = input()

    # tratando nome
    nome_lista = entrada.split()[:-2]

    nome = ''

    for palavra in nome_lista:
        nome += palavra + ' '

    nome = nome.strip()

    # armazenando poderes de ataque e defesa
    poder_ataque = int(entrada.split()[-2])
    poder_defesa = int(entrada.split()[-1])

    # adiciona carta ao dicionário
    dicionario_cartas[nome] = (poder_ataque, poder_defesa)

# retorna lista de cartas
lista_poder_ataque, lista_poder_defesa = organizar_cartas(dicionario_cartas)

# retorna o maior de ataque e de defesa com outputs
print(f'Carta com maior poder de ataque: {maior(lista_poder_ataque)[0]}')
print(f'Ataque: {maior(lista_poder_ataque)[1]}')
print()
print(f'Carta com maior poder de defesa: {maior(lista_poder_defesa)[0]}')
print(f'Defesa: {maior(lista_poder_defesa)[1]}')
