import time


def match_unico(rodada, lista_jogode3):
    print(f"Match: {rodada}")
    time.sleep(1.5)
    cartas_match = []
    for jogador_cartas in lista_jogode3:
        carta_numero = jogador_cartas[rodada]
        cartas_match.append(carta_numero)

        opcoes_carta = ["Pedra", "Papel", "Tesoura"]
        print(f"{jogador_cartas[0]} -----> carta: {opcoes_carta[carta_numero - 1]}")

    carta_ganhadora = verificar_carta_ganhadora(cartas_match)
    jogador_ganhador = ganhador_jogo(lista_jogode3, carta_ganhadora, rodada)
    return carta_ganhadora, jogador_ganhador


def verificar_carta_ganhadora(cartas_match):
    if 1 in cartas_match and 2 in cartas_match:
        carta_ganhadora = 2
    elif 1 in cartas_match and 3 in cartas_match:
        carta_ganhadora = 1
    elif 2 in cartas_match and 3 in cartas_match:
        carta_ganhadora = 3
    else:
        carta_ganhadora = 0
    return carta_ganhadora


def ganhador_jogo(lista_jogode3, carta_ganhadora, rodada):
    if lista_jogode3[0][rodada] == carta_ganhadora:
        jogador_ganhador = lista_jogode3[0][0]  # nome do primeiro jogador
    elif lista_jogode3[1][rodada] == carta_ganhadora:
        jogador_ganhador = lista_jogode3[1][0]  # nome do primeiro jogador
    else:
        jogador_ganhador = 0

    return jogador_ganhador


def tres_maches(lista_jogode3):
    carta_ganhadora, jogador_ganhador = match_unico(1, lista_jogode3)
    if jogador_ganhador != 0:
        vencedor = jogador_ganhador
    elif jogador_ganhador == 0:
        carta_ganhadora, jogador_ganhador = match_unico(2, lista_jogode3)
        if jogador_ganhador != 0:
            vencedor = jogador_ganhador
        elif jogador_ganhador == 0:
            carta_ganhadora, jogador_ganhador = match_unico(3, lista_jogode3)
    return jogador_ganhador
