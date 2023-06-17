from Interface import Interface
from Player import Player
from Quoridor import Quoridor
from Ai import Ai
import main_Menu as menu
import Button


def main():

    # Lancer le menu
    params = menu.main_menu()
    print("paramètres =  ", params)
    # Créer une instance de Quoridor

    Players = []
    params[1] = int(params[1])
    print("params[1] = ", params[1])
    # Petite variable pour l'initalisation des joueurs en fonction du nombre des paramètres
    mid = params[1] // 2
    maxi = params[1] - 1
    nb_walls = 3

    # Player(self, name, initial_position, goal_position, color, grid_size=9, nb_walls=7):

    if params[0] == 1:
        Players.append(Player("Moi", (0, mid),
                       "d", (194, 65, 245), params[1], nb_walls))
        Players.append(Ai("IA", (maxi, mid), "u",
                       (88, 245, 65), params[1], nb_walls))
        print("Players = ", Players)
        print("Players[0] = ", Players[0])
        print("Players[1] = ", Players[1])
        print("ai")

    if params[0] > 1:
        Players.append(Player("Alice", (0, mid), "d",
                       (194, 65, 245), params[1], nb_walls))
        print("1 player")
        if params[0] >= 2:
            Players.append(
                Player("Dave", (maxi, mid), "u", (88, 245, 65), params[1], nb_walls))
            if params[0] >= 3:
                Players.append(
                    Player("Bob", (mid, maxi), "l", (1, 245, 234), params[1], nb_walls))
                if params[0] >= 4:
                    Players.append(
                        Player("Charlie", (mid, 0), "r", (244, 139, 71), params[1], nb_walls))
    print("Players = ", Players)
    quoridor = Quoridor(Players, params[1])
    print("quoridor = ", quoridor)
    # Créer une instance de Interface
    gui = Interface(quoridor)

    # Lancer l'interface graphique
    gui.run()


# Appeler la fonction main si ce fichier est exécuté
if __name__ == '__main__':
    main()
