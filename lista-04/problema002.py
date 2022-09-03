# função que verifica a origem do barulho
def verificando_barulho(valor_entrada):

    barulho_inseto, barulho_aeronave = False, False

    lista_sons_insetos = ['crcrcrcrcr', 'uuuuuuuoooooo', 'ooooooeeeeeeee']
    lista_sons_aeronaves = ['ppprrrrrooon', 'tutututututututu', 'eeeeeeeeoooooo']

    # divide as palavras da frase de entrada para tentar interceptar com algum dos padrões
    for palavra in valor_entrada.split(' '):

        if palavra in lista_sons_insetos:
            barulho_inseto = True

        if palavra in lista_sons_aeronaves:
            barulho_aeronave = True

    # outputs
    if barulho_inseto and not barulho_aeronave:
        return 'É apenas o Mar Podre se comunicando, podemos ficar tranquilos, por enquanto…'

    elif not barulho_inseto and barulho_aeronave:
        return 'São sinais de aeronaves estrangeiras! Devemos preparar nossas defesas??'

    elif barulho_inseto and barulho_aeronave:
        return 'A transmissão sugere que tropas estrangeiras e as criaturas do Mar Podre irão se confrontar! Precisamos impedi-los antes que mais mortes desnecessárias ocorram!'

    else:
        return 'não identificado'


barulho_identificado = True

while barulho_identificado:

    entrada = input()

    # condicao de parada das analises
    if verificando_barulho(entrada) == 'não identificado':
        print('Não é possível determinar a origem da transmissão… Isso deverá levar mais algum tempo.')
        barulho_identificado = False

    else:
        print(verificando_barulho(entrada))
