from pygame import *

# la class Wall gère les murs/barrières du jeu


class Wall:
    def __init__(self, position, orientation):
        # position du mur sur la grille (x1 , y1 , x2 , y2)
        self.position = position
        # orientation du mur (h = horizontal, v = vertical)
        self.orientation = orientation
        self.color = Color("black")  # couleur du mur
        self.thickness = 5  # épaisseur du mur

    def get_position(self):
        # retourne la position du mur
        return self.position

    def get_orientation(self):
        # retourne l'orientation du mur
        return self.orientation

    def get_color(self):
        # retourne la couleur du mur
        return self.color

    def get_thickness(self):
        # retourne l'épaisseur du mur
        return self.thickness

    def set_position(self, position):
        # modifie la position du mur
        self.position = position

    def set_orientation(self, orientation):
        # modifie l'orientation du mur
        self.orientation = orientation

    def set_color(self, color):
        # modifie la couleur du mur
        self.color = color

    def set_thickness(self, thickness):
        # modifie l'épaisseur du mur
        self.thickness = thickness

    def __eq__(self, other):
        # retourne True si le mur est égal à un autre mur
        return self.position == other.position and self.orientation == other.orientation and self.color == other.color and self.thickness == other.thickness

    def __ne__(self, other):
        # retourne True si le mur est différent d'un autre mur
        return not self.__eq__(other)
