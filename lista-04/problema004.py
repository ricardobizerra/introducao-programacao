# funções
# separar as palavras em partes para analisar qual(is) estão nas sílabas do hospital
def analisador_palavra(palavra):

    possiveis_palavras = []

    for i in range(len(palavra)):

        for j in range(i + 1, len(palavra) + 1):

            possiveis_palavras.append(palavra[i:j])

    return possiveis_palavras


# formando frase para output
def string_palavras(lista_palavras_lembradas):

    string_lembradas = ''

    for k in lista_palavras_lembradas:

        if k == lista_palavras_lembradas[0]:
            string_lembradas = string_lembradas + k

        else:
            string_lembradas = string_lembradas + ', ' + k

    return string_lembradas


# inicializando listas
silabas_nome_hospital = ['shi', 'chi', 'ko', 'ku', 'ya', 'ma']
lista_lembrada_hospital = []

# loop
while len(lista_lembrada_hospital) != len(silabas_nome_hospital):

    # entrada
    input_palavra = input().lower().strip()

    # lista para analisar apenas as sílabas que vierem de um input, sendo "limpada" para a próxima iteração
    lista_lembrada = []
    lista_index_lembrada = []

    # analisando se parte da palavra está nas sílabas do hospital
    for possivel_palavra in analisador_palavra(input_palavra):

        if possivel_palavra in silabas_nome_hospital:

            if possivel_palavra not in lista_lembrada_hospital:
                lista_lembrada.append(possivel_palavra)
                lista_index_lembrada.append(silabas_nome_hospital.index(possivel_palavra))
                lista_lembrada_hospital.append(possivel_palavra)

    # checando se as sílabas lembradas estão em ordem
    esta_em_ordem = 0

    for idx in range(len(lista_index_lembrada) - 1):

        if lista_index_lembrada[idx + 1] == lista_index_lembrada[idx] + 1:
            esta_em_ordem += 1

    if esta_em_ordem == len(lista_index_lembrada) - 1:
        palavras_na_ordem = True

    else:
        palavras_na_ordem = False

    # outputs
    if not lista_lembrada:
        print('Infelizmente nenhuma dessas sílabas me lembrou do nome do hospital, Totoro.')

    else:

        concat_lembrada = ''

        for lembrada in lista_lembrada:
            concat_lembrada = concat_lembrada + lembrada

        if palavras_na_ordem and concat_lembrada == input_palavra and len(lista_lembrada) != 1:
            print(f'A palavra {concat_lembrada} está toda no nome do hospital. Acertou em cheio, Totoro!')

        else:

            if len(lista_lembrada) == 1:
                print(f'Lembrei! A sílaba {string_palavras(lista_lembrada)} está no nome do hospital. Obrigada, Totoro!')

            else:
                print(f'Lembrei! As sílabas: {string_palavras(lista_lembrada)} estão no nome do hospital. Obrigada, Totoro!')

    # output para quando todas as sílabas forem lembradas
    if len(lista_lembrada_hospital) == len(silabas_nome_hospital):
        print('Conseguimos lembrar o nome do hospital shichikokuyama, agora é só pegar o Catbus e ir até lá!')
