'''
Game PokenPô
2025.07.02
Rodrigo Lima dos Santos Batista
'''

# OBJETIVO: Desenvolver um Jogo onde o Jogador escolhe um pokemon de um elemento especifico, e tenta ganhar do PC que escolhe outro elemento aleatório

# BIBLIOTECA
from modules import limpaTela, mostrarCabecalho, mostraMenu, getValue, validaValue, sortNum, playAgain, tipos       # Importa funções de 'modules', cada uma faz uma coisa diferente
from time import sleep      # Importa função de esperar um determinado tempo
import random       # Permite usar funções de sorteio de elementos
# VARIÁVEIS
msg = ''        # Transforma a variavel 'msg' em string para não haver falhas durante a ativação de outros códigos
resp = ''       # Transforma a variavel 'resp' em string para não haver falhas durante a ativação de outros códigos
PcjogadaPokemon = ''        # Transforma a variavel 'PcjogadaPokemon' em string para não haver falhas durante a ativação de outros códigos
Poke = ''       # Transforma a variavel 'Poke' em string para não haver falhas durante a ativação de outros códigos
userElemento = 0
userPokemon = 0
# LISTAS
msgsCab = ['JOGO POKENPÔ', 'Desenvolvido por Rodrigo L. dos S. Batista']        # Lista com msg de cabeçalho
msgsMenu = ['Escolha um elemento']        # Lista de msg para dar opções de escolha de elemento
listaelementos = ['Água', 'Fogo', 'Grama', 'Terra', 'Elétrico']         # Lista dos elementos
listaPokeA = ['Blastoise', 'Empoleon', 'Kyogre', 'Swampert']           # Lista dos pokenpôs de Água
listaPokeF = ['Charizard', 'Typhlosion', 'Blaziken', 'Talonflame']      # Lista dos pokenpôs de Fogo
listaPokeG = ['Venusaur', 'Sceptile', 'Torterra', 'Kartana']            # Lista dos pokenpôs de Grama
listaPokeT = ['Sandslash', 'Groudon', 'Garchomp', 'Krookodile']         # Lista dos pokenpôs de Terra
listaPokeE = ['Pikachu', 'Zapdos', 'Zekrom', 'Luxray']                  # Lista dos pokenpôs de Elétrico
listaC = ['Água', ['Blastoise', 'Empoleon', 'Kyogre', 'Swampert'], 
          'Fogo', ['Charizard', 'Typhlosion', 'Blaziken', 'Talonflame'], 
          'Grama', ['Venusaur', 'Sceptile', 'Torterra', 'Kartana'],
          'Terra', ['Sandslash', 'Groudon', 'Garchomp', 'Krookodile'],
          'Elétrico', ['Pikachu', 'Zapdos', 'Zekrom', 'Luxray']]



# FUNÇÃO PRINCIPAL DO JOGO
def playGame():
    limpaTela()         # Limpa a tela(Pulando 50 linhas) para iniciar o game
    mostrarCabecalho(msgsCab)       # Mostra a msg do cabeçalho
    mostraMenu(msgsMenu)        # Mostra msg do menu
    mostraMenu(listaelementos)
    msg = '-> Digite o número de um elemento'       # Espaço para pedir para o jogador digitar
    resp = getValue(msg)    # Serve como entrada para o usuario
    opcoes = ['1', '2', '3', '4', '5']      # Variavel usada para mostrar quais digitos o usuario deve usar
    while not validaValue(resp, opcoes):        # Verifica se a entrada do usario é compativel com a variavel opcoes
        resp = getValue(msg)    
        
    sleep(1)        # Cria um intervalo de tempo antes dos próximos códigos serem ativados
    limpaTela()     # Limpa a tela(Pulando 50 linhas) para iniciar o game
    userElemento = int(resp)    # Transforma a variavel resp em um inteiro
    tipos(userElemento)         # Uma função para mostrar uma lista de opções de de pokenpôs de acordo com o elemento que o usuario escolheu 
    msg = '-> Digite o número de um pokenpô'    # variavel com msg que pede para o usuario digitar um numero
    resp = getValue(msg)        # Serve como entrada para o usuario
    opcoes = ['1', '2', '3', '4']       # Lista de quais numeros o usuario pode usar
    while not validaValue(resp, opcoes):        # Valida se a resposta do usuario é compativel com as opções da lista 'opcoes'
        resp = getValue(msg)        # Da opção para o usario digitar novamente 
    
    userPokemon = int(resp)
    sleep(1)        # Cria um intervalo de tempo antes dos próximos códigos serem ativados
    limpaTela()     # Limpa a tela(Pulando 50 linhas) para iniciar o game
    PcjogadaElemento = random.randint(1,5)        # Seleciona um elemento aleatorio(Da 'listaelementos') para o Pc
    if PcjogadaElemento == 1:                          # Caso a lista sorteada seja 'Água' sera sorteado um pokemon da 'listaPokeA'
        PcjogadaPokemon = random.choice(listaPokeA)
    elif PcjogadaElemento == 2:                        # Caso a lista sorteada seja 'Fogo' sera sorteado um pokemon da 'listaPokeF'
        PcjogadaPokemon = random.choice(listaPokeF)
    elif PcjogadaElemento == 3:                       # Caso a lista sorteada seja 'Grama' sera sorteado um pokemon da 'listaPokeG'
        PcjogadaPokemon = random.choice(listaPokeG)
    elif PcjogadaElemento == 4:                       # Caso a lista sorteada seja 'Terra' sera sorteado um pokemon da 'listaPokeT'
        PcjogadaPokemon = random.choice(listaPokeT)
    elif PcjogadaElemento == 5:                    # Caso a lista sorteada seja 'Elétrico' sera sorteado um pokemon da 'listaPokeE'
        PcjogadaPokemon = random.choice(listaPokeE)


