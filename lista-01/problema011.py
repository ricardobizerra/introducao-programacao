# meus atributos
seu_nome = 'São João'
seus_pontos_vida = int(input())
seu_ataque = int(input())
sua_defesa = int(input())
sua_fraqueza = input()
sua_resistencia = input()

# atributos do inimigo
nome_entidade = input()
pontos_vida_entidade = int(input())
ataque_entidade = int(input())
defesa_entidade = int(input())
fraqueza_entidade = input()
resistencia_entidade = input()

if sua_fraqueza != 'fogo' and sua_fraqueza != 'gelo' and sua_fraqueza != 'eletricidade':
    sua_fraqueza = 'naotem'
if sua_resistencia != 'fogo' and sua_resistencia != 'gelo' and sua_resistencia != 'eletricidade':
    sua_resistencia = 'nãotem'
if fraqueza_entidade != 'fogo' and fraqueza_entidade != 'gelo' and fraqueza_entidade != 'eletricidade':
    fraqueza_entidade = 'nao tem'
if resistencia_entidade != 'fogo' and resistencia_entidade != 'gelo' and resistencia_entidade != 'eletricidade':
    resistencia_entidade = 'não tem'

turno = 1

if turno == 1 and (sua_fraqueza != fraqueza_entidade) and (sua_resistencia != resistencia_entidade) and (sua_defesa < seu_ataque > defesa_entidade) and (sua_defesa < ataque_entidade > defesa_entidade):

    print(f'Turno: {turno}')

    atacante = seu_nome
    atacado = nome_entidade

    t1_ataque = input()
    dano_geral = seu_ataque - defesa_entidade

    acerto_critico = ''

    if t1_ataque == 'Ataque Físico':
        pontos_vida_entidade -= dano_geral

        if pontos_vida_entidade >= 0:
            pontos_vida_entidade = pontos_vida_entidade
        else:
            pontos_vida_entidade = 0

        print(f'{atacante} usou {t1_ataque} e causou {dano_geral} de dano em {atacado} que agora tem {pontos_vida_entidade} de vida.')

    elif t1_ataque == 'Agi':
        if resistencia_entidade == 'fogo':
            dano_geral = int(0.5 * dano_geral)
            pontos_vida_entidade -= dano_geral

            if pontos_vida_entidade >= 0:
                pontos_vida_entidade = pontos_vida_entidade
            else:
                pontos_vida_entidade = 0

            print(f'{atacante} usou {t1_ataque}, mas acertou uma resistência, portanto causou apenas {dano_geral} de dano em {atacado} que agora tem {pontos_vida_entidade} de vida.')

        elif fraqueza_entidade == 'fogo':
            dano_geral = int(1.7 * dano_geral)
            pontos_vida_entidade -= dano_geral
            acerto_critico = atacado

            if pontos_vida_entidade >= 0:
                pontos_vida_entidade = pontos_vida_entidade
            else:
                pontos_vida_entidade = 0

            print(f'Isso! {atacante} usou {t1_ataque} e acertou a fraqueza do adversário! A magia causou {dano_geral} de dano em {atacado} que agora tem {pontos_vida_entidade} de vida.')

        else:
            pontos_vida_entidade -= dano_geral

            if pontos_vida_entidade >= 0:
                pontos_vida_entidade = pontos_vida_entidade
            else:
                pontos_vida_entidade = 0

            print(f'{atacante} usou {t1_ataque} e causou {dano_geral} de dano em {atacado} que agora tem {pontos_vida_entidade} de vida.')

    elif t1_ataque == 'Bufu':
        if resistencia_entidade == 'gelo':
            dano_geral = int(0.5 * dano_geral)
            pontos_vida_entidade -= dano_geral

            if pontos_vida_entidade >= 0:
                pontos_vida_entidade = pontos_vida_entidade
            else:
                pontos_vida_entidade = 0

            print(f'{atacante} usou {t1_ataque}, mas acertou uma resistência, portanto causou apenas {dano_geral} de dano em {atacado} que agora tem {pontos_vida_entidade} de vida.')

        elif fraqueza_entidade == 'gelo':
            dano_geral = int(1.7 * dano_geral)
            pontos_vida_entidade -= dano_geral
            acerto_critico = atacado

            if pontos_vida_entidade >= 0:
                pontos_vida_entidade = pontos_vida_entidade
            else:
                pontos_vida_entidade = 0

            print(f'Isso! {atacante} usou {t1_ataque} e acertou a fraqueza do adversário! A magia causou {dano_geral} de dano em {atacado} que agora tem {pontos_vida_entidade} de vida.')

        else:
            pontos_vida_entidade -= dano_geral

            if pontos_vida_entidade >= 0:
                pontos_vida_entidade = pontos_vida_entidade
            else:
                pontos_vida_entidade = 0

            print(f'{atacante} usou {t1_ataque} e causou {dano_geral} de dano em {atacado} que agora tem {pontos_vida_entidade} de vida.')

    elif t1_ataque == 'Zio':
        if resistencia_entidade == 'eletricidade':
            dano_geral = int(0.5 * dano_geral)
            pontos_vida_entidade -= dano_geral

            if pontos_vida_entidade >= 0:
                pontos_vida_entidade = pontos_vida_entidade
            else:
                pontos_vida_entidade = 0

            print(f'{atacante} usou {t1_ataque}, mas acertou uma resistência, portanto causou apenas {dano_geral} de dano em {atacado} que agora tem {pontos_vida_entidade} de vida.')

        elif fraqueza_entidade == 'eletricidade':
            dano_geral = int(1.7 * dano_geral)
            pontos_vida_entidade -= dano_geral
            acerto_critico = atacado

            if pontos_vida_entidade >= 0:
                pontos_vida_entidade = pontos_vida_entidade
            else:
                pontos_vida_entidade = 0

            print(f'Isso! {atacante} usou {t1_ataque} e acertou a fraqueza do adversário! A magia causou {dano_geral} de dano em {atacado} que agora tem {pontos_vida_entidade} de vida.')

        else:
            pontos_vida_entidade -= dano_geral

            if pontos_vida_entidade >= 0:
                pontos_vida_entidade = pontos_vida_entidade
            else:
                pontos_vida_entidade = 0

            print(f'{atacante} usou {t1_ataque} e causou {dano_geral} de dano em {atacado} que agora tem {pontos_vida_entidade} de vida.')

    if pontos_vida_entidade == 0:
        turno = 0
        print('Vitória! Parece que o Nahobino São João reinará nesse solstício!')

    else:
        turno += 1

        print(f'Turno: {turno}')

        atacante = nome_entidade
        atacado = seu_nome

        dano_geral = ataque_entidade - sua_defesa

        if acerto_critico == nome_entidade:
            print(f'{atacante} teve sua fraqueza em {fraqueza_entidade} acertada, portanto não poderá agir.')

        else:

            t2_ataque = input()

            if t2_ataque == 'Ataque Físico':
                seus_pontos_vida -= dano_geral

                if seus_pontos_vida >= 0:
                    seus_pontos_vida = seus_pontos_vida
                else:
                    seus_pontos_vida = 0

                print(f'{atacante} usou {t2_ataque} e causou {dano_geral} de dano em {atacado} que agora tem {seus_pontos_vida} de vida.')

            elif t2_ataque == 'Agi':
                if sua_resistencia == 'fogo':
                    dano_geral = int(0.5 * dano_geral)
                    seus_pontos_vida -= dano_geral

                    if seus_pontos_vida >= 0:
                        seus_pontos_vida = seus_pontos_vida
                    else:
                        seus_pontos_vida = 0

                    print(f'{atacante} usou {t2_ataque}, mas acertou uma resistência, portanto causou apenas {dano_geral} de dano em {atacado} que agora tem {seus_pontos_vida} de vida.')

                elif sua_fraqueza == 'fogo':
                    dano_geral = int(1.7 * dano_geral)
                    seus_pontos_vida -= dano_geral
                    acerto_critico = atacado

                    if seus_pontos_vida >= 0:
                        seus_pontos_vida = seus_pontos_vida
                    else:
                        seus_pontos_vida = 0

                    print(f'Vixe! {atacante} usou {t2_ataque} e acertou sua fraqueza! A magia causou {dano_geral} de dano em {atacado} que agora tem {seus_pontos_vida} de vida.')

                else:
                    seus_pontos_vida -= dano_geral

                    if seus_pontos_vida >= 0:
                        seus_pontos_vida = seus_pontos_vida
                    else:
                        seus_pontos_vida = 0

                    print(f'{atacante} usou {t2_ataque} e causou {dano_geral} de dano em {atacado} que agora tem {seus_pontos_vida} de vida.')

            elif t2_ataque == 'Bufu':
                if sua_resistencia == 'gelo':
                    dano_geral = int(0.5 * dano_geral)
                    seus_pontos_vida -= dano_geral

                    if seus_pontos_vida >= 0:
                        seus_pontos_vida = seus_pontos_vida
                    else:
                        seus_pontos_vida = 0

                    print(f'{atacante} usou {t2_ataque}, mas acertou uma resistência, portanto causou apenas {dano_geral} de dano em {atacado} que agora tem {seus_pontos_vida} de vida.')

                elif sua_fraqueza == 'gelo':
                    dano_geral = int(1.7 * dano_geral)
                    seus_pontos_vida -= dano_geral
                    acerto_critico = atacado

                    if seus_pontos_vida >= 0:
                        seus_pontos_vida = seus_pontos_vida
                    else:
                        seus_pontos_vida = 0

                    print(f'Vixe! {atacante} usou {t2_ataque} e acertou sua fraqueza! A magia causou {dano_geral} de dano em {atacado} que agora tem {seus_pontos_vida} de vida.')

                else:
                    seus_pontos_vida -= dano_geral

                    if seus_pontos_vida >= 0:
                        seus_pontos_vida = seus_pontos_vida
                    else:
                        seus_pontos_vida = 0

                    print(f'{atacante} usou {t2_ataque} e causou {dano_geral} de dano em {atacado} que agora tem {seus_pontos_vida} de vida.')

            elif t2_ataque == 'Zio':
                if sua_resistencia == 'eletricidade':
                    dano_geral = int(0.5 * dano_geral)
                    seus_pontos_vida -= dano_geral

                    if seus_pontos_vida >= 0:
                        seus_pontos_vida = seus_pontos_vida
                    else:
                        seus_pontos_vida = 0

                    print(f'{atacante} usou {t2_ataque}, mas acertou uma resistência, portanto causou apenas {dano_geral} de dano em {atacado} que agora tem {seus_pontos_vida} de vida.')

                elif sua_fraqueza == 'eletricidade':
                    dano_geral = int(1.7 * dano_geral)
                    seus_pontos_vida -= dano_geral
                    acerto_critico = atacado

                    if seus_pontos_vida >= 0:
                        seus_pontos_vida = seus_pontos_vida
                    else:
                        seus_pontos_vida = 0

                    print(f'Vixe! {atacante} usou {t2_ataque} e acertou sua fraqueza! A magia causou {dano_geral} de dano em {atacado} que agora tem {seus_pontos_vida} de vida.')

                else:
                    seus_pontos_vida -= dano_geral

                    if seus_pontos_vida >= 0:
                        seus_pontos_vida = seus_pontos_vida
                    else:
                        seus_pontos_vida = 0

                    print(f'{atacante} usou {t2_ataque} e causou {dano_geral} de dano em {atacado} que agora tem {seus_pontos_vida} de vida.')

        if seus_pontos_vida == 0:
            turno = 0
            print(f'Morremos… Parece que {nome_entidade} tem mais chances de ascender ao trono da Midsommar…')

        else:
            turno += 1

            print(f'Turno: {turno}')

            atacante = seu_nome
            atacado = nome_entidade

            dano_geral = seu_ataque - defesa_entidade

            if acerto_critico == seu_nome:
                print(f'{atacante} teve sua fraqueza em {sua_fraqueza} acertada, portanto não poderá agir.')

            else:

                t3_ataque = input()

                if t3_ataque == 'Ataque Físico':
                    pontos_vida_entidade -= dano_geral

                    if pontos_vida_entidade >= 0:
                        pontos_vida_entidade = pontos_vida_entidade
                    else:
                        pontos_vida_entidade = 0

                    print(f'{atacante} usou {t3_ataque} e causou {dano_geral} de dano em {atacado} que agora tem {pontos_vida_entidade} de vida.')

                elif t3_ataque == 'Agi':
                    if resistencia_entidade == 'fogo':
                        dano_geral = int(0.5 * dano_geral)
                        pontos_vida_entidade -= dano_geral

                        if pontos_vida_entidade >= 0:
                            pontos_vida_entidade = pontos_vida_entidade
                        else:
                            pontos_vida_entidade = 0

                        print(f'{atacante} usou {t3_ataque}, mas acertou uma resistência, portanto causou apenas {dano_geral} de dano em {atacado} que agora tem {pontos_vida_entidade} de vida.')

                    elif fraqueza_entidade == 'fogo':
                        dano_geral = int(1.7 * dano_geral)
                        pontos_vida_entidade -= dano_geral
                        acerto_critico = atacado

                        if pontos_vida_entidade >= 0:
                            pontos_vida_entidade = pontos_vida_entidade
                        else:
                            pontos_vida_entidade = 0

                        print(f'Isso! {atacante} usou {t3_ataque} e acertou a fraqueza do adversário! A magia causou {dano_geral} de dano em {atacado} que agora tem {pontos_vida_entidade} de vida.')

                    else:
                        pontos_vida_entidade -= dano_geral

                        if pontos_vida_entidade >= 0:
                            pontos_vida_entidade = pontos_vida_entidade
                        else:
                            pontos_vida_entidade = 0

                        print(f'{atacante} usou {t3_ataque} e causou {dano_geral} de dano em {atacado} que agora tem {pontos_vida_entidade} de vida.')

                elif t3_ataque == 'Bufu':
                    if resistencia_entidade == 'gelo':
                        dano_geral = int(0.5 * dano_geral)
                        pontos_vida_entidade -= dano_geral

                        if pontos_vida_entidade >= 0:
                            pontos_vida_entidade = pontos_vida_entidade
                        else:
                            pontos_vida_entidade = 0

                        print(f'{atacante} usou {t3_ataque}, mas acertou uma resistência, portanto causou apenas {dano_geral} de dano em {atacado} que agora tem {pontos_vida_entidade} de vida.')

                    elif fraqueza_entidade == 'gelo':
                        dano_geral = int(1.7 * dano_geral)
                        pontos_vida_entidade -= dano_geral
                        acerto_critico = atacado

                        if pontos_vida_entidade >= 0:
                            pontos_vida_entidade = pontos_vida_entidade
                        else:
                            pontos_vida_entidade = 0

                        print(f'Isso! {atacante} usou {t3_ataque} e acertou a fraqueza do adversário! A magia causou {dano_geral} de dano em {atacado} que agora tem {pontos_vida_entidade} de vida.')

                    else:
                        pontos_vida_entidade -= dano_geral

                        if pontos_vida_entidade >= 0:
                            pontos_vida_entidade = pontos_vida_entidade
                        else:
                            pontos_vida_entidade = 0

                        print(f'{atacante} usou {t3_ataque} e causou {dano_geral} de dano em {atacado} que agora tem {pontos_vida_entidade} de vida.')

                elif t3_ataque == 'Zio':
                    if resistencia_entidade == 'eletricidade':
                        dano_geral = int(0.5 * dano_geral)
                        pontos_vida_entidade -= dano_geral

                        if pontos_vida_entidade >= 0:
                            pontos_vida_entidade = pontos_vida_entidade
                        else:
                            pontos_vida_entidade = 0

                        print(f'{atacante} usou {t3_ataque}, mas acertou uma resistência, portanto causou apenas {dano_geral} de dano em {atacado} que agora tem {pontos_vida_entidade} de vida.')

                    elif fraqueza_entidade == 'eletricidade':
                        dano_geral = int(1.7 * dano_geral)
                        pontos_vida_entidade -= dano_geral
                        acerto_critico = atacado

                        if pontos_vida_entidade >= 0:
                            pontos_vida_entidade = pontos_vida_entidade
                        else:
                            pontos_vida_entidade = 0

                        print(f'Isso! {atacante} usou {t3_ataque} e acertou a fraqueza do adversário! A magia causou {dano_geral} de dano em {atacado} que agora tem {pontos_vida_entidade} de vida.')

                    else:
                        pontos_vida_entidade -= dano_geral

                        if pontos_vida_entidade >= 0:
                            pontos_vida_entidade = pontos_vida_entidade
                        else:
                            pontos_vida_entidade = 0

                        print(f'{atacante} usou {t3_ataque} e causou {dano_geral} de dano em {atacado} que agora tem {pontos_vida_entidade} de vida.')

            if pontos_vida_entidade == 0:
                turno = 0
                print('Vitória! Parece que o Nahobino São João reinará nesse solstício!')

            else:
                print('Ambos ainda sobrevivem. Melhor se retirar e derrotar entidades mais fracas para ficar mais forte…')
