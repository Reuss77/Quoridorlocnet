import pygame
import pygame.mixer
import time


class Quoridor:
    def __init__(self, players, grid_size=9):
        self.players = players
        self.current_player_index = 0
        self.walls = []
        self.grid_size = grid_size
        self.winner = []
        self.last_winner = None

        # son

        pygame.mixer.init()
        self.win = pygame.mixer.Sound("QuoridorGame/assets/son/win.mp3")
        self.move = pygame.mixer.Sound("QuoridorGame/assets/son/move.mp3")
        self.win.set_volume(0.5)
        self.move.set_volume(0.5)


# -----------------TOUR DE JEU-----------------#

    def current_player(self):
        # retourne le joueur qui doit jouer
        return self.players[self.current_player_index % len(self.players)]

    def next_player(self):
        # passe au joueur suivant dans la liste des joueurs (self.players)
        print(self.current_player_index %
              len(self.players), (self.current_player().name))
        self.current_player_index += 1
        self.next_player_is_ia()

    def next_player_is_ia(self):
        if self.current_player().is_ia():
            # print("Je suis une IA")
            self.current_player().random_move(self)
        # else:
            # print("Je ne suis pas une IA")

# -----------------Move-----------------#

    def move_player(self, x, y):
        # déplace le joueur sur la grille si la position est valide et si le joueur a gagné (ce qui doit être modifié car ne prend pas en charge les égalités.)
        player = self.current_player()

        if (x, y) in self.get_possible_moves():
            player.position = (x, y)
            # DEBUG:print(player.position)
            player.add_coup()  # ajoute un coup au joueur
            self.move.play()  # son du déplacement
            self.winnerCondition()  # vérifie si le joueur a gagné
            self.next_player()  # passe au joueur suivant
        else:
            raise ValueError("Invalid move: player cannot reach this location")

    def is_valid_position(self, x, y):
        """
        Vérifie si la position (x, y) est valide sur la grille
        """
        # DEBUG:print(f"La position ({x}, {y}) est valide.")
        # retourne True si la position est valide, False sinon
        return x >= 0 and x < self.grid_size and y >= 0 and y < self.grid_size and (x, y)

    def get_possible_moves(self):
        # retourne la liste des positions atteignables par le joueur en un seul coup, sous la forme d'une liste de tuples (x, y)
        # mais si un joueur se trouve sur la position (x, y) alors il ne peut pas se déplacer sur cette position (x, y).
        player = self.current_player()
        x, y = player.position
        possible_moves = []
        for dx, dy in [(0, -1), (0, 1), (-1, 0), (1, 0)]:
            nx, ny = x + dx, y + dy
            if self.is_valid_position(nx, ny):
                if self.is_free_position(nx, ny):
                    possible_moves.append((nx, ny))
                else:
                    nnx, nny = nx + dx, ny + dy
                    if self.is_valid_position(nnx, nny):
                        if self.is_free_position(nnx, nny):
                            possible_moves.append((nnx, nny))
                # DEBUG:print(possible_moves)
        return possible_moves

    def is_free_position(self, x, y):
        """
        retourne True si la position (x, y) est libre sur la grille c'est à dire qu'aucun joueur ne s'y trouve
        """
        for player in self.players:  # pour chaque joueur dans la liste des joueurs du jeu
            # si la position du joueur est égale à la position (x, y)
            if player.position == (x, y):
                return False  # retourne False
        return True  # sinon retourne True

# -----------------Wall-----------------#

    def place_wall(self, position, orientation):
        # Vérifier si la position et l'orientation du mur sont valides
        if self.is_valid_wall_position(position, orientation):
            wall = Wall(position, orientation)
            self.walls.append(wall)
        else:
            raise ValueError("Invalid wall position or orientation")

    def is_valid_wall_position(self, position, orientation):
        # Vérifier si la position et l'orientation sont valides
        # Vérifier si le mur ne coupe pas un autre mur déjà présent
        # Retourner True si la position et l'orientation sont valides, False sinon
        # Implémentez la logique appropriée selon vos règles de placement des murs
        return True  # À modifier


