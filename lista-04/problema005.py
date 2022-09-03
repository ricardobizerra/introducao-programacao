# funções de cada serviço
def pedras_quentes(gorjeta_atual, tempo_expediente):
    gorjeta_servico = int((tempo_expediente + gorjeta_atual) / 2)

    return gorjeta_servico


def massagem_pes(gorjeta_atual):
    if gorjeta_atual % 2 == 0:
        gorjeta_servico = (gorjeta_atual % 7) * 6

    else:
        gorjeta_servico = (gorjeta_atual % 7) ** 2

    return gorjeta_servico


def servir_refeicao(gorjeta_atual):
    gorjeta_servico = 0

    if gorjeta_atual % 10 == 0:
        gorjeta_servico = 5

    else:

        while (gorjeta_atual - gorjeta_servico) % 10 != 0:
            gorjeta_servico += 1

    return gorjeta_servico


def massagem_completa(gorjeta_atual):
    dezena = gorjeta_atual // 10
    unidade = gorjeta_atual - (dezena * 10)

    gorjeta_servico = dezena + unidade

    return gorjeta_servico


# inicializando variáveis
gorjetas_chihiro = 10
duracao_expediente = 0

# loop de chamada dos serviços
while gorjetas_chihiro < 50 and duracao_expediente < 120:

    entrada = input()

    servico_valido = True

    if entrada == 'pedras':
        nome_servico = 'Pedras Quentes'
        gorjetas_chihiro += pedras_quentes(gorjetas_chihiro, duracao_expediente)
        duracao_expediente += 20

    elif entrada == 'pes':
        nome_servico = 'Massagem nos Pes'
        gorjetas_chihiro += massagem_pes(gorjetas_chihiro)
        duracao_expediente += 30

    elif entrada == 'refeicao':
        nome_servico = 'Servir Refeicao'
        gorjetas_chihiro += servir_refeicao(gorjetas_chihiro)
        duracao_expediente += 15

    elif entrada == 'completa':
        nome_servico = 'Massagem Completa'
        gorjetas_chihiro += massagem_completa(gorjetas_chihiro)
        duracao_expediente += 50

    else:
        nome_servico = ''
        duracao_expediente += 5

        servico_valido = False
        print(f'O cliente fez voce perder tempo, voce ainda possui {gorjetas_chihiro} gorjetas.')

    # se um dos 4 serviços foi realizado, imprime esta mensagem
    if servico_valido:
        print(f'Voce concluiu o servico de {nome_servico} e agora possui {gorjetas_chihiro} gorjetas.')

# outputs
if gorjetas_chihiro >= 50:
    print(f'Você acumulou {gorjetas_chihiro} gorjetas, com essa quantidade voce conseguira comprar sua passagem de saida e salvar seus pais.')

else:
    print('Voce nao conseguiu o minimo necessario para comprar a passagem de saida desse mundo e salvar seus pais.')
