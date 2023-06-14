import pygame
import Quoridor
from Wall import Wall
import random


class Interface:
    def __init__(self, quoridor):
        pygame.init()
        self.quoridor = quoridor
        self.window_width = 1200
        self.window_height = 700
        self.grid_size = quoridor.grid_size
        self.window = pygame.display.set_mode(
            (self.window_width, self.window_height), pygame.RESIZABLE)
        self.background_image = pygame.image.load(
            "QuoridorGame/assets/Background.png").convert()
        self.grid_color = pygame.Color(0, 0, 0)
        self.font = pygame.font.Font(None, 30)
        self.board_size = self.window_height - 80
        self.cell_size = self.board_size // self.grid_size
        self.cell_color = pygame.Color(182, 143, 64, 255)
        self.margin = (self.window_width - self.board_size) // 2
        self.board_rect = pygame.Rect(
            self.margin, 40, self.board_size, self.board_size)
        self.surface = pygame.Surface(
            (self.window_width, self.window_height - 40))
        self.screen = pygame.display.set_mode(
            (self.window_width, self.window_height))
        self.clock = pygame.time.Clock()
        self.FPS = 60
        self.fullscreen = False

        self.ambianceList = ["QuoridorGame/assets/son/son0.mp3",
                             "QuoridorGame/assets/son/son1.mp3",
                             "QuoridorGame/assets/son/son2.mp3",
                             "QuoridorGame/assets/son/son3.mp3"]
        self.current_track = 0

        # Événement pour détecter la fin de chaque morceau de musique
        self.music_end_event = pygame.USEREVENT + 1
        pygame.mixer.music.set_endevent(self.music_end_event)
        # boutton pour la musique on/off
        # Chargement des images du bouton
        self.button_son_on = pygame.image.load(
            "QuoridorGame/assets/high-sound.png")
        self.button_son_off = pygame.image.load(
            "QuoridorGame/assets/mute-sound.png")

        # Position du bouton
        self.button_x = 20
        self.button_y = self.window_height // 2

        # État du bouton (désactivé au départ)
        self.button_son_etat = False

    def draw(self):
        self.draw_background()
        # Draw the board
        self.drawn_board()
        self.draw_pawn()
        self.draw_possible_moves()
        self.clock.tick(self.FPS)
        # print(self.clock.get_fps())
        if self.button_son_etat:
            bouton_son = self.button_son_on
        else:
            bouton_son = self.button_son_off
        self.screen.blit(bouton_son, (self.button_x, self.button_y))

        pygame.display.update()