# Verificando o vencedor
    if ( (userElemento == PcjogadaElemento) or
        (userElemento == 2 and PcjogadaElemento == 5) or
        (userElemento == 3 and PcjogadaElemento == 5)):     # Verifica se vai ocerrer um empate se (Usario escolher Fogo e o Pc Elétrico, ou se o usuario escolher Grama e o Pc Elétrico, ou caso os dois escolham o mesmo elemento)
        sleep(1)        # Cria um intervalo de tempo antes dos próximos códigos serem ativados
        mostrarCabecalho([f"{listaC[userElemento][userPokemon-1]} e {PcjogadaPokemon} se anularam", 'Empate'])       # Mostra a msg de empate
    elif( (userElemento == 1 and PcjogadaElemento == 3) or 
         (userElemento == 1 and PcjogadaElemento == 4) or
         (userElemento == 2 and PcjogadaElemento == 3) or 
         (userElemento == 3 and PcjogadaElemento == 4) or 
         (userElemento == 4 and PcjogadaElemento == 5) or 
         (userElemento == 4 and PcjogadaElemento == 2) or 
         (userElemento == 5 and PcjogadaElemento == 1) or 
         (userElemento == 3 and PcjogadaElemento == 1)):         # Verifica se vai ocerrer uma vitoria para o jogador se (o usuario escolher Fogo e o Pc Grama, ou se escolher Grama e o Pc Terra, ou se escolher Terra e o Pc Elétrico, ou se escolher Elétrico e o Pc Água, ou se escolher Água e o Pc Fogo, ou se escolher Terra e o Pc Fogo, ou se escolher Água e o Pc Terra, ou se escolher Grama e o Pc Água)
        mostrarCabecalho([f'{listaC[userElemento][userPokemon-1]} ganhou de {PcjogadaPokemon}', 'You WIN'])      # Mostra a msg de que o Usuario ganhou do Pc
          # Verifica se vai ocerrer um empate se (Usario escolher Fogo e o Pc Elétrico, ou se o usuario escolher Grama e o Pc Elétrico, ou caso os dois escolham o mesmo elemento)
    else:       # Caso o nenhuma das condições do if e elif não seja atendida o Pc vence 
       sleep(1)         # Cria um intervalo de tempo antes dos próximos códigos serem ativados
       mostrarCabecalho([f"{PcjogadaPokemon} ganhou de {listaC[userElemento][userPokemon-1]}", 'You Lose'])     # Mostra a msg Pc ganhou do usuario
    
    if playAgain():     # Pergunta se o usuario quer jogar novamente
        sleep(1)        # Cria um intervalo de tempo antes dos próximos códigos serem ativados
        playGame()
    else:       # Caso não o sistema agrade por ter jogado
        mostrarCabecalho(['Obrigado por jogar!', 'Até a próxima!'])
playGame()