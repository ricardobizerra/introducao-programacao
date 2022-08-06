mensagem = ''
feitos = 0
novo_feito = False
ganhou_nobel = False

while mensagem != 'É o fim da Estrada pra Sheldon Cooper' and not ganhou_nobel:
    mensagem = input()

    # condição do bazinga

    if mensagem == 'Bazinga' and novo_feito:
        feitos -= 1
        novo_feito = False

    # condição do xingamento

    xingamento = False

    if mensagem == 'Tinha que ser o engenheiro sem Phd do Wolowitz':
        xingamento = True
    elif mensagem == 'Leonard seu anão covarde':
        xingamento = True
    elif mensagem == 'Tu é muito burro Raj':
        xingamento = True

    if xingamento:
        print('Não xingue seus amigos Sheldon!')
        novo_feito = False

    # condição do feito 1

    if feitos == 0 and mensagem == 'Começou a Trabalhar na Caltech':
        novo_feito = True
        feitos += 1
    else:
        novo_feito = False

        # condição do feito 2

        if feitos == 1 and mensagem == 'Trabalho sobre a String Theory':
            novo_feito = True
            feitos += 1
        else:
            novo_feito = False

            # condição do feito 3

            if feitos == 2 and mensagem == 'Ganhar o Chancellor de ciência':
                novo_feito = True
                feitos += 1
            else:
                novo_feito = False

                # condição do feito 4

                if feitos == 3 and mensagem == 'Pensar na Teoria de Cooper-Hofstader':
                    novo_feito = True
                    feitos += 1
                else:
                    novo_feito = False

                    # condição do feito 5

                    if feitos == 4 and mensagem == 'Criou a Super Assimetria':
                        novo_feito = True
                        feitos += 1
                    else:
                        novo_feito = False

                        # condição para ganhar o nobel

                        if feitos == 5 and mensagem == 'Ganhar o Nobel':
                            novo_feito = True
                            ganhou_nobel = True
                        else:
                            novo_feito = False

if ganhou_nobel:
    print('Você conseguiu Sheldon, o Nobel é seu!!!')
else:
    if feitos == 0:
        print('Que potencial desperdiçado...')
    elif feitos == 1 or feitos == 2:
        print('Tão perto, mas tão longe')
    elif feitos == 3 or feitos == 4:
        print('Não desista Sheldon, você ainda têm muito para alcançar!')
    elif feitos == 5:
        print('Nãoooooo, esse momento ia ser seu Sheldon')
