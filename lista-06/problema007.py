# funções
def def_item_mais_pedido(dict_contador):
    retorno, num_mais_pedido = '', 0

    for item_pedido in dict_contador.items():

        if item_pedido[1] != 0 and item_pedido[1] > num_mais_pedido:
            retorno, num_mais_pedido = item_pedido

    return retorno


def preco_novo_item(dict_precos_ingredientes, dict_cardapio):
    preco = 5

    for ingrediente in dict_cardapio[pedido]:
        preco += dict_precos_ingredientes[ingrediente]

    return preco


# dicionários
precos_ingredientes = {
    'trigo': 3,
    'fermento': 2,
    'manteiga': 6,
    'ovos': 2,
    'batata': 4,
    'arroz': 3,
    'siri': 8,
    'pao': 2,
    'tomate': 2,
    'alface': 1,
    'picles': 3,
    'queijo': 5
}

qtd_ingredientes = {
    'trigo': 5,
    'fermento': 5,
    'manteiga': 5,
    'ovos': 5,
    'batata': 5,
    'arroz': 5,
    'siri': 5,
    'pao': 5,
    'tomate': 5,
    'alface': 5,
    'picles': 5,
    'queijo': 5
}

cardapio = {
    'hamburguer de siri': ('siri', 'pao', 'alface', 'tomate', 'queijo', 'picles'),
    'pizza de siri': ('siri', 'trigo', 'fermento', 'ovos', 'queijo'),
    'siri frito': ('siri', 'manteiga'),
    'siri a parmegiana': ('siri', 'trigo', 'ovos', 'queijo', 'tomate')
}

precos_cardapio = {
    'hamburguer de siri': 24,
    'pizza de siri': 42,
    'siri frito': 15,
    'siri a parmegiana': 24
}

contador_pedidos = dict()

caixa = 40

while True:

    try:
        # recebe pedido
        pedido = input()

        # confere se o item pedido existe
        pedido_existe = False

        for item in precos_cardapio.items():

            # pedido existe
            if pedido == item[0]:

                for ingrediente in qtd_ingredientes.items():

                    # verifica se algum ingrediente está zerado e compra 4 unidades

                    if ingrediente[1] == 0 and ingrediente[0] in cardapio[pedido]:
                        # compra
                        qtd_ingredientes[ingrediente[0]] = 4

                        caixa -= 4 * precos_ingredientes[ingrediente[0]]

                    # consome ingredientes
                    if ingrediente[0] in cardapio[pedido]:
                        qtd_ingredientes[ingrediente[0]] -= 1

                # recebe valor da comida
                caixa += precos_cardapio[pedido]

                # output
                print(f'{pedido} saindo...')
                pedido_existe = True

        # contando o pedido no contador, inclusive os não existentes
        if pedido not in contador_pedidos.keys():
            contador_pedidos[pedido] = 1

        else:
            contador_pedidos[pedido] += 1

        # adicionando novo pedido
        if not pedido_existe:

            if contador_pedidos[pedido] < 3:
                print(f'{pedido} ainda não é uma opção disponível.')

            else:
                print(f'Atendendo demandas, {pedido} é a mais nova adição ao cardápio do Siri Cascudo.')

                # adiciona ao cardápio
                ingredientes_novo_pedido = input().split()

                for ingrediente in ingredientes_novo_pedido:

                    if ingrediente not in qtd_ingredientes:
                        ingredientes_novo_pedido.remove(ingrediente)

                cardapio[pedido] = tuple(ingredientes_novo_pedido)

                # determina preço da comida
                precos_cardapio[pedido] = preco_novo_item(precos_ingredientes, cardapio)

                # volta o contador de pedidos para zero
                contador_pedidos[pedido] = 0

    # encerra programa
    except EOFError:

        print('##### Fim do expediente #####')

        lucro = caixa - 40
        print(f'O lucro obtido no dia de hoje foi de R${lucro}.')

        item_mais_pedido = def_item_mais_pedido(contador_pedidos)

        if item_mais_pedido == 'hamburguer de siri':
            print('O bom e tradicional hambúrguer de siri, líder em vendas, nunca será superado!')

        else:
            print(
                f'{item_mais_pedido.capitalize()} está fazendo sucesso entre os clientes, ultrapassando até mesmo o lendário hambúrguer de siri.')

        break
