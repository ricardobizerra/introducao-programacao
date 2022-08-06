nome_doce1 = input()
quantidade1 = int(input())
nome_doce2 = input()
quantidade2 = int(input())
nome_doce3 = input()
quantidade3 = int(input())

faturamento_doce1 = quantidade1 * 2
faturamento_doce2 = quantidade2 * 5
faturamento_doce3 = quantidade3 * 3

if (quantidade1 == 0) and (quantidade2 == 0) and (quantidade3 == 0):
    print('A ideia foi peba! Acho melhor encontrar um novo jeito de ganhar dinheiro...')
else:
    if (faturamento_doce1 >= faturamento_doce2) and (faturamento_doce1 >= faturamento_doce3):
        faturamento = faturamento_doce1
        melhor_doce = nome_doce1
    elif (faturamento_doce2 > faturamento_doce3):
        faturamento = faturamento_doce2
        melhor_doce = nome_doce2
    elif (faturamento_doce3 >= faturamento_doce2):
        faturamento = faturamento_doce3
        melhor_doce = nome_doce3
    else:
        faturamento = faturamento_doce2
        melhor_doce = nome_doce2

    print(f'Oxe! Você ganhou {faturamento} reais vendendo {melhor_doce}. O povo gostou, visse?!')
