# comando add
def comando_add(nome, texto, dicionario):
    added = False

    for i in range(len(dicionario)):

        if nome in dicionario[i]['nomes'] and not added:
            added = True
            break

    if not added:
        dicionario.append({'nomes': nome, 'descricoes': texto})

    return dicionario


# comando desc
def comando_desc(nome, dicionario):
    retorno = ''

    exists = False

    for i in range(len(dicionario)):

        if nome in dicionario[i]['nomes']:
            retorno = dicionario[i]['descricoes']
            exists = True
            break

    if not exists:
        retorno = 'Ainda não há registro desse Pokémon'

    return retorno


# inicializando lista de dicionários
dicionario_pokemon, nomes_digitados = [], []

while True:

    try:
        comando = input()

        if len(comando.split(' ')) > 1:
            nome_comando, nome_pokemon = comando.split(' ')

            if nome_comando == 'ADD':

                if nome_pokemon not in nomes_digitados:
                    nomes_digitados.append(nome_pokemon)
                    descricao = input()

                    dicionario_pokemon = comando_add(nome_pokemon, descricao, dicionario_pokemon)

                    print('Pokémon adicionado com sucesso')

                else:
                    print('Pokémon já adicionado na Pokédex')

            elif nome_comando == 'DESC':

                mensagem_retorno = comando_desc(nome_pokemon, dicionario_pokemon)
                print(mensagem_retorno)

    # encerra programa
    except EOFError:
        break
