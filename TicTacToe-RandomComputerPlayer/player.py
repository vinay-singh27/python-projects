import random
import math

class Player() :

    def __init__(self, letter) :
        #letter can be x or o
        self.letter = letter

    def move(self, game) :
        pass


class RandomComputerPlayer(Player) :

    def __init__(self, letter) :
        super().__init__(letter)

    def get_move(self, game) :
        #select a random move
        square = random.choice(game.available_moves())
        return square


class HumanPlayer(Player) :

    def __init__(self, letter):
        super().__init__(letter)

    def get_move(self, game) :
        valid_square = False
        val = None
        while not valid_square :
            square = input(self.letter + '\'s turn. Input move (0-9) :' )
            try :
                val = int(square)
                if val not in game.available_moves() :
                    raise ValueError
                valid_square = True
            except ValueError:
                print('Invalid Input') 
        return val

            

