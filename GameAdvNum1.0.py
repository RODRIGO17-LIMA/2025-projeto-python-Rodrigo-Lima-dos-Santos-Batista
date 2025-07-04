'''
Projeto: Game Adivinhe o Numero - V.1.0
2025.06.23
Rodrigo Lima dos Santos Batista
'''
# Objetivo: Desenvolve um Jogo, onde o Computador sorteia 1 número 1 a 10, o Jogador tera 3 chances para adivinhar com o Jogo fornecendo dicas

# Espaço reservado ´para adeclaração das bibliotecas e funções
from random import randint    # Importa a função randint da biblioteca random 
from time import sleep      # Importa a função sleep da biblioteca time
from modules import limpaTela, mostraline, msgLeft, mostrarCabecalho, mostraMenu, sortNum, validaValue, getValue, mostraDica, playAgain

# CONSTANTES --> 
TAM = int(50)   # Tamanho da Tela
MAR = int(2)    # Margem da mensagem na Tela

#Espaço reservado para declaração de variaveis
key = 0     # Variável que guarda o número sorteado
resp = 0    # Variável que guarda a resposta do Jogador
vidas = 3   # Variável que guarda o número de vidas do Jogador
limite = 0  # Variável que guarda o número máximo do sorteio
tentativas = 0  # Variável que guarda o número de tentativas do Jogador
msg = ''    # Variável que guarda a mensagem

# Listas 
MSGS = []   # Lista que irá guardar as mensagens
# Lista que guarda msgs do cabeçalho
msgsCab = ['JOGO DO ADIVINHE O NÚMERO',
           'Desenvolvido por Rodrigo L. dos S. Batista']
# Lista que guarda msgs do menu de níveis de dificuldade
msgsLevel = ['NÍVEIS DE DIFICULDADE',
             '[1] Fácil (1 a 10)',
             '[2] Difícil (1 a 100)',
             '[3] Impossível (1 a 1000)',
             'Escolha o nível de dificuldade:']
# FUNÇÕES DO PROJETO --> Espaço reservado para declaração das funções do projeto

# Função principal 
def playGame():
    global key, resp, vidas, limite, tentativas, MSGS
    limpaTela()     # Limpa Tela
    mostrarCabecalho(msgsCab)   # Mostra o Cabeçalho do Jogo
    mostraMenu(msgsLevel)   # Mostra o Menu de Níveis de Dificuldade
    msg = '-> Digite o número correspondente ao nível'
    resp = getValue(msg)
    opcoes = ['1', '2', '3']
    while not validaValue(resp, opcoes):
        resp = getValue(msg)

    # Verificar nivel do usuario
    if resp == '1':     # Facil
        vidas = 3
        limite = 10
    elif resp == '2':   #Dificil
        vidas = 5
        limite = 100
    elif resp == '3':   # Impossivel
        vidas = 10
        limite = 1000

    # Chama Função que Sorteia um Número
    key = sortNum(limite)

    limpaTela()     # Limpa a tela antes de iniciar o jogo
    sleep(1)        # Pausa de 1 segundo para criar expectativa
    mostrarCabecalho(msgsCab)   # Mostra o Cabeçalho do Jogo
    mostrarCabecalho([f'Adivinhe o número entre 1 e {limite}', f'Você tem {vidas} tentativas'])     # Exibe instruções

    #Loop de tentativas
    for tentativa in range(vidas):
        msg = f'Tentativa {tentativa+1}/{vidas} -> Seu palpite'
        resp = getValue(msg)

        # Validação de entrada numerica
        while not resp.isdigit():
            mostrarCabecalho(['Entrada inválida! Por favor, insira um número'])
            resp = getValue(msg)

        resp = int(resp)

        # Verificar se o palpite é correto
        if resp == key:
            sleep(1)
            mostrarCabecalho(['Parabéns!!!', 'Você acertou o número!'])
            break
        else:
            if tentativa < vidas - 1:
                # Dica se o jogador ainda tiver tentativas
                sleep(1)
                mostrarCabecalho(['Número incorreto!',
                                  f'Você ainda tem {vidas - tentativa - 1} tentativas'])
                mostraDica(resp, key)
    else:
        # Mensagem de derrota se o jogador não acertar o número
        sleep(1)
        mostrarCabecalho(['Que pena...', f'O número secreto era {key}', 'Fim de jogo!'])
    
    # Pergunta se o jogador deseja jogar novamente
    if playAgain():
        playGame()
    else:
        # Mensagem de despedida
        mostrarCabecalho(['Obrigado por jogar!', 'Até a próxima!'])
# Início do Jogo
playGame()  # Chama a função principal para iniciar o jogo