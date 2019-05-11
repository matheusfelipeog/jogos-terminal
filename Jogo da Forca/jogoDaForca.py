# Importando metodo choice da lib random, que será responsável 
# por sortear e retornar um elemento de uma lista
from random import choice

# Importando modúlo que manipula o sistema
from os import system
system('cls||clear') # Método sendo usado para limpar a tela do prompt/terminal
                     # passando como parâmetro cls (Limpa no windows) e clear (linux) 

# Lista de palavras
listaPalavras = ['paralelepipedo', 'ferrari', 'papagaio', 'motocicleta',
                 'titanic', 'tsunami', 'terremoto', 'frança', 'brasil',
                 'europa', 'aniversario', 'python', 'caneta', 'lapiseira',
                 'aviao', 'metralhadora', 'velocidade', 'gorila', 'homem',
                 'mulher', 'infinito', 'coringa', 'batman', 'girafa',
                 'elefante', 'astronalta', 'programacao', 'computador']

# Sorteando uma palavra para ser adivinhada no jogo
palavraSecreta = choice(listaPalavras)

digitadas = []
acertos = []
erros = 0

# Loop infinito
while True:
    senha =  ''
    for letra in palavraSecreta:
        senha += letra if letra in acertos else '.'
    print('PALAVRA: ' + senha)

    # Verifica se a palavra secreta está correta, assim finalizando o game
    if senha == palavraSecreta:
        print('Parabéns, você acertou!!!')
        break
    
    # Solicitando uma letra como tentativa, e tratando-a para
    # ser minuscula e sem espaços no inicio e no fim
    tentativa = input('\nDigite uma letra: ').lower().strip()
    
    system('cls||clear')
    
    while True:
        # método isalpha está verificando se tem caracteres diferente de letras
        if len(tentativa) != 1 or tentativa.isalpha() == False:
            system('cls||clear')
            print('\nNÃO É PERMITIDO: MAIS DE UM DIGITO, DIGITOS ESPECIAIS, NÚMEROS OU ESPAÇOS.')
            print('TENTE NOVAMENTE!!!')
            tentativa = input('\nDigite uma letra: ').lower().strip()
        else:
            system('cls||clear')
            break

    
    # Verificando se a letra tentada já foi informada anteriormente
    if tentativa in digitadas:
        print('Você já tentou essa letra, tente nomente!!!')
        continue
    else:
        digitadas += tentativa
        if tentativa in palavraSecreta:
            acertos += tentativa
        else:
            erros += 1
            print('ERRROUU!!!')

    # Criando a estrutura da forca e o personagem, utilizando operador ternário
    print('X=======:=====\nX       :  ')
    print('''X
X      //\    
X     ///\\   
X    //. .\\  
X   //\_O_/\\ 
X   \/`|_|`\/ ''' if erros >= 1 else 'X')

    # Peito e braços
    linha2 = ''
    if erros == 2:
        linha2 = '''    _|----  
X    \___//   
X    /  ---    '''
    elif erros == 3:
        linha2 = '''    _|----\\
X    \___// \\
X    /  ---( \)'''
    elif erros >= 4:
        linha2 = '''   /_|----\\
X  //\___// \\
X (/ /  ---( \)'''
    print('X%s' % linha2)

    # Pernas
    linha3 = ''
    if erros == 5:
        linha3 += '''   /_______\
           
X            '''
    elif erros == 6:
        linha3 += '''   /_______\

X    |_|    
X   (__/'''

    elif erros >= 7:
        linha3 += '''   /_______\

X    |_| |_|
X   (__/ (__)'''
    print('X%s' % linha3)
    print('X\n================')
    # Quantidade máxima de erros atingida
    if erros == 7:
        print('VOCÊ FOI ENFORCADO')
        print('\nA PALAVRA SECRETA ERA: %s' % palavraSecreta)
        break


#Modélo do avatar da forca
#      //\
#     ///\\
#    //. .\\
#   //\_O_/\\
#   \/`|_|`\/
#   /_|----\\
#  //\___// \\
# (/ /  ---( \)
#   /_______\
#    |_| |_|
#   (__/ (__)
#
  

