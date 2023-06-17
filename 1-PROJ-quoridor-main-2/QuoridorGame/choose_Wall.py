import pygame
import sys
from Button import Button
from main_Menu import *


pygame.init()
SCREEN = pygame.display.set_mode((1280, 720))
pygame.display.set_caption("Walls")

BG = pygame.image.load("QuoridorGame/assets/Background.png")

choice = ["?"]

def walls():
    global choice
    walls_page = True
    num = None

    while walls_page:

        SCREEN.blit(BG, (0, 0))

        MENU_MOUSE_POS = pygame.mouse.get_pos()
        OPTIONS_MOUSE_POS = pygame.mouse.get_pos()

        WALL_TEXT = get_font(50).render("How many walls ?", True, "#b68f40")
        WALL_RECT = WALL_TEXT.get_rect(center=(640, 100))
        SCREEN.blit(WALL_TEXT,WALL_RECT)

        CHOICE_TEXT = get_font(30).render(str(choice), True, "#b68f40")
        selected_walls = [str(wall) if wall != "?" else "?" for wall in choice]
        CHOICE_TEXT = get_font(30).render(" ".join(selected_walls), True, "#b68f40")
        CHOICE_RECT = CHOICE_TEXT.get_rect(center=(640, 500))
        SCREEN.blit(CHOICE_TEXT, CHOICE_RECT)


        _4 = Button(image=None, pos=(400, 250),
                                        text_input="4", font=get_font(30), base_color="black", hovering_color="Green")
        _8 = Button(image=None, pos=(500, 250),
                                        text_input="8", font=get_font(30), base_color="black", hovering_color="Green")
        _12 = Button(image=None, pos=(600, 250),
                                        text_input="12", font=get_font(30), base_color="black", hovering_color="Green")
        _16= Button(image=None, pos=(700, 250),
                                        text_input="16", font=get_font(30), base_color="black", hovering_color="Green")
        _20 = Button(image=None, pos=(800, 250),
                                        text_input="20", font=get_font(30), base_color="black", hovering_color="Green")
        _24 = Button(image=None, pos=(400, 350),
                                        text_input="24", font=get_font(30), base_color="black", hovering_color="Green")
        _28= Button(image=None, pos=(500, 350),
                                        text_input="28", font=get_font(30), base_color="black", hovering_color="Green")
        _32 = Button(image=None, pos=(600, 350),
                                        text_input="32", font=get_font(30), base_color="black", hovering_color="Green")
        _36 = Button(image=None, pos=(700, 350),
                                        text_input="36", font=get_font(30), base_color="black", hovering_color="Green")
        _40= Button(image=None, pos=(800, 350),
                                        text_input="40", font=get_font(30), base_color="black", hovering_color="Green")

        _4.changeColor(OPTIONS_MOUSE_POS)
        _4.update(SCREEN)
        _8.changeColor(OPTIONS_MOUSE_POS)
        _8.update(SCREEN)
        _12.changeColor(OPTIONS_MOUSE_POS)
        _12.update(SCREEN)
        _16.changeColor(OPTIONS_MOUSE_POS)
        _16.update(SCREEN)
        _20.changeColor(OPTIONS_MOUSE_POS)
        _20.update(SCREEN)
        _24.changeColor(OPTIONS_MOUSE_POS)
        _24.update(SCREEN)
        _28.changeColor(OPTIONS_MOUSE_POS)
        _28.update(SCREEN)
        _32.changeColor(OPTIONS_MOUSE_POS)
        _32.update(SCREEN)
        _36.changeColor(OPTIONS_MOUSE_POS)
        _36.update(SCREEN)
        _40.changeColor(OPTIONS_MOUSE_POS)
        _40.update(SCREEN)


        PLAY_BUTTON = Button(image=pygame.image.load("QuoridorGame/assets/Play Rect.png"), pos=(400, 600),
                             text_input="PLAY", font=get_font(75), base_color="#d7fcd4", hovering_color="White")

        QUIT_BUTTON = Button(image=pygame.image.load("QuoridorGame/assets/Quit Rect.png"), pos=(900, 600),
                             text_input="QUIT", font=get_font(75), base_color="#d7fcd4", hovering_color="White")

                
        for button in [PLAY_BUTTON, QUIT_BUTTON]:
            button.changeColor(MENU_MOUSE_POS)
            button.update(SCREEN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if num is None:
                    num = choosenWall(
                        _4, _8, _12, _16, _20, _24, _28, _32, _36, _40, OPTIONS_MOUSE_POS)
                    choice[0] = num if num else "?"
                
                if QUIT_BUTTON.checkForInput(MENU_MOUSE_POS):
                    pygame.quit()
                    sys.exit()

                if PLAY_BUTTON.checkForInput(MENU_MOUSE_POS):
                    walls_page = choice
                    return walls_page

        pygame.display.update()


def choosenWall(_4, _8, _12, _16, _20, _24, _28, _32, _36, _40, options_mouse_pos):
    if _4.checkForInput(options_mouse_pos):
        return 4
    elif _8.checkForInput(options_mouse_pos):
        return 8
    elif _12.checkForInput(options_mouse_pos):
        return 12
    elif _16.checkForInput(options_mouse_pos):
        return 16
    elif _20.checkForInput(options_mouse_pos):
        return 20
    elif _24.checkForInput(options_mouse_pos):
        return 24
    elif _28.checkForInput(options_mouse_pos):
        return 28
    elif _32.checkForInput(options_mouse_pos):
        return 32
    elif _36.checkForInput(options_mouse_pos):
        return 36
    elif _40.checkForInput(options_mouse_pos):
        return 40
    else:
        return None