def match_unico(rodada, lista_jogode3):
    print(f"Match: {rodada}")
    cartas_match = []
    for jogador_cartas in lista_jogode3:
        carta_numero = jogador_cartas[rodada]
        cartas_match.append(carta_numero)

        opcoes_carta = ["Pedra", "Papel", "Tesoura"]
        print(f"{jogador_cartas[0]} -----> carta: {opcoes_carta[carta_numero - 1]}")

    if 1 in cartas_match and 2 in cartas_match:
        carta_ganhadora = 2
        if lista_jogode3[0][rodada] == carta_ganhadora:
            jogador_ganhador = lista_jogode3[0][0]  # nome do primeiro jogador
        else:
            jogador_ganhador = lista_jogode3[1][0]  # nome do segundo jogador
        return carta_ganhadora, jogador_ganhador

    elif 1 in cartas_match and 3 in cartas_match:
        carta_ganhadora = 1
        if lista_jogode3[0][rodada] == carta_ganhadora:
            jogador_ganhador = lista_jogode3[0][0]
        else:
            jogador_ganhador = lista_jogode3[1][0]
        return carta_ganhadora, jogador_ganhador

    elif 2 in cartas_match and 3 in cartas_match:
        carta_ganhadora = 3
        if lista_jogode3[0][rodada] == carta_ganhadora:
            jogador_ganhador = lista_jogode3[0][0]
        else:
            jogador_ganhador = lista_jogode3[1][0]
        return carta_ganhadora, jogador_ganhador
    else:
        return 0, 0


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
