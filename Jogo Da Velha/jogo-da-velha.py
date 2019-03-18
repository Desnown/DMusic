#!-*- coding: utf-8 -*-
#author: Desnown, 02/2019

'''
Levei em consideração as seguintes regras da Pep 8:
    •Use espaços em vez de tabulações para indentação.
    •Use quatro espaços para cada nível de indentação sintaticamente
        significativa.
    •As linhas devem ter 79 caracteres de comprimento, ou menos.
    •Em um arquivo, as funções e classes devem ser separadas por duas linhas
        em branco.
    • Coloque um – e apenas um – espaço antes e depois de uma atribuição de
variável.
'''

#OBS: O jogo ainda está um pouco "sujo", se quiser, pode edtitá-lo como bem entender

from os import system, name
from pdb import set_trace #DEBUGAR


def clear_output():
    '''
    Limpar Tela para que fique melhor a vizualiação
    '''
    if name == 'posix':
        system('clear')
    else:
        system('cls')


def display_board(tab):
    '''
    Função responsável por printar o jogo na tela
    '''
    clear_output()
    print(f'''
  {tab[0]} | {tab[1]} | {tab[2]}  
-------------
  {tab[3]} | {tab[4]} | {tab[5]}  
-------------
  {tab[6]} | {tab[7]} | {tab[8]} 
''')


def player_input():
    '''
    Função responsável por solicitar "X" ou "O" do primeiro player.
    OBS: o player 2 ficará com a letra que o player 1 não quis(óbvio).
    '''
    market = ''
    while market is not ('X' or 'O'):
        market = input('Player 1, qual você prefere, X ou O\n>: ').upper()

        if market == "X":
            return ('X', 'O')
        elif market == 'O':
            return ('O', 'X')
        else:
            continue


def place_marker(tab,marker, position):
    '''
    Função que "carimba" o símbolo no lugar que o player pediu
    '''
    # set_trace() #DEBUG
    if tab[position-1] == ' ':
        tab[position-1] = marker


def win_check(tab, mark):
    '''
    Função responsável por verificar se o player que acabou de jogar
    ganhou a partida.
    '''
    return ((tab[0] == mark and tab[1] == mark and tab[2] == mark)  or
            (tab[3] == mark and tab[4] == mark and tab[5] == mark)  or
            (tab[6] == mark and tab[7] == mark and tab[8] == mark)  or
            # ->> Horizontal

            (tab[0] == mark and tab[3] == mark and tab[6] == mark)  or
            (tab[1] == mark and tab[4] == mark and tab[7] == mark)  or
            (tab[2] == mark and tab[5] == mark and tab[8] == mark)  or
            # ->> Vertical

            (tab[0] == mark and tab[4] == mark and tab[8] == mark)  or
            (tab[2] == mark and tab[4] == mark and tab[6] == mark)
            # ->> Diagonal
            )


def space_check(tab, position):
    '''
    Retorna um valor booleano(True) caso a posição requisitada esteja vazia
    '''
    return tab[position-1] == ' '


def full_board_check(tab):
    for i in range(0,10):
        if space_check(tab, i):
            return False
    return True


def player_choice(tab, jog):
    '''
    Escolher a posição onde o usuário quer jogar.
    '''
    pos = 10
    # set_trace()
    while True:
        try:
            pos = int(input(f"{jog}, qual posição que você deseja(1-9)\n>: "))
            if pos in range(1,10):
                if not space_check(tab, pos):
                    print("\n\nPOSIÇÃO OCUPADA")
                else:
                    return pos
        except Exception:
                print('Número, viado!!!')


def print_points(pontos_jogadores):
    #printa os pontos dos jogadores do jogo
    print(f'''+----------------+
|  Player 1 : {pontos_jogadores["Player 1"]}  |
+----------------+
|  Player 2 : {pontos_jogadores["Player 2"]}  |
+----------------+\n''')


def replay():
    '''
    Função responsável por solicitação de um novo jogo, ou não
    '''

    #OBS: Obedecendo a PEP 8 de no máximo 79 caracteres de comprimento
    return input('''Vocês desejam jogar novamente? "SIM" ou "NÃO"
>: ''').upper().startswith('S'),clear_output()


#Limpar tela
clear_output()
#Guardar os pontos de cada um
pontos = {'Player 1': 0, 'Player 2': 0}
print("Bem Vindo ao jogo da velha!")

while True:
    tabuleiro = [' '] * 9
    player1_marker, player2_marker = player_input()
    #Mantem o jogo percorrendo
    game_on = True
    jogador = 'Player 1'
    #Marcador do jogador( X ou O )
    marker = ''

    while game_on:
        #printa o jogo/tabuleiro
        display_board(tabuleiro)
        if jogador == 'Player 1':
            # set_trace() #DEBUG
            position = player_choice(tabuleiro, jogador)
            place_marker(tabuleiro,player1_marker, position)

        else:
            position = player_choice(tabuleiro, jogador)
            place_marker(tabuleiro,player2_marker, position)

        if win_check(tabuleiro, marker):
            display_board(tabuleiro)
            print(f"\n{jogador.upper()} GANHOU!!!")
            # set_trace()
            pontos[jogador]+=1
            print_points(pontos)
            game_on = False

        else:
            if full_board_check(tabuleiro):
                display_board(tabuleiro)
                print("DEU VELHA!")
                break
        # contador +=1

        if jogador == 'Player 1':
            jogador = 'Player 2'
            marker = player2_marker
        else:
            jogador = 'Player 1'
            marker = player1_marker


    if not replay()[0]:
        break