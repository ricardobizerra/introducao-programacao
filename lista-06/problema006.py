# funções que retornam a habilidade e o requisito baseado no talismã
def habilidade(tal, dicionario):
    return dicionario[tal][0]


def requisito(tal, dicionario):
    return dicionario[tal][1]


# dicionário dos amuletos
dicionario_amuletos = {
    'Carneiro': ('Adormecer', 'Imortalidade'),
    'Cao': ('Imortalidade', 'Forca descomunal'),
    'Cobra': ('Invisibilidade', 'Equilibrio espiritual'),
    'Coelho': ('Alta velocidade', 'Metamorfose Animal'),
    'Tigre': ('Equilibrio espiritual', 'Adormecer'),
    'Dragao': ('Fogo', 'Cura'),
    'Cavalo': ('Cura', 'Levitacao'),
    'Macaco': ('Metamorfose Animal', 'Raio laser'),
    'Galo': ('Levitacao', 'Animar objetos'),
    'Porco': ('Raio laser', 'Fogo'),
    'Rato': ('Animar objetos', 'Alta velocidade'),
    'Touro': ('Forca descomunal', 'Invisibilidade')
}

# talismãs do jackie
n = int(input())
talismas_jackie, habilidades_jackie = [], []

for i in range(n):
    talisma_jackie = input()
    talismas_jackie.append(talisma_jackie)
    habilidades_jackie.append(habilidade(talisma_jackie, dicionario_amuletos))

# talismãs do chefe
m = int(input())

todos_viloes_derrotados = True

for j in range(m):

    talisma_chefe = input()
    possui_requisito = False

    # conquistou talismã
    if requisito(talisma_chefe, dicionario_amuletos) in habilidades_jackie:

        possui_requisito = True

        talismas_jackie.append(talisma_chefe)
        habilidades_jackie.append(habilidade(talisma_chefe, dicionario_amuletos))

        print(f'Boa! O talisma do {talisma_chefe} vai ser nosso!')
    
    # não conquistou talismã
    else:

        # variável para verificar se todos foram derrotados
        todos_viloes_derrotados = False
        
        for item in dicionario_amuletos.items():

            if item[1][0] == requisito(talisma_chefe, dicionario_amuletos):
                talisma_requisito = item[0]

        print(f'Nao vai dar, melhor ir atras do talisma do {talisma_requisito} antes.')

# outputs finais
if todos_viloes_derrotados:
    print('Esse plano funciona, vamos agora!')

else:
    print('Que mau dia!! Melhor pensarmos num plano de fuga')
