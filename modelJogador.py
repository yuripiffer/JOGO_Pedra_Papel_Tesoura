import random


class jogador:
    nome = ""
    lista_de_cartas = []

    def __init__(self, nome):
        self.nome = nome

        lista_de_cartas = list()
        lista_de_cartas.append(random.randint(1, 3))
        lista_de_cartas.append(random.randint(1, 3))
        lista_de_cartas.append(random.randint(1, 3))
        self.lista_de_cartas = lista_de_cartas


def gerar_lista_jogode3(jogador1, jogador2):
    lista_jogode3 = [['', 0, 0, 0], ['', 0, 0, 0]]
    lista_jogode3[0][0] = jogador1.nome
    lista_jogode3[0][1] = jogador1.lista_de_cartas[0]
    lista_jogode3[0][2] = jogador1.lista_de_cartas[1]
    lista_jogode3[0][3] = jogador1.lista_de_cartas[2]

    lista_jogode3[1][0] = jogador2.nome
    lista_jogode3[1][1] = jogador2.lista_de_cartas[0]
    lista_jogode3[1][2] = jogador2.lista_de_cartas[1]
    lista_jogode3[1][3] = jogador2.lista_de_cartas[2]
    return lista_jogode3
