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
    lista_jogode3 = [['', 0, 0, 0], ['', 0, 0, 0]]
    lista_jogode3[0][0] = jogador1.nome
    lista_jogode3[0][1] = jogador1.carta1
    lista_jogode3[0][2] = jogador1.carta2
    lista_jogode3[0][3] = jogador1.carta3

    lista_jogode3[1][0] = jogador2.nome
    lista_jogode3[1][1] = jogador2.carta1
    lista_jogode3[1][2] = jogador2.carta2
    lista_jogode3[1][3] = jogador2.carta3
    return lista_jogode3
