from pygame import Color


class Player:
    def __init__(self, name, initial_position, goal_position, color, grid_size=9, nb_walls=5):
        self.name = name
        self.grid_size = grid_size
        self.position = initial_position
        self.goal_position = goal_position
        self.color = Color(color)
        self.walls = nb_walls
        self.coups = 0

    def has_reached_goal(self):
        # si la position du joueur est sur la ligne ou colonne de la position de la ligne de but
        if self.goal_position == "l" and self.position[1] == 0:
            return True
        elif self.goal_position == "r" and self.position[1] == self.grid_size - 1:
            return True
        elif self.goal_position == "d" and self.position[0] == self.grid_size - 1:
            return True
        elif self.goal_position == "u" and self.position[0] == 0:
            return True
        else:
            return False

    def use_wall(self):
        self.walls -= 1

    def add_coup(self):
        self.coups += 1

    def is_ia(self):
        print("not IA")
        return False
