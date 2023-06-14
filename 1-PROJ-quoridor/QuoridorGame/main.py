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
    # donne la moitié de la taille de la grille (paramètre 1) donc pour 9x9, params[1] devrait retourner 4
    mid = params[1] // 2
    maxi = params[1] - 1

    if params[0] == 1:
        Players.append(Player("M    oi", (0, mid),
                       "d", (194, 65, 245), params[1]))
        Players.append(Ai("IA", (maxi, mid), "u", (88, 245, 65), params[1]))
        print("Players = ", Players)
        print("Players[0] = ", Players[0])
        print("Players[1] = ", Players[1])
        print("ai")

    if params[0] > 1:
        Players.append(Player("Alice", (0, mid), "d",
                    (194, 65, 245), params[1]))
        print("1 player")
        if params[0] >= 2:
            if params[2] == "network":
                Players.append(
                    Player("Dave", (maxi, mid), "u", (88, 245, 65), params[1], network=True))
            else:
                Players.append(
                    Player("Dave", (maxi, mid), "u", (88, 245, 65), params[1]))
        if params[0] >= 3:
            if params[2] == "network":
                Players.append(
                    Player("Bob", (mid, maxi), "l", (1, 245, 234), params[1], network=True))
            else:
                Players.append(
                    Player("Bob", (mid, maxi), "l", (1, 245, 234), params[1]))
        if params[0] >= 4:
            if params[2] == "network":
                Players.append(
                    Player("Charlie", (mid, 0), "r", (244, 139, 71), params[1], network=True))
            else:
                Players.append(
                    Player("Charlie", (mid, 0), "r", (244, 139, 71), params[1]))
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