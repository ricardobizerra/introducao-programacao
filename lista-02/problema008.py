qtd_instrucoes = 0

while not(1 <= qtd_instrucoes <= 4):
    qtd_instrucoes = input()
    qtd_instrucoes = int(qtd_instrucoes, 2)

for i in range(0, qtd_instrucoes):

    tipo_corpo = input()

    # se indicou planeta

    if tipo_corpo == '0101':

        # input

        caracteristica_planeta = ''
        beleza = 0
        possivel_vida_extraterra = 0
        agua_aparente = 0
        temp_adequada = 0
        qtd_luas = 0

        while caracteristica_planeta != 'End':

            caracteristica_planeta = input()

            if caracteristica_planeta == 'Beleza':
                beleza = int(input())

            elif caracteristica_planeta == 'Possibilidade de vida extraterrestre':
                possivel_vida_extraterra = int(input())

            elif caracteristica_planeta == 'Agua aparente':
                agua_aparente = int(input())

            elif caracteristica_planeta == 'Temperatura adequada':
                temp_adequada = int(input())

            elif caracteristica_planeta == 'Quantidade de luas':
                qtd_luas = input()
                qtd_luas = int(qtd_luas, 2)

        # output

        if agua_aparente == 1 and temp_adequada == 1 and beleza == 1 and possivel_vida_extraterra == 1:
            print(f'Achamos o planeta ideal e ainda tem {qtd_luas} lua(s)!')
            print('Parece bom demais pra ser verdade, que tipo de vida sera que nos aguarda?')

        elif agua_aparente == 1 and temp_adequada == 1 and beleza == 1 and possivel_vida_extraterra == 0:
            print('Ainda nao sabemos se o planeta e habitavel, parece nao haver vida')

        elif agua_aparente == 1 and temp_adequada == 1 and beleza == 0 and possivel_vida_extraterra == 1:
            print(f'O planeta e possivelmente habitavel porem olha essa aparencia, mesmo que tenha {qtd_luas} lua(s) vamos omitir esse do relatorio!')

        else:
            print('Vish! Esse nao satisfaz nem as condicoes basicas, nao perderemos tempo')

    # se indicou galáxia

    elif tipo_corpo == '1101':

        # input

        qtd_planetas_milhoes = ''
        valido = False

        while not valido:

            qtd_planetas_milhoes = input()

            if qtd_planetas_milhoes == '01100100':
                valido = True
            elif qtd_planetas_milhoes == '11001000':
                valido = True
            elif qtd_planetas_milhoes == '100101100':
                valido = True
            else:
                valido = False

        buraco_super = 2

        while buraco_super != 0 and buraco_super != 1:
            buraco_super = int(input())

        # output

        if buraco_super == 1:
            print(f'Ha um buraco negro supermassivo nesta galaxia, demais! Alem da existencia de cerca de {int(qtd_planetas_milhoes, 2)} milhoes de planetas')
        else:
            print(f'Aparentemente nao ha nenhum buraco negro supermassivo no centro dessa galaxia, jurava que todas tinham! Nao importa, ainda temos {int(qtd_planetas_milhoes, 2)} milhoes de planetas para observar algum deve apresentar possiblidade de vida')

    # se indicou buraco negro

    elif tipo_corpo == '0000':

        # input

        massa = input()

        spin = 2

        while spin != 0 and spin != 1:
            spin = int(input())

        carga = input()

        carga_neutra = False
        carga_negativa = False
        carga_positiva = False

        if carga == '0000':
            carga_neutra = True

        elif carga == '0001':
            carga_positiva = True

        else:
            carga_negativa = True

        # output

        print('Conseguimos todas informacoes necessarias para classificar este buraco negro no nosso banco de dados!')

        print('De acordo com as analises, o buraco negro:')

        print(f'- Tem massa de aproximadamente {int(massa, 2)} milhoes massas solares')

        print(f'- Possui em media {spin} rotacao(oes) por segundo')

        if carga_neutra:
            print('- Apresenta carga inexistente ou nula')

        elif carga_positiva:
            print('- Apresenta carga positiva')

        elif carga_negativa:
            print('- Apresenta carga negativa')
