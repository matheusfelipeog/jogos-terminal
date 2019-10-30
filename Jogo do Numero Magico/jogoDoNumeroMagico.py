# Importando seletor aleatório em determinado intervalo
from random import randrange

# Importando modúlo que manipula o sistema
from os import system
system('cls||clear') # Método sendo usado para limpar a tela do prompt/terminal
                     # passando como parâmetro cls (Limpa no windows) e clear (linux) 

# Guarda numero aleatório
numeroMagico = randrange(1, 101)

# Número de tentativas restantes
numeroTentativas = 7

print('NÃO É PERMITIDO:\n- DIGITOS NÃO NÚMERICOS;\n- NÚMEROS OU ESPAÇOS.')
print('\nHumm... Eu pensei em um número de 1 a 100, você tem que adivinhar\n' +
      'ele em menos de 7 rodadas, está preparado?')

# Inicia o Jogo
while True:

    # Verifica se a quantidade de rodadas restantes acabou
    if (numeroTentativas == 0):
        print('Você perdeu!')
        break

    # Verifica se a tentativa inserida é válida
    while True:
        tentativa = input('\nDigite o número que você acha que é: ')

        if not tentativa.isdigit():
            print('NÃO É PERMITIDO:\n- DIGITOS NÃO NÚMERICOS;\n- NÚMEROS OU ESPAÇOS.\n')
        else:
            tentativa = int(tentativa)
            break
    
    # Jogar Vence
    if (tentativa == numeroMagico):
        print('Parabéns, você Venceu!!!')
        break
    
    # Número sugerido é muito baixo e diminui número de tentativas
    elif (tentativa < numeroMagico):
        print('Seu número é muito baixo.')
        numeroTentativas -= 1
    
    # Número sugerido é muito alto e diminui número de tentativas
    else:
        print('Seu número é muito alto.')
        numeroTentativas -= 1