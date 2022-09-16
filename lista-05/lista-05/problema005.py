# função para verificar o grau de relevância, baseado na nota
def verificando_relevancia(lista_niveis):

    resultado = []

    if lista_niveis[0] <= 4:
        resultado = ['Baixo']

    elif 4 < lista_niveis[0] <= 6:
        resultado = ['Médio']

    else:
        resultado = ['Alto']

    if len(lista_niveis) == 1:

        return resultado

    else:

        return resultado + verificando_relevancia(lista_niveis[1:])


# função para contar cada classificação de relevância
def classificar_niveis(lista_classificacao, cont_alta, cont_media, cont_baixa):

    resultado = 0

    if lista_classificacao[0] == 'Alto':
        cont_alta += 1

    elif lista_classificacao[0] == 'Médio':
        cont_media += 1

    else:
        cont_baixa += 1

    if len(lista_classificacao) == 1:
        return cont_alta, cont_media, cont_baixa

    else:
        return classificar_niveis(lista_classificacao[1:], cont_alta, cont_media, cont_baixa)


# quantidade de acontecimentos
qtd_acontecimentos = int(input())

# recebendo e tratando níveis de relevância
nivel_relevancia_entrada = input()
lista_nivel_relevancia_str = nivel_relevancia_entrada.split(', ')
lista_nivel_relevancia = []

for nivel in lista_nivel_relevancia_str:
    lista_nivel_relevancia.append(int(nivel))

lista_classificacao_relevancia = verificando_relevancia(lista_nivel_relevancia)

nivel_alto_nota, nivel_medio, nivel_baixo = 0, 0, 0

# datas dos acontecimentos
datas_entrada = input()
lista_datas = datas_entrada.split(', ')

lista_datas_mes_ano = []
lista_datas_anos = []

for data in lista_datas:
    lista_datas_mes_ano.append([int(data.split('.')[0]), int(data.split('.')[1])])

# lista de acontecimentos
acontecimentos_entrada = input()
lista_acontecimentos = acontecimentos_entrada.split(', ')

# recebe data atual
data_atual = input()
mes_data_atual = int(data_atual.split('.')[0])
ano_data_atual = int(data_atual.split('.')[1])

# cálculo da insegurança
nivel_alto_nota, nivel_medio, nivel_baixo = classificar_niveis(lista_classificacao_relevancia, nivel_alto_nota, nivel_medio, nivel_baixo)

if nivel_medio + nivel_baixo != 0:
    inseguranca = int((nivel_medio/(nivel_baixo + nivel_medio))*100)
else:
    inseguranca = 0

# output

# inicializando variáveis para análise de gap e da existência de alta relevância
lista_gaps = []
relevancia = False
nivel_alto_tempo = 0

# definindo gaps
for data_completa in lista_datas_mes_ano:

    if mes_data_atual - data_completa[0] >= 0:
        gap_anos = ano_data_atual - data_completa[1]
        gap_meses = mes_data_atual - data_completa[0]

    else:
        gap_anos = ano_data_atual - data_completa[1] - 1
        gap_meses = 12 + (mes_data_atual - data_completa[0])

    if (gap_anos == 4 and gap_meses >= 6) or gap_anos >= 5:
        nivel_alto_tempo += 1

    lista_gaps.append([gap_anos, gap_meses])

if nivel_alto_nota > 0 or nivel_alto_tempo > 0:
    relevancia = True

# condicional da relevancia e inseguranca
if not relevancia:

    print('Os cálculos mostram que é possível acessar essa linha do tempo sem que haja muitos danos.')

    if inseguranca > 20:
        print(f'Mas é necessário termos cuidado, a taxa de insegurança é de {inseguranca}%')

    else:
        print('A chance de sucesso é muito alta. Mudaremos o mundo mais uma vez, dr. Helena Smith.')

else:
    print('Realizar essa operação é um grande erro. A humanidade pode entrar em colapso.')
    print(f'Há {nivel_alto_nota + nivel_alto_tempo} acontecimento(s) relevante(s). Se as consequências das suas ações anularem algum desses eventos, teremos sérios problemas.')

# dados dos acontecimentos
print('\nAqui estão os dados dos acontecimentos:')

for i in range(qtd_acontecimentos):
    print(f'{lista_acontecimentos[i]} | gap: {lista_gaps[i][0]} anos e {lista_gaps[i][1]} meses | nível de relevância: {lista_nivel_relevancia[i]}')
