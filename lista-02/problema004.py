num_planetas = int(input())

while num_planetas <= 1:
    print('Número inválido, tente novamente')
    num_planetas = int(input())

melhor_indice_hab = 0
melhor_nome = ''

for i in range(0, num_planetas):
    nome = input()
    raio = float(input())
    massa = float(input())
    temperatura = int(input())

    indice_hab = (raio + massa + (temperatura/288))/3

    if abs(indice_hab - 1) < abs(melhor_indice_hab - 1):
        melhor_nome = nome
        melhor_indice_hab = indice_hab
    else:
        melhor_nome = melhor_nome
        melhor_indice_hab = melhor_indice_hab

if melhor_indice_hab == 1:
    print(f'{melhor_nome} é perfeito!')
elif melhor_indice_hab < 1:
    print(f'{melhor_nome} vai dar pro gasto')
else:
    print(f'{melhor_nome} vai ter que servir')
