import modelJogador
import modelRodada
import time

print(("-" * 40).center(40))
print("\33[31mJÓ - KEM - PÔ\33[m".center(42))
print("O famoso 'pedra - papel - tesoura'".center(40))
print("\33[31mBora para uma partida?!?!\33[m".center(42))
print(("-" * 40).center(40))

# IMPUT DO NOME DOS JOGADORES
nome_jogador1 = input("Nome do 1º jogador: ")
nome_jogador2 = input("Nome do 2º jogador: ")

# CHAMA AS 3 RODADAS
ganhadores_por_rodada = []
for i in range(1, 4):
    print(f"\n{i}ª RODADA (ATÉ 3 MATCHES)")
    time.sleep(1.5)
    jogador1, jogador2, lista_jogode3 = modelJogador.instanciar_jogadores(nome_jogador1, nome_jogador2)
    ganhador = modelRodada.tres_maches(lista_jogode3)
    if ganhador == 0:
        print("Sem ganhador no primeiro match de 3.\n")
    else:
        print(f"O jogador ganhador do primeiro match de 3 foi: {ganhador}")
    ganhadores_por_rodada.append(ganhador)

# CHAMA A RODAD EM CASO DE EMPATE
if 0 in ganhadores_por_rodada:
    time.sleep(1.5)
    while True:
        print("\nRODADA DE DESEMPATE")
        jogador1, jogador2, lista_jogode3 = modelJogador.instanciar_jogadores(nome_jogador1, nome_jogador2)
        ganhador = modelRodada.tres_maches(lista_jogode3)
        if ganhador == 0:
            print("Sem ganhador no match de desempate. Vamos para mais uma!")
        else:
            print(f"O jogador ganhador do match de desempate foi: {ganhador}")
            ganhadores_por_rodada.append(ganhador)
            break

# PRINTA O GANHADOR GERAL
if 0 in ganhadores_por_rodada:
    ganhadores_por_rodada.remove(0)
print('\n')
print(('_' * 42).center(40))
print(f'\33[31mTHE WINNER IS: ---> {max(set(ganhadores_por_rodada))} <---'.center(40))
print("Parabéns!!!!!\33[m".center(40))
print(('_' * 42).center(40))
