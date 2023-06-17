class Test:
    def __init__(self):
        self.grid_size = 4
        self.walls = []

    def is_valid_wall(self, x1, y1, x2, y2):
        if any(coord < 0 or coord >= self.grid_size for coord in [x1, x2, y1, y2]):
            return False

        # Vérifie si le mur est vertical et de longueur 2
        if x1 == x2 and abs(y2 - y1) == 2:
            if any(
                (x1 == wx1 and min(y1, y2) < wy2 < max(y1, y2) and min(wy1, wy2) < y1 < max(wy1, wy2)) or
                (x1 == wx2 and min(y1, y2) < wy1 < max(y1, y2)
                 and min(wy1, wy2) < y1 < max(wy1, wy2))
                for wx1, wy1, wx2, wy2 in self.walls
            ):
                return False
            return True

        # Vérifie si le mur est horizontal et de longueur 2
        if y1 == y2 and abs(x2 - x1) == 2:
            if any(
                (y1 == wy1 and min(x1, x2) < wx2 < max(x1, x2) and min(wx1, wx2) < x1 < max(wx1, wx2)) or
                (y1 == wy2 and min(x1, x2) < wx1 < max(x1, x2)
                 and min(wx1, wx2) < x1 < max(wx1, wx2))
                for wx1, wy1, wx2, wy2 in self.walls
            ):
                return False
            return True

        return False

    def is_free_wall(self, x1, y1, x2, y2):
        for wall in self.walls:
            wx1, wy1, wx2, wy2 = wall
            if (x1, y1, x2, y2) == (wx1, wy1, wx2, wy2) or (x1, y1, x2, y2) == (wx2, wy2, wx1, wy1):
                return False
        return True

    def get_possible_walls(self):
        possible_walls = []
        for x in range(self.grid_size):
            for y in range(self.grid_size):
                if self.is_free_wall(x, y, x, y + 2):
                    possible_walls.append((x, y, x, y + 2))
                if self.is_free_wall(x, y, x + 2, y):
                    possible_walls.append((x, y, x + 2, y))
        return possible_walls

    def add_wall(self, x1, y1, x2, y2):
        x1, y1, x2, y2 = int(x1), int(y1), int(x2), int(
            y2)  # Convertit les coordonnées en entiers

        if self.is_valid_wall(x1, y1, x2, y2) and self.is_free_wall(x1, y1, x2, y2):
            for wall in self.walls:
                wx1, wy1, wx2, wy2 = wall
                # Vérifie si le mur à ajouter coupe un mur existant
                if ((y1 == y2 and wy1 != wy2 and min(x1, x2) < wx1 < max(x1, x2) and min(wy1, wy2) < y1 < max(wy1, wy2)) or
                        (x1 == x2 and wx1 != wx2 and min(y1, y2) < wy1 < max(y1, y2) and min(wx1, wx2) < x1 < max(wx1, wx2))):
                    print("Impossible de poser le mur, il coupe un mur existant.")
                    return

            self.walls.append((x1, y1, x2, y2))
            print("Mur ajouté :", x1, y1, x2, y2)
        else:
            print("Mur invalide :", x1, y1, x2, y2)


place = Test()
print(place.get_possible_walls())
place.add_wall(0, 2, 2, 2)
place.add_wall(1, 1, 1, 3)
place.add_wall(1, 1, 3, 1)
place.add_wall(1, 1, 3, 3)
place.add_wall(1, 3, 1, 5)
print(place.get_possible_walls())
