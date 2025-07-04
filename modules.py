'''
Arquivo de funções utilizadas
2025.06.25
Rodrigo Lima dos Santos Batista
'''

# OBJETIVO : Criar um  arquivo de funções que serão utilizadas em nossos projetos

# BIBLIOTECAS
from random import randint # importa a função randint da bibliotca random
import random
#CONSTANTES
TAM = int(50) # Tamanho da tela
MAR = int(2) # Margem da mensagem na tela
CAR = '-' # Caractere utilizado para desenhar a linha


# FUNÇÕES

# função para limpar a tela(fingir)
def limpaTela():
    print('\n'*TAM)     # Mostra na tela TAM(50) linhas em branco (\n)

# Função para desenhar uma linha
def mostraline():
    print(f'{CAR}'*TAM)     # Mostra na tela TAM(50) caracteres '-'

 # Função ppara mostrar uma msg centralizada
def msgCenter (msg):
    print(f'{CAR}{msg:^{TAM-MAR-MAR}} {CAR}')   # Mostra na tela o valor do parametro msg Centralizado entre TAM(50)-MAR(2)-MAR(2)

# Função para mostrar uma msg a esquerda
def msgLeft(msg):
    print(f'{CAR} {msg:<{TAM-MAR-MAR}} {CAR}')  # Mostra na tela o valor do parametro msg a esquerda entre TAM(50)-MAR(2)-MAR(2)

# Função para mostrar cabeçalho
def mostrarCabecalho(MSGS):
    mostraline()    # Chama a função que mostra a linha
    for msg in MSGS:    # Itera sobre a lista MSGS
        msgCenter(msg)  # Chama a função que mostra a mensagem centralizada
    mostraline()    # Chama a função que mostra a linha


# Função para mostrar menu
def mostraMenu(MSGS):
    mostraline()    # Chama a função que mostra a linha
    for msg in MSGS:    # Itera sobre a lista MSGS
        msgLeft(msg)    # Chama a função que mostra a mensagem a esquerda 
    mostraline()    # Chama a função que mostra a linha

# Função para sortear um número
def sortNum(limite):
    key = randint(1, limite)    # Usa a Função randint para sortear um número
    return key      # Retorna o número sorteado

# Função para validar as entradas 
def validaValue(resp, opcoes):
    if resp in opcoes:
        return True
    else:
        MSGS= [f'{resp} não é uma opção válida!',
               f'Escolha entre {opcoes}']
        mostraMenu(MSGS)
        return False
    
# Funçao pega e valida valores
def getValue(msg):
    resp = input(f'{CAR} {msg}: ').strip()
    return resp

# Mostra dica == verificar se a resposta é Maior ou Menor que o Número Sorteado
def mostraDica(resp, key):  
    if resp > key:
        mostrarCabecalho(['Tente um número menor!'])
    else:
        mostrarCabecalho(['Tente um número maior!'])

#função para perguntar
def playAgain():
    opcoes = ['1', '0']
    mostrarCabecalho(['Deseja jogar novamente?', '[1] Sim', '[0] Não'])
    resp = getValue('Escolha uma opção')
    return resp == '1'

# Tipos
listaPokeA = ['Blastoise', 'Empoleon', 'Kyogre', 'Swampert']           # Lista dos pokenpôs de Água
listaPokeF = ['Charizard', 'Typhlosion', 'Blaziken', 'Talonflame']      # Lista dos pokenpôs de Fogo
listaPokeG = ['Venusaur', 'Sceptile', 'Torterra', 'Kartana']            # Lista dos pokenpôs de Grama
listaPokeT = ['Sandslash', 'Groudon', 'Garchomp', 'Krookodile']         # Lista dos pokenpôs de Terra
listaPokeE = ['Pikachu', 'Zapdos', 'Zekrom', 'Luxray']                  # Lista dos pokenpôs de Elétrico
Poke = ''
def tipos(resp):
    if resp == 1:
        mostraMenu(['[1] Blastoise', '[2] Empoleon', '[3] Kyogre', '[4] Swampert'])
    elif resp == 2:
        mostraMenu(['[1] Charizard', '[2] Typhlosion', '[3] Blaziken', '[4] Talonflame'])
    elif resp == 3:
        mostraMenu(['[1] Venusaur', '[2] Sceptile', '[3] Torterra', '[4] Kartana'])
    elif resp == 4:
        mostraMenu(['[1] Sandslash', '[2] Groudon', '[3] Garchomp', '[4] Krookodile'])
    elif resp == 5:
        mostraMenu(['[1] Pikachu', '[2] Zapdos', '[3] Zekrom', '[4] Luxray'])

