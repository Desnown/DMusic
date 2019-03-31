#! -*- coding: utf-8 -*-
__author__ = 'Desnown'
__date__ = '02/2019'


from os import system, name
from pdb import set_trace #DEBUGAR

tabuleiro = ['']
def clear_output():
    '''
    Limpar Tela para que fique melhor a vizualiação
    '''
    if name == 'posix':
        system('clear')
    else:
        system('cls')

def welcome():
    print(f"""+-----------------------------+
| WELCOME TO THE TIC-TAC-TOE! |
+-----------------------------+
| Author: {__author__}             |
| Date: {__date__}               |
+-----------------------------+\n""")


def display_board(tab=[' ']*9):
    if len(tab) != 9:
        print("Só aceitamos 9 posições")
        exit()
    '''
    Função responsável por printar o jogo na tela
    '''

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
        market = input('Qual vc prefere, X ou O\n>: ').upper()

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
    # set_trace() #DEBUG
    while True:
        try:
            pos = int(input(f"{jog}, qual posição que você deseja(1-9)\n>: "))
            if pos in range(1,10):
                if not space_check(tab, pos):
                    clear_output()
                    print(f"POSIÇÃO {pos} ESTÁ OCUPADA")
                    display_board(tabuleiro)
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
>: ''').upper().startswith('SIM'),clear_output()


#Limpar tela
clear_output()
#printar uma mensagem de boas vindas.
welcome()
#Guardar os pontos de cada um
pontos = {'Player 1': 0, 'Player 2': 0}
#Player escola X ou O #DEBUG
player1_marker, player2_marker = player_input()
#Jogador primario
player_1 = 'Player 1'
#Jogador secundário
player_2 = 'Player 2'

# set_trace() #DEBUG
while True:
    #Tabuleiro(list) com 9 espaços.
    tabuleiro = [' '] * 9
    #Mantem o jogo percorrendo
    game_on = True

    while game_on:
        print(f"{player_1} começa a partida")
        #printa o jogo/tabuleiro
        clear_output()
        display_board(tabuleiro)
        if player_1 == 'Player 1':
            # set_trace() #DEBUG
            position = player_choice(tabuleiro, player_1)
            place_marker(tabuleiro,player1_marker, position)

        else:
            position = player_choice(tabuleiro, player_1)
            place_marker(tabuleiro,player1_marker, position)

        if win_check(tabuleiro, player1_marker):
            clear_output()
            display_board(tabuleiro)
            print(18*'-')
            print(f"\n{player_1.upper()} GANHOU!!!")
            # set_trace() #DEBUG
            pontos[player_1]+=1
            print_points(pontos)
            display_board(tabuleiro)
            game_on = False

        else:
            if full_board_check(tabuleiro):
                clear_output()
                print("   WE TIED!  ")
                display_board(tabuleiro)
                break

        player_1, player_2 = player_2, player_1
        player1_marker, player2_marker = player2_marker, player1_marker

    # set_trace() #DEBUG
    if not replay()[0]:
        break

    else:
        player_1, player_2 = player_2, player_1
        player1_marker, player2_marker = player2_marker, player1_marker