# -----------------Dessine le plateau-----------------#

    def drawn_board(self):
        # Draw player info on left side
        player = self.quoridor.players[0]
        nomP1 = f"Player: {player.name}"
        wallP1 = f"Walls left: {player.walls}"
        afficheNomP1 = self.font.render(
            nomP1, True, self.get_player_color(player))
        afficheWallP1 = self.font.render(
            wallP1, True, self.get_player_color(player))
        self.window.blit(afficheNomP1, (20, 20))
        self.window.blit(afficheWallP1, (20, 50))
        if len(self.quoridor.players) > 1:
            # Draw player info on right side
            player2 = self.quoridor.players[1]
            nomP2 = f"Player: {player2.name}"
            WallP2 = f"Walls left: {player2.walls}"
            afficheNomP2 = self.font.render(
                nomP2, True, self.get_player_color(player2))
            afficheWallP2 = self.font.render(
                WallP2, True, self.get_player_color(player2))
            self.window.blit(afficheNomP2, (self.window_width -
                                            afficheNomP2.get_width() - 20, 20))
            self.window.blit(afficheWallP2, (self.window_width -
                                             afficheWallP2.get_width() - 20, 50))

        if len(self.quoridor.players) > 2:
            # Draw player info on right bottom side
            player3 = self.quoridor.players[2]
            nomP3 = f"Player: {player3.name}"
            WallP3 = f"Walls left: {player3.walls}"
            afficheNomP3 = self.font.render(
                nomP3, True, self.get_player_color(player3))
            afficheWallP3 = self.font.render(
                WallP3, True, self.get_player_color(player3))
            self.window.blit(afficheNomP3, (self.window_width -
                             afficheNomP3.get_width() - 20, self.window_height - 80))
            self.window.blit(afficheWallP3, (self.window_width -
                             afficheWallP3.get_width() - 20, self.window_height - 50))

        if len(self.quoridor.players) > 3:
            player4 = self.quoridor.players[3]
            nomP4 = f"Player: {player4.name}"
            WallP4 = f"Walls left: {player4.walls}"
            afficheNomP4 = self.font.render(
                nomP4, True, self.get_player_color(player4))
            afficheWallP4 = self.font.render(
                WallP4, True, self.get_player_color(player4))
            self.window.blit(afficheNomP4, (20, self.window_height - 80))
            self.window.blit(afficheWallP4, (20, self.window_height - 50))

        # Draw board
        pygame.draw.rect(self.window, self.grid_color, self.board_rect, 1)
        background = pygame.Surface(self.board_rect.size)
        background.fill(self.cell_color)
        self.window.blit(background, self.board_rect)

        for i in range(self.grid_size):
            start_pos = (self.margin, 40 + i * self.cell_size)
            end_pos = (self.margin + self.board_size, 40 + i * self.cell_size)
            pygame.draw.line(self.window, self.grid_color,
                             start_pos, end_pos, 1)
            start_pos = (self.margin + i * self.cell_size, 40)
            end_pos = (self.margin + i * self.cell_size, 40 + self.board_size)
            pygame.draw.line(self.window, self.grid_color,
                             start_pos, end_pos, 1)

        # Draw player current  info en haut au centre de lécran:
        tour = f"C'est au tour de : {player.name} !"
        players = self.font.render(tour, True, self.get_player_color(player))
        self.window.blit(players, (self.window_width //
                         2 - players.get_width() // 2, 20))

        self.draw_walls()


# -----------------Dessine pions-----------------#

    def draw_pawn(self):
        # Draw players
        for player in self.quoridor.players:
            player_color = self.get_player_color(player)
            player_pos = player.position
            x = self.board_rect.left + \
                player_pos[1] * self.cell_size + self.cell_size // 2
            y = self.board_rect.top + \
                player_pos[0] * self.cell_size + self.cell_size // 2
            pygame.draw.circle(self.screen, player_color,
                               (x, y), self.cell_size // 3)

# -----------------Recupère la couleur-----------------#

    def get_player_color(self, player):
        return player.color

# -----------------Interaction-----------------#

    def run(self):
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == self.music_end_event:
                    # Passe au morceau suivant
                    self.current_track = (
                        self.current_track + 1) % len(self.ambianceList)
                    self.son()

                elif event.type == pygame.VIDEORESIZE and self.fullscreen == False:
                    self.window_width, self.window_height = event.size
                    self.window = pygame.display.set_mode(
                        (self.window_width, self.window_height), pygame.RESIZABLE)
                    self.board_size = self.window_height - 80
                    self.cell_size = self.board_size // self.grid_size
                    self.margin = (self.window_width - self.board_size) // 2
                    self.board_rect = pygame.Rect(
                        self.margin, 40, self.board_size, self.board_size)
                    pygame.display.set_mode(
                        (self.window_width, self.window_height), pygame.RESIZABLE,)

                elif event.type == pygame.MOUSEBUTTONDOWN:
                    # Get the position of the mouse click relative to the board
                    mouse_pos = pygame.mouse.get_pos()
                    x, y = mouse_pos[0] - self.margin, mouse_pos[1] - 40
                    row, col = y // self.cell_size, x // self.cell_size
                    if (row, col) in self.quoridor.get_possible_moves():
                        self.quoridor.move_player(row, col)
                    elif self.button_x <= mouse_pos[0] <= self.button_x + self.button_son_on.get_width() and self.button_y <= mouse_pos[1] <= self.button_y + self.button_son_on.get_height():
                        self.button_son_etat = not self.button_son_etat  # Inversion de l'état du bouton
                        self.son()  # Appel de la fonction son

                # cheat/debug
                elif event.type == pygame.KEYDOWN:
                    # debug next player
                    if event.key == pygame.K_SPACE:
                        print("le joueur est : ",
                              self.quoridor.current_player().name)
                        self.quoridor.next_player()
                        print("le joueur actuel deviens : ",
                              self.quoridor.current_player().name)
                    # debug add wall
                    elif event.key == pygame.K_1:
                        self.quoridor.add_wall()
                    elif event.key == pygame.K_ESCAPE:
                        # Sortir du mode plein écran et afficher la fenêtre en mode fenêtré par defaut
                        if pygame.display.get_surface().get_flags() & pygame.FULLSCREEN:
                            self.defaut_screen()
                            print("fullscreen off")
                        else:
                            quit()
                    elif event.key == pygame.K_F11:
                        if pygame.display.get_surface().get_flags() & pygame.FULLSCREEN:
                            self.defaut_screen()
                            print("fullscreen off")
                        else:
                            pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
                            self.window_width, self.window_height = pygame.display.get_surface().get_size()
                            self.window = pygame.display.set_mode(
                                (self.window_width, self.window_height), pygame.RESIZABLE, pygame.FULLSCREEN)
                            self.board_size = self.window_height - 80
                            self.cell_size = self.board_size // self.grid_size
                            self.margin = (self.window_width -
                                           self.board_size) // 2
                            self.board_rect = pygame.Rect(
                                self.margin, 40, self.board_size, self.board_size)
                            pygame.display.set_mode(
                                (self.window_width, self.window_height), pygame.RESIZABLE, pygame.FULLSCREEN)
                            pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
                            print("fullscreen on")
                            self.fullscreen = True

            self.draw()
        pygame.quit()


# -----------------son-----------------#

    def son(self):
        random.shuffle(self.ambianceList)
        if self.button_son_etat == True:
            pygame.mixer.music.load(self.ambianceList[self.current_track])
            pygame.mixer.music.play()
            print("son on")
        else:
            pygame.mixer.music.stop()
            pygame.mixer.music.unload()
            print("son off")
# -----------------Move-----------------#

    def draw_possible_moves(self):
       # Draw possible moves
        possible_moves = self.quoridor.get_possible_moves()
        for move_pos in possible_moves:
            x = self.board_rect.left + \
                move_pos[1] * self.cell_size + self.cell_size // 2
            y = self.board_rect.top + \
                move_pos[0] * self.cell_size + self.cell_size // 2
            pygame.draw.circle(
                self.screen, self.quoridor.current_player().color, (x, y), self.cell_size // 6)

# -----------------Wall-----------------#

    def draw_walls(self):
        for wall in self.quoridor.walls:
            if wall.orientation == "horizontal":
                # Dessiner le mur horizontal entre les deux cellules
                # Implémentez la logique pour dessiner un mur horizontal entre les cellules appropriées
                pass
            elif wall.orientation == "vertical":
                # Dessiner le mur vertical entre les deux cellules
                # Implémentez la logique pour dessiner un mur vertical entre les cellules appropriées
                pass

    def draw_background(self):
        # Redimensionner l'image de l'arrière-plan à la taille de la fenêtre
        background = pygame.transform.scale(
            self.background_image, (self.window_width, self.window_height))
        self.window.blit(background, (0, 0))

    def defaut_screen(self):
        # Afficher l'écran avec les propriété au démarrage

        pygame.display.set_mode(
            (self.window_width, self.window_height), pygame.RESIZABLE,)
        self.window_width, self.window_height = 1200, 700
        self.window = pygame.display.set_mode(
            (self.window_width, self.window_height), pygame.RESIZABLE)
        self.board_size = self.window_height - 80
        self.cell_size = self.board_size // self.grid_size
        self.margin = (self.window_width -
                       self.board_size) // 2
        self.board_rect = pygame.Rect(
            self.margin, 40, self.board_size, self.board_size)
        self.fullscreen = False