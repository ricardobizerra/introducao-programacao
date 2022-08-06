piada = ''
piadas_encerradas = False
piada_boa = 0
piada_ruim = 0

while not piadas_encerradas:
    piada = input()

    if piada == 'Fim do Show!':
        piadas_encerradas = True
    else:
        reacao = input()

        if reacao == 'BAZINGA!':
            piada_boa += 1
        else:
            piada_ruim += 1

if piada_boa > 0.6 * (piada_boa + piada_ruim):
    print('BAZINGA! O senso de humor dele é muito bom, Amy, parece com o meu!')
elif piada_ruim > 0.6 * (piada_boa + piada_ruim):
    print('Amy, acredito que acabei de perder 60 de QI ouvindo essas piadas!')
else:
    print('Esse stand up foi bastante mediano, Amy. Parece a carreira do Leonard!')
