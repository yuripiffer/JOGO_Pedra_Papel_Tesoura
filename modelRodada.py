import time


def match(rodada, lista_jogode3):
    """
    Função que roda a match.
    Utiliza a lista_jogode3 para saber os jogadores e suas cartas,
    Printa as cartas dos jogadores,
    retorna a carta ganhadora.

    Cartas
    1 - equivalente a Pedra
    2 - equivalente a Papel
    3 - equivalente a tesoura

    :param rodada: int: parâmetro se é a rodada 1, 2 ou 3
    :return: valor da carta ganhadora (1,2,3) ou 0 para nenhum vencedor
    """
    print(f"Rodada: {rodada}")
    cartas_match = []
    for jogador_cartas in lista_jogode3:
        carta_numero = jogador_cartas[rodada]
        cartas_match.append(carta_numero)

        elemento_do_numero = ["Pedra", "Papel", "Tesoura"]
        print(f"{jogador_cartas[0]}, carta: {elemento_do_numero[carta_numero - 1]}")

    if 1 in cartas_match and 2 in cartas_match:
        return 1
    elif 1 in cartas_match and 3 in cartas_match:
        return 3
    elif 2 in cartas_match and 3 in cartas_match:
        return 2
    else:
        return 0


def rodar_round(lista_jogode3):
    time.sleep(1)
    vencedor = 0
    resultado_1 = match(1, lista_jogode3)
    if resultado_1 != 0:
        vencedor = resultado_1
        if lista_jogode3[0][1] == resultado_1:
            print(f"Quem ganhou foi: {lista_jogode3[0][0]}")
        else:
            print(f"Quem ganhou foi: {lista_jogode3[1][0]}")
    else:
        print("Sem vencedor ainda.\n")

    if vencedor == 0:
        time.sleep(1)
        resultado_2 = match(2, lista_jogode3)
        if resultado_2 != 0:
            vencedor = resultado_2
            if lista_jogode3[0][2] == resultado_1:
                print(f"Quem ganhou foi: {lista_jogode3[0][0]}")
            else:
                print(f"Quem ganhou foi: {lista_jogode3[1][0]}")
        else:
            print("Sem vencedor ainda.\n")

    if vencedor == 0:
        time.sleep(1)
        resultado_3 = match(3, lista_jogode3)
        if resultado_3 != 0:
            vencedor = resultado_3
            if lista_jogode3[0][3] == resultado_1:
                print(f"Quem ganhou foi: {lista_jogode3[0][0]}")
            else:
                print(f"Quem ganhou foi: {lista_jogode3[1][0]}")
        else:
            print("Sem vencedor ainda.\n")

    if vencedor == 0:
        print("Não houve ninguém ganhador nesse jogo :(")
