import pygame
import sys
from Button import Button
from Rules import *

pygame.init()
SCREEN = pygame.display.set_mode((1280, 720))
pygame.display.set_caption("Menu")

BG = pygame.image.load("QuoridorGame/assets/Background.png")

chosen_options = ["?","?","?"]


def get_font(size):  # Returns Press-Start-2P in the desired size
    return pygame.font.Font("QuoridorGame/assets/font.ttf", size)


def main_menu():
    global chosen_options 
    menu = True
    player = None
    board = None
    gameType = None
    while menu:
        SCREEN.blit(BG, (0, 0))

        MENU_MOUSE_POS = pygame.mouse.get_pos()
        OPTIONS_MOUSE_POS = pygame.mouse.get_pos()

        MENU_TEXT = get_font(100).render("QUORIDOR", True, "#b68f40")
        MENU_RECT = MENU_TEXT.get_rect(center=(640, 100))

        # Ajouter les options de nombre de joueurs
        PLAYERS_TEXT = get_font(30).render("Players :", True, "#d7fcd4")
        PLAYERS_RECT = PLAYERS_TEXT.get_rect(center=(300, 250))
        SCREEN.blit(PLAYERS_TEXT, PLAYERS_RECT)

        PLAYER_1_BUTTON = Button(image=None, pos=(600, 250),
                                 text_input="1", font=get_font(30), base_color="black", hovering_color="Green")
        PLAYER_2_BUTTON = Button(image=None, pos=(670, 250),
                                 text_input="2", font=get_font(30), base_color="black", hovering_color="Green")
        PLAYER_3_BUTTON = Button(image=None, pos=(740, 250),
                                 text_input="3", font=get_font(30), base_color="black", hovering_color="Green")
        PLAYER_4_BUTTON = Button(image=None, pos=(800, 250),
                                 text_input="4", font=get_font(30), base_color="black", hovering_color="Green")

        PLAYER_1_BUTTON.changeColor(OPTIONS_MOUSE_POS)
        PLAYER_1_BUTTON.update(SCREEN)
        PLAYER_2_BUTTON.changeColor(OPTIONS_MOUSE_POS)
        PLAYER_2_BUTTON.update(SCREEN)
        PLAYER_3_BUTTON.changeColor(OPTIONS_MOUSE_POS)
        PLAYER_3_BUTTON.update(SCREEN)
        PLAYER_4_BUTTON.changeColor(OPTIONS_MOUSE_POS)
        PLAYER_4_BUTTON.update(SCREEN)

        # Ajouter les options de taille de plateau
        BOARD_SIZE_TEXT = get_font(30).render("Board :", True, "#d7fcd4")
        BOARD_SIZE_RECT = BOARD_SIZE_TEXT.get_rect(center=(300, 350))
        SCREEN.blit(BOARD_SIZE_TEXT, BOARD_SIZE_RECT)

        SIZE_5_BUTTON = Button(image=None, pos=(550, 350),
                               text_input="5x5", font=get_font(30), base_color="black", hovering_color="Green")
        SIZE_7_BUTTON = Button(image=None, pos=(670, 350),
                               text_input="7x7", font=get_font(30), base_color="black", hovering_color="Green")
        SIZE_9_BUTTON = Button(image=None, pos=(780, 350),
                               text_input="9x9", font=get_font(30), base_color="black", hovering_color="Green")
        SIZE_11_BUTTON = Button(image=None, pos=(920, 350),
                                text_input="11x11", font=get_font(30), base_color="black", hovering_color="Green")

        SIZE_5_BUTTON.changeColor(OPTIONS_MOUSE_POS)
        SIZE_5_BUTTON.update(SCREEN)
        SIZE_7_BUTTON.changeColor(OPTIONS_MOUSE_POS)
        SIZE_7_BUTTON.update(SCREEN)
        SIZE_9_BUTTON.changeColor(OPTIONS_MOUSE_POS)
        SIZE_9_BUTTON.update(SCREEN)
        SIZE_11_BUTTON.changeColor(OPTIONS_MOUSE_POS)
        SIZE_11_BUTTON.update(SCREEN)

        # Ajouter les options de type de jeu
        GAME_TYPE_TEXT = get_font(30).render("Game type :", True, "#d7fcd4")
        GAME_TYPE_RECT = GAME_TYPE_TEXT.get_rect(center=(300, 450))
        SCREEN.blit(GAME_TYPE_TEXT, GAME_TYPE_RECT)

        LOCAL_BUTTON = Button(image=None, pos=(600, 450),
                              text_input="Local", font=get_font(30), base_color="black", hovering_color="Green")
        NETWORK_BUTTON = Button(image=None, pos=(850, 450),
                                text_input="Network", font=get_font(30), base_color="black", hovering_color="Green")
        JOIN_BUTTON = Button(image=None, pos=(1050, 450),
                             text_input="JOIN", font=get_font(30), base_color="black", hovering_color="Green")

        LOCAL_BUTTON.changeColor(OPTIONS_MOUSE_POS)
        LOCAL_BUTTON.update(SCREEN)
        NETWORK_BUTTON.changeColor(OPTIONS_MOUSE_POS)
        NETWORK_BUTTON.update(SCREEN)
        JOIN_BUTTON.changeColor(OPTIONS_MOUSE_POS)
        JOIN_BUTTON.update(SCREEN)

        PARAMS_TEXT = get_font(30).render(str(chosen_options), True, "#b68f40")
        selected_options = [str(option) if option != "?" else "?" for option in chosen_options]
        PARAMS_TEXT = get_font(30).render(" ".join(selected_options), True, "#b68f40")
        PARAMS_RECT = PARAMS_TEXT.get_rect(center=(640, 500))

        PLAY_BUTTON = Button(image=pygame.image.load("QuoridorGame/assets/Play Rect.png"), pos=(400, 600),
                             text_input="PLAY", font=get_font(75), base_color="#d7fcd4", hovering_color="White")

        QUIT_BUTTON = Button(image=pygame.image.load("QuoridorGame/assets/Quit Rect.png"), pos=(900, 600),
                             text_input="QUIT", font=get_font(75), base_color="#d7fcd4", hovering_color="White")

        RULES_BUTTON = Button(image=pygame.image.load("QuoridorGame/assets/whynot.png"), pos=(100, 100),
                              text_input="", font=get_font(35), base_color="#d7fcd4", hovering_color="White",)

        SCREEN.blit(MENU_TEXT, MENU_RECT)
        SCREEN.blit(PARAMS_TEXT, PARAMS_RECT)


        for button in [PLAY_BUTTON, QUIT_BUTTON, RULES_BUTTON]:
            button.changeColor(MENU_MOUSE_POS)
            button.update(SCREEN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if player is None:
                    player = choosenPlayer(
                        PLAYER_1_BUTTON, PLAYER_2_BUTTON, PLAYER_3_BUTTON, PLAYER_4_BUTTON, OPTIONS_MOUSE_POS)
                    chosen_options[0] = player if player else "?"
                elif board is None:
                    board = choosenBoard(
                        SIZE_5_BUTTON, SIZE_7_BUTTON, SIZE_9_BUTTON, SIZE_11_BUTTON, OPTIONS_MOUSE_POS)
                    chosen_options[1] = board if board else "?"
                elif gameType is None:
                    gameType = choosenGameType(
                        LOCAL_BUTTON, NETWORK_BUTTON, JOIN_BUTTON, OPTIONS_MOUSE_POS)
                    chosen_options[2] = gameType if gameType else "?"
                
                PARAMS_TEXT = get_font(30).render(str(chosen_options), True, "#b68f40")
                selected_options = [str(option) if option != "?" else "?" for option in chosen_options]
                PARAMS_RECT = PARAMS_TEXT.get_rect(center=(640, 530))

                if PLAY_BUTTON.checkForInput(MENU_MOUSE_POS):
                    if player is not None and board is not None and gameType is not None:
                        chosen_options[0] = player
                        chosen_options[1] = board
                        chosen_options[2] = gameType
                        print(chosen_options)
                        menu = chosen_options
                        return menu

                if QUIT_BUTTON.checkForInput(MENU_MOUSE_POS):
                    pygame.quit()
                    sys.exit()
                if RULES_BUTTON.checkForInput(MENU_MOUSE_POS):
                    rules()

        pygame.display.update()
    return menu


def choosenPlayer(player1, player2, player3, player4, options_mouse_pos):
    if player1.checkForInput(options_mouse_pos):
        return 1
    elif player2.checkForInput(options_mouse_pos):
        return 2
    elif player3.checkForInput(options_mouse_pos):
        return 3
    elif player4.checkForInput(options_mouse_pos):
        return 4
    else:
        return None


def choosenBoard(board1, board2, board3, board4, options_mouse_pos):
    if board1.checkForInput(options_mouse_pos):
        return 5
    if board2.checkForInput(options_mouse_pos):
        return 7
    if board3.checkForInput(options_mouse_pos):
        return 9
    if board4.checkForInput(options_mouse_pos):
        return 11
    else:
        return None



def choosenGameType(gameType1, gameType2, gameType3, options_mouse_pos):
    if gameType1.checkForInput(options_mouse_pos):
        return "Local"
    if gameType2.checkForInput(options_mouse_pos):
        return "Network"
    if gameType3.checkForInput(options_mouse_pos):
        return "Join"
    else:
        return None

