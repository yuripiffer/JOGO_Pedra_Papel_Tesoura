import random


class jogador:
    nome = ""
    lista_de_cartas = []

    def __init__(self, nome):
        self.nome = nome

        self.carta1 = random.randint(1, 3)
        self.carta2 = random.randint(1, 3)
        self.carta3 = random.randint(1, 3)


def gerar_lista_jogode3(jogador1, jogador2):
    lista_jogadores1 = [jogador1.nome, jogador1.carta1, jogador1.carta2, jogador1.carta3]
    lista_jogadores2 = [jogador2.nome, jogador2.carta2, jogador2.carta2, jogador2.carta3]
    lista_jogode3 = [lista_jogadores1, lista_jogadores2]
    return lista_jogode3


def instanciar_jogadores(nome_jogador1, nome_jogador2):
    jogador1 = jogador(nome_jogador1)
    jogador2 = jogador(nome_jogador2)
    lista_jogode3 = gerar_lista_jogode3(jogador1, jogador2)
    return jogador1, jogador2, lista_jogode3
