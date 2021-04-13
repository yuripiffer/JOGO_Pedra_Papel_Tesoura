import modelJogador
import modelRodada


print("--------------------------------")
print("JO - QUEM - PÔ")
print("O famoso 'pedra - papel - tesoura'")
print("Bora para uma partida?!?!")
print("--------------------------------\n")

jogador1 = modelJogador.jogador(input("Nome do 1º jogador: "))
jogador2 = modelJogador.jogador(input("Nome do 2º Jogador: "))

lista_jogode3 = modelJogador.gerar_lista_jogode3(jogador1, jogador2)

modelRodada.rodar_round(lista_jogode3)


