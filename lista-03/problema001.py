suspeitos = input()

lista_suspeitos = suspeitos.split(',')

if len(lista_suspeitos) == 1:
    unico_suspeito = True
else:
    unico_suspeito = False

while unico_suspeito == False:

    entrada = input()

    if entrada == 'Não encontrei nada no primeiro suspeito':
        lista_suspeitos.pop(0)

    elif entrada == 'O último da lista está limpo':
        lista_suspeitos.pop(-1)

    elif entrada == 'Procurei por um elemento um pouco mais além na lista e ele está acima de qualquer suspeita':
        lista_suspeitos.pop(len(lista_suspeitos) // 2)

    elif entrada == 'Pelas minhas verificações, não encontrei nada de alarmante no indivíduo que está na seguinte posição:':
        indice = int(input())
        lista_suspeitos.pop(indice)

    elif entrada == 'Acho que temos mais uma opção a ser analisada…':
        novo_suspeito = input()
        lista_suspeitos.append(novo_suspeito)

    else:
        print('Isso não estava no combinado, a lista vai permanecer do mesmo jeito')

    if len(lista_suspeitos) == 1:
        unico_suspeito = True
    else:
        unico_suspeito = False

print(f'Acho que encontramos o suspeito. O seu nome é {lista_suspeitos[0]}, vamos salvar o Sam!')
