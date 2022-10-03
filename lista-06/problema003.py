# adicionando sequencias a um dicionario
def add_dicionario(sequencia):

    dicionario = dict()

    for elemento in sequencia:

        # contando quantas vezes uma distancia foi atingida
        if elemento not in dicionario:
            dicionario[elemento] = 1

        else:
            dicionario[elemento] += 1

    return dicionario


# input
qtd_pedras = int(input())

sequencia1 = input().split()
sequencia2 = input().split()

# fazendo dicionarios
dict_seq1, dict_seq2 = add_dicionario(sequencia1), add_dicionario(sequencia2)

# outputs
if dict_seq1 == dict_seq2:
    print('Dale Gohan!')

else:
    print('Ih, nao foi agora, Gohan! Vamos tentar de novo semana que vem.')
