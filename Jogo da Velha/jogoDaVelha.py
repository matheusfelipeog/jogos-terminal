from os import system
system('cls||clear')

# Lista de posições
posicao = list(range(1, 10))

# rodada do jogo
rodada = 0

#jogador inicia com X
jogador = 'X'

# Loop do jogo
jogando = True
while True:
    # Tabuleiro do Jogo
    tabuleiro = f'{posicao[0]:^5}|{posicao[1]:^5}|{posicao[2]:^5}\n-----+-----+-----\n{posicao[3]:^5}|{posicao[4]:^5}|{posicao[5]:^5}\n-----+-----+-----\n{posicao[6]:^5}|{posicao[7]:^5}|{posicao[8]:^5}'
    print(tabuleiro)
    print()

    # Verifica se o jogo ja tem ganhador... Jogando igual a False: tem ganhador, caso contrário não
    if jogando == False:
        # Trocando o jogador em caso de vitoria, porque quando o loop retorna ao inicio ele é trocado
        jogador = 'O' if jogador == 'X' else 'X'
        print(f'VOTORIA DO JOGADOR: {jogador}')
        break

    # Verifica se o jogo empatou
    if rodada == 9:
        print('Empate')
        break

    # Jogador escolhendo uma posição
    print(f'VEZ DO JOGADOR: {jogador}')
    posiJogada = input('POSIÇÃO DESEJADA: ').strip()
    print()

    # Verificando se a string NÃO é um número
    if not(posiJogada.isdigit()):
        system('cls||clear')
        print('NÃO SÃO ACEITOS: LETRAS, ESPAÇOS OU CARACTERES ESPECIAIS')
        print('TENTE NOVAMENTE!!!')
        continue # Retornando ao inicio o loop
    else:
        # Convertendo a posição escolhida de STRING para INT e subtraindo 1
        posiJogada = int(posiJogada) - 1 

        # Verificando se a posição escolhida existe
        if not (0 <= posiJogada < 9):
            print('CASA NÃO EXISTE, TENTE NOVAMENTE.')
            continue # Retornando ao inicio o loop

    # Verificando se a casa escolhida está VAZIA
    if posicao[posiJogada] != 'X' and posicao[posiJogada] != 'O':

        system('cls||clear')
        # Marcando jogada na casa escolhida
        posicao[posiJogada] = jogador
        rodada += 1
    else:
        system('cls||clear')
        print('CASA OCUPADA, TENTE NOVAMENTE!!!\n')
        continue # Retornando ao inicio o loop

    # Alternando jogador
    jogador = 'O' if jogador == 'X' else 'X'

    # Verificando se tem vencedor na partida

    # vitoria em linha
    if 'X' == posicao[0] == posicao[1] == posicao[2] or 'O' == posicao[0] == posicao[1] == posicao[2]:
        jogando = False
    elif 'X' == posicao[3] == posicao[4] == posicao[5] or 'O' == posicao[3] == posicao[4] == posicao[5]:
        jogando = False
    elif 'X' == posicao[6] == posicao[7] == posicao[8] or 'O' == posicao[6] == posicao[7] == posicao[8]:
        jogando = False

    # vitoria em coluna
    if 'X' == posicao[0] == posicao[3] == posicao[6] or 'O' == posicao[0] == posicao[3] == posicao[6]:
        jogando = False
    elif 'X' == posicao[1] == posicao[4] == posicao[7] or 'O' == posicao[1] == posicao[4] == posicao[7]:
        jogando = False
    elif 'X' == posicao[2] == posicao[5] == posicao[8] or 'O' == posicao[2] == posicao[5] == posicao[8]:
        jogando = False

    # vitoria em diagonal
    if 'X' == posicao[0] == posicao[4] == posicao[8] or 'O' == posicao[0] == posicao[4] == posicao[8]:
        jogando = False
    elif 'X' == posicao[2] == posicao[4] == posicao[6] or 'O' == posicao[2] == posicao[4] == posicao[6]:
        jogando = False

