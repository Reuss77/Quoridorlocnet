from pygame import Color
import random
from Quoridor import Quoridor
from Player import Player


class Ai(Player):
    def __init__(self, name, initial_position, goal_position, color, grid_size=9):
        super().__init__(name, initial_position, goal_position, color, grid_size)

    def random_move(self, quoridor):
        possible_moves = quoridor.get_possible_moves()
        random_move = random.choice(possible_moves)
        print(random_move)
        x = random_move[1]
        y = random_move[0]
        quoridor.move_player(y, x)
        print("tentative de mouvement random")
        return random_move

    def is_smart_move(self, quoridor):
        pass

    def is_ia(self):
        print("IA")
        return True