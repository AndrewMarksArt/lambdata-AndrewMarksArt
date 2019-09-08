'''
DSPT-1Lecture 321-OOP and code style
'''

from random import random


class Game:
    """
    General representation of a game
    """
    def __init__(self, player1='Player 1', player2='Player 2'):
        self.rounds = 1
        self.player1 = player1
        self.player2 = player2

    def print_players(self):
        """
        print out the names of player 1 and player 2
        """
        print('{} is playing {}'.format(self.player1, self.player2))

    def add_rounds(self):
        """
        Incrementing the number of rounds by 1
        """
        self.rounds += 1

    def winner(self):
        return(self.player1 if random() > 0.5 else self.player2)


class TicTacToe(Game):
    def __init__(self):
        super().__init__(player1='Stella', player2='Bailey')

    def print_players(self):
        print('{} is playing Tic-Tac-Toe with {}'.format(self.player1,
                                                         self.player2))
