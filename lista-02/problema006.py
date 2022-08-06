toc = ''
contagem = 0
flag_invalido = 0

while toc != 'Boa noite':
    toc = input()

    if toc == 'Boa noite':
        print('Boa noite Penny')
        continue
    elif toc != 'toc-toc-toc':
        flag_invalido = 1
        for i in range(0, flag_invalido):
            print('Não pode entrar, se identifique!!!')
        contagem = 0
        continue
    else:
        penny = input()
        if penny != 'Penny':
            flag_invalido = 1
            for i in range(0, flag_invalido):
                print('Não pode entrar, se identifique!!!')
            contagem = 0
            continue

        if toc == 'toc-toc-toc' and penny == 'Penny':
            contagem += 1

            print(contagem)

            if contagem == 3:
                print('Pode entrar Sheldon')
                contagem = 0
