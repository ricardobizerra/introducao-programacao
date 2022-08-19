# inicializando flags e listas de alunos e sintomas
aluno_com_sintomas = False
max_apareceu = False
max_na_lista = False
todos_alunos = []
alunos_todos_sintomas = []
alunos_todos_sintomas_sem_max = []

sintomas = ['dor de cabeca', 'insonia', 'pesadelos', 'suor frio', 'visoes']

entrada = input()

while entrada != 'descobrir':

    entrada = entrada.split(', ')

    nome = entrada[0]
    sintomas_nome = entrada[1:]

    sintomas_do_nome = []

    todos_alunos.append(nome)

    for s in sintomas_nome:
        s = s.replace('ç', 'c')
        s = s.replace('ô', 'o')
        s = s.replace('õ', 'o')
        sintomas_do_nome.append(s)

    if nome == 'Max':
        max_apareceu = True

    sintomas_em_comum = 0

    for sintoma in sintomas:

        i = 0

        while i < len(sintomas_do_nome):

            if sintoma == sintomas_do_nome[i]:
                sintomas_em_comum += 1
                break

            i += 1

    if sintomas_em_comum == len(sintomas):
        aluno_com_sintomas = True
        alunos_todos_sintomas.append(nome)

    entrada = input()

# verificando se max esta na lista de alunos com sintomas

for aluno in alunos_todos_sintomas:

    if aluno == 'Max':
        max_na_lista = True

# se max estiver na lista, cria nova lista de alunos com todos os sintomas, exceto max

alunos_todos_sintomas_sem_max = alunos_todos_sintomas.copy()

if max_na_lista:
    alunos_todos_sintomas_sem_max.remove('Max')

# condicionais de output

if not aluno_com_sintomas:
    print('Não conseguimos encontrar ninguém com esses sintomas, o próximo ataque do Vecna será imprevisível.')

n = len(alunos_todos_sintomas)

if max_na_lista:
    print("Oh não, Max está em perigo! Let's run up that hill com a Kate Bush e ajudar nossa amiga.")

    if n > 1:
        print(f'Além dela, tem mais {n - 1} pessoa(s) na mira do Vecna!')

if n > 0 and (not max_apareceu or not max_na_lista):
    print(f'Tem {n} pessoa(s) na mira do Vecna!')

if alunos_todos_sintomas_sem_max:

    if len(alunos_todos_sintomas_sem_max) == 1:
        print(f'Precisamos avisar {alunos_todos_sintomas_sem_max[0]} para preparar sua música favorita.')

    elif len(alunos_todos_sintomas_sem_max) > 1:

        nomes = ''

        for aluno in alunos_todos_sintomas_sem_max:

            if alunos_todos_sintomas_sem_max.index(aluno) < (len(alunos_todos_sintomas_sem_max) - 2):
                nomes = nomes + aluno + ', '

            elif aluno == alunos_todos_sintomas_sem_max[-2]:
                nomes = nomes + aluno + ' e '

            else:
                nomes = nomes + aluno

        print(f'Precisamos avisar {nomes} para prepararem suas músicas favoritas.')
