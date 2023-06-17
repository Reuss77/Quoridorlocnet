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
        self.gameover_music = pygame.mixer.Sound("QuoridorGame/assets/son/gameover.mp3")
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
    def is_valid_wall(self, x1, y1, x2, y2):
        if any(coord < 0 or coord >= self.grid_size for coord in [x1, x2, y1, y2]):
            return False
        if x1 == x2 and abs(y2 - y1) == 2:
            if any(
                (x1 == wx1 and min(y1, y2) < wy2 < max(y1, y2) and min(wy1, wy2) < y1 < max(wy1, wy2)) or
                (x1 == wx2 and min(y1, y2) < wy1 < max(y1, y2)
                 and min(wy1, wy2) < y1 < max(wy1, wy2))
                for wx1, wy1, wx2, wy2 in self.walls
            ):
                return False
            return True
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

# -----------------Win-----------------#

    def is_end_game(self):
        # si il n'y a plus de joueurs
        if len(self.players) == 0:
            self.finish_game()
        # si il ne reste qu'un joueur et que le nombre de coups du joueur restant est égal au nombre de coups +1 du dernier joueur gagnant
        if len(self.players) == 1 and self.last_winner + 1 == self.current_player().coups:
            self.finish_game()

    def finish_game(self):
    # Create the Pygame window
        pygame.init()
        screen = pygame.display.set_mode((920, 685))
        pygame.display.set_caption("Game Over")

        # chargement de l'image de fond
        background_image = pygame.image.load("QuoridorGame/assets/finish.png")
        
        # jouer la game over musique
        self.gameover_music.play()

        # Create the "Replay" and "Quit" buttons
        font = pygame.font.Font(None, 36)
        replay_text = font.render("Replay", True, (255, 255, 255))
        quit_text = font.render("Quit", True, (255, 255, 255))
        replay_button = pygame.Rect(380, 450, replay_text.get_width(), replay_text.get_height())
        quit_button = pygame.Rect(520, 450, quit_text.get_width(), quit_text.get_height())

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_pos = pygame.mouse.get_pos()
                    if replay_button.collidepoint(mouse_pos):
                        self.replay_game()
                    elif quit_button.collidepoint(mouse_pos):
                        pygame.quit()
                        quit()

            # Display the background image and buttons
            screen.blit(background_image, (0, 0))
            pygame.draw.rect(screen, (0, 0, 0), replay_button)
            pygame.draw.rect(screen, (0, 0, 0), quit_button)
            screen.blit(replay_text, (replay_button.x, replay_button.y))
            screen.blit(quit_text, (quit_button.x, quit_button.y))

            pygame.display.flip()
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
    
# -----------------Rejouer-----------------#
    def replay_game(self):
    # Réinitialiser toutes les variables du jeu
        self.current_player_index = 0
        self.walls = []
        self.winner = []
        self.last_winner = None

        # Réinitialiser les positions des joueurs
        for player in self.players:
            player.position = player.start_position

        # Réinitialiser les scores des joueurs
        for player in self.players:
            player.coups = 0

        # Réinitialiser les autres éléments du jeu, si nécessaire

        # Lancer une nouvelle partie
        self.play_game()    