# -----------------Win-----------------#

    def is_end_game(self):
        # si il n'y a plus de joueurs
        if len(self.players) == 0:
            self.finish_game()
        # si il ne reste qu'un joueur et que le nombre de coups du joueur restant est égal au nombre de coups +1 du dernier joueur gagnant
        if len(self.players) == 1 and self.last_winner + 1 == self.current_player().coups:
            self.finish_game()

    def finish_game(self):
        # affiche le nom du/des joueur(s) gagnant(s)
        print(self.display_winner())
        # attend 3secondes
        time.sleep(3)
        # quitte le jeu
        pygame.mixer.music.stop()  # Stop the background music
        pygame.quit()
        quit()

    def has_reached_goal(self):
        # si la position du joueur est sur la ligne ou colonne de la position de la ligne de but
        return self.current_player().position in self.current_player().goal_position

    def winnerCondition(self):
        player = self.current_player()
        if player.has_reached_goal():  # si le joueur a gagné
            # ajoute le nom du joueur à la liste des gagnants
            self.winner.append((self.current_player().name,
                               self.current_player().coups))
            print(self.winner)
            self.last_winner = self.current_player().coups
            print(self.last_winner, "last winner")
            self.win.play()  # son de la victoire
            # retire le joueur de la liste des joueursl
            self.players.remove(player)
        self.is_end_game()  # vérifie si la partie est terminée

    def display_winner(self):
        message = ""
        num_winners = len(self.winner)

        if num_winners == 1:
            name, tour = self.winner[0]
            message = f"Bravo à {name.capitalize()} qui finit 1er en {tour} tour."
        elif num_winners == 2:
            names, tours = zip(*self.winner)
            if len(set(tours)) == 1:
                message = f"{', '.join(name.capitalize() for name in names)} ont tous deux gagné au tour {tours[0]}."
            else:
                message = f"{names[0].capitalize()} a gagné au tour {tours[0]} et {names[1].capitalize()} a gagné au tour {tours[1]}."
        elif num_winners == 3:
            names, tours = zip(*self.winner)
            if len(set(tours)) == 1:
                message = f"{', '.join(name.capitalize() for name in names)} ont tous trois gagné au tour {tours[0]}."
            elif len(set(tours[:2])) == 1:
                message = f"{names[0].capitalize()} et {names[1].capitalize()} ont tous deux gagné au tour {tours[0]} et {names[2].capitalize()} a gagné au tour {tours[2]}."
            elif len(set(tours[1:])) == 1:
                message = f"{names[0].capitalize()} a gagné au tour {tours[0]} et {names[1].capitalize()} et {names[2].capitalize()} ont tous deux gagné au tour {tours[1]}."
            else:
                message = f"{names[0].capitalize()} a gagné au tour {tours[0]}, {names[1].capitalize()} a gagné au tour {tours[1]} et {names[2].capitalize()} a gagné au tour {tours[2]}."
        elif num_winners == 4:
            names, tours = zip(*self.winner)
            if len(set(tours)) == 1:
                message = f"{', '.join(name.capitalize() for name in names)} ont tous quatre gagné au tour {tours[0]}."
            elif len(set(tours[:2])) == 1 and len(set(tours[2:])) == 1:
                message = f"{names[0].capitalize()} et {names[1].capitalize()} ont tous deux gagné au tour {tours[0]} et {names[2].capitalize()} et {names[3].capitalize()} ont tous deux gagné au tour {tours[2]}."
            elif len(set(tours[:3])) == 1 and len(set(tours[3:])) == 1:
                message = f"{names[0].capitalize()} a gagné au tour {tours[0]} et {names[1].capitalize()}, {names[2].capitalize()} et {names[3].capitalize()} ont tous trois gagné au tour {tours[2]}."
            else:
                message = f"{names[0].capitalize()} a gagné au tour {tours[0]}, {names[1].capitalize()} a gagné au tour {tours[1]}, {names[2].capitalize()} a gagné au tour {tours[2]} et {names[3].capitalize()} a gagné au tour {tours[3]}."

        return message