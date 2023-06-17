from pygame import Color
import random
from Quoridor import Quoridor
from Player import Player


class Ai(Player):
    def __init__(self, name, initial_position, goal_position, color, grid_size=9, nb_walls=7):
        super().__init__(name, initial_position, goal_position, color, grid_size, nb_walls)

    def random_move(self, quoridor):
        possible_moves = quoridor.get_possible_moves()
        random_move = random.choice(possible_moves)
        x = random_move[1]
        y = random_move[0]
        quoridor.move_player(y, x)
        print("Random move")
        return random_move

    def alpha_beta(self, quoridor, depth, alpha, beta, maximizing_player):
        if depth == 0 or quoridor.is_game_over():
            return self.evaluate_position(quoridor)

        if maximizing_player:
            max_eval = float('-inf')
            possible_moves = quoridor.get_possible_moves()

            for move in possible_moves:
                x = move[1]
                y = move[0]
                quoridor.move_player(y, x)

                eval = self.alpha_beta(quoridor, depth - 1, alpha, beta, False)

                quoridor.undo_move()

                max_eval = max(max_eval, eval)
                alpha = max(alpha, eval)
                if beta <= alpha:
                    break

            return max_eval
        else:
            min_eval = float('inf')
            possible_moves = quoridor.get_possible_moves()

            for move in possible_moves:
                x = move[1]
                y = move[0]
                quoridor.move_player(y, x)

                eval = self.alpha_beta(quoridor, depth - 1, alpha, beta, True)

                quoridor.undo_move()

                min_eval = min(min_eval, eval)
                beta = min(beta, eval)
                if beta <= alpha:
                    break

            return min_eval

    def is_smart_move(self, quoridor):
        best_eval = float('-inf')
        best_move = None
        possible_moves = quoridor.get_possible_moves()

        for move in possible_moves:
            x = move[1]
            y = move[0]
            quoridor.move_player(y, x)

            eval = self.alpha_beta(quoridor, 3, float('-inf'), float('inf'), False)

            quoridor.undo_move()

            if eval > best_eval:
                best_eval = eval
                best_move = move

        x = best_move[1]
        y = best_move[0]
        quoridor.move_player(y, x)
        print("Smart move")
        return best_move

    def is_ia(self):
        print("AI")
        return True
