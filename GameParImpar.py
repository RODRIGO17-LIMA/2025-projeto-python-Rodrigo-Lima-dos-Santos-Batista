'''
Game Par ou Ímpar V.1.0
2025.06.25
Rodrigo Lima dos Santos Batista
'''

# OBJETIVO: Desenvolver um Jogo onde o Jogador escolhe Par ou Ímpar e faz sua Jogada, o PC sorteia um Número entre 1 e 0 e soma com a Jogada do Jogador, se o resultado for Par, ele ganha se for Ímpar e o Jogador escolheu Ímpar, ele ganha, caso contrário o PC ganha

# BIBLIOTECA
from modules import limpaTela, mostrarCabecalho, mostraMenu, getValue, validaValue, sortNum, playAgain 

# CONSTANTE
limite = 10     # Limite do Sorteio (1 a 10)

# VARIÁVEIS
escolha = ''    # Variável que guarda a escolha do Jogador (Par ou Ímpar)
msg = ''        # Variável que guarda a mensagem

# LISTAS
msgsCab = ['JOGO PAR OU ÍMPAR', 'Desenvolvido por Rodrigo L. dos S. Batista']
msgsMenu = ['Escolha', '[0] para Par', '[1] para Ímpar']

# FUNÇÃO PRINCIPAL DO JOGO
def playGame():
    limpaTela()
    mostrarCabecalho(msgsCab)   # Mostra o Cabeçalho do Jogo
    mostraMenu(msgsMenu)
    msg = '-> Sua escolha: '
    escolha = getValue(msg)
    opcoes = ['0', '1']
    while not validaValue(escolha, opcoes):
        escolha = getValue(msg)
    msg = '-> Sua Jogada: '
    userJogada = getValue(msg)  
    while not userJogada.isdigit:
        userJogada = getValue(msg)
    userJogada = int(userJogada)    # Converte a Jogada do Jogador para inteiro
    pcJogada = sortNum(limite)  # Sorteia um número entre 1 e 10 para o PC
    result = userJogada + pcJogada  # Soma a Jogada do Jogador com a Jogada do PC
    if (result%2 == 0) and escolha =='0':
        ganhador = 'Jogador'
    elif(result%2 != 0) and escolha =='1':
        ganhador = 'Jogador'
    else:
        ganhador = 'PC'
    MSGS = [f'PC Jogou: {pcJogada}', f'Jogador Jogou: {userJogada}', f'Resultado: {result}', f'Ganhador: {ganhador}']

    mostrarCabecalho(MSGS)  # Mostra o resultado do Jogo
    # Pergunta se o jogador deseja jogar novamente
    if playAgain():
        playGame()
    else:
        # Mensagem de despedida
        mostrarCabecalho(['Obrigado por Jogar!', 'Até a próxima!'])
    
# CÓDIGO PRINCIPAL
playGame() # Chama função principal do Jogo