import modelJogador
import modelRodada


print("--------------------------------".center(40))
print("\33[31mJÓ - KEM - PÔ\33[m".center(40))
print("O famoso 'pedra - papel - tesoura'".center(40))
print("\33[31mBora para uma partida?!?!\33[m".center(40))
print("--------------------------------\n".center(40))

# GERA OS JOGADORES COM SUAS CARTAS
nome_jogador1 = input("Nome do 1º jogador: ")
nome_jogador2 = input("Nome do 2º jogador: ")

# RODADAS
print("\nPRIMEIRA RODADA (ATÉ 3 MATCHES)")
# Instancia e cria novas cartas
jogador1 = modelJogador.jogador(nome_jogador1)
jogador2 = modelJogador.jogador(nome_jogador2)
lista_jogode3 = modelJogador.gerar_lista_jogode3(jogador1, jogador2)
r1_ganhador = modelRodada.tres_maches(lista_jogode3)
if r1_ganhador == 0:
    print("Sem ganhador no primeiro match de 3.\n")
else:
    print(f"O jogador ganhador do primeiro match de 3 foi: {r1_ganhador}")

print("\nSEGUNDA RODADA (ATÉ 3 MATCHES)")
# Instancia e cria novas cartas
jogador1 = modelJogador.jogador(nome_jogador1)
jogador2 = modelJogador.jogador(nome_jogador2)
lista_jogode3 = modelJogador.gerar_lista_jogode3(jogador1, jogador2)
r2_ganhador = modelRodada.tres_maches(lista_jogode3)
if r2_ganhador == 0:
    print("Sem ganhador no segundo match de 3.")
else:
    print(f"O jogador ganhador do segundo match de 3 foi: {r2_ganhador}")

print("\nTERCEIRA RODADA (ATÉ 3 MATCHES)")
# Instancia e cria novas cartas
jogador1 = modelJogador.jogador(nome_jogador1)
jogador2 = modelJogador.jogador(nome_jogador2)
lista_jogode3 = modelJogador.gerar_lista_jogode3(jogador1, jogador2)
r3_ganhador = modelRodada.tres_maches(lista_jogode3)
if r3_ganhador == 0:
    print("Sem ganhador no terceiro match de 3.")
else:
    print(f"O jogador ganhador do terceiro match de 3 foi: {r3_ganhador}")

r4_ganhador = '0'
if (r1_ganhador == 0) or (r2_ganhador == 0) or (r3_ganhador == 0) == True:
    while True:
        # Instancia e cria novas cartas
        jogador1 = modelJogador.jogador(nome_jogador1)
        jogador2 = modelJogador.jogador(nome_jogador2)
        lista_jogode3 = modelJogador.gerar_lista_jogode3(jogador1, jogador2)
        print("\nRODADA DE DESEMPATE")
        r4_ganhador = modelRodada.tres_maches(lista_jogode3)
        if r4_ganhador == 0:
            print("Sem ganhador no match de desempate. Vamos para mais uma!")
        else:
            print(f"O jogador ganhador do match de desempate foi: {r4_ganhador}")
            break


print('\n________________________________________________')
ganhadores = [r1_ganhador, r2_ganhador, r3_ganhador, r4_ganhador]
if 0 in ganhadores:
    ganhadores.remove(0)
print(f'THE WINNER IS: ---> {max(set(ganhadores))} <---')
print("Parabéns!!!!!")
print('________________________________________________')
