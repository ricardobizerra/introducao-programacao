# condicoes iniciais
temperatura = 30
fome = True
internet = 0

entrada = input()

while (entrada != 'ir para o grad') and (entrada != 'sair para a rua') and (entrada != 'comer uma quentinha') and (entrada != 'conectar no wifi') and (entrada != 'parar'):
    print('Entrada inválida')
    entrada = input()

while entrada != 'parar':
    if entrada == 'ir para o grad':
        temperatura -= 5
        internet += 300

    elif entrada == 'sair para a rua':
        temperatura += 5

    elif entrada == 'comer uma quentinha':
        fome = False

    elif entrada == 'conectar no wifi':
        internet += 100

    entrada = input()

    while (entrada != 'ir para o grad') and (entrada != 'sair para a rua') and (entrada != 'comer uma quentinha') and (entrada != 'conectar no wifi') and (entrada != 'parar'):
        print('Entrada inválida')
        entrada = input()

else:

    if temperatura >= 30:
        print('A temperatura aqui não está agradável')

    if temperatura <= 25:
        print('Agora sim, está aconchegante')

    if fome == True:
        print('Meu corpo precisa de comida')

    if internet < 100:
        print('Essa conexão está horrível')

    if fome == False and temperatura <= 25 and internet >= 300:
        print('Finalmente um lugar preciso para mim!')
