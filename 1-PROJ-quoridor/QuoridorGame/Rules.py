import pygame
import sys
from Button import Button

pygame.init()
SCREEN = pygame.display.set_mode((1280, 720))
pygame.display.set_caption("Rules")

BG = pygame.image.load("QuoridorGame/assets/Background.png")

def get_font(size):  # Returns Press-Start-2P in the desired size
    return pygame.font.Font("QuoridorGame/assets/font.ttf", size)

def rules():
    rules_page = True

    while rules_page:
        SCREEN.blit(BG, (0, 0))

        RULES_TEXT = get_font(40).render("Rules", True, "#b68f40")
        RULES_RECT = RULES_TEXT.get_rect(center=(640, 100))
        SCREEN.blit(RULES_TEXT, RULES_RECT)

        RULES_CONTENT = [
            "Chaque joueur commence avec un pion à sa position départ, située au milieu de son du plateau.",
            " ",
            "À tour de rôle, chaque joueur peut déplacer son pion d'une case en avant, en arrière, à droite ou à gauche.",
            " ",
            "Ou bien, il peut choisir de placer un mur qui bloque le chemin de l'adversaire.",
            " ",
            "L'utilisation des barrières est stratégique. Elles peuvent ralentir l'adversaire, mais on en possède en nombre limité.",
            " ",
            "Il est interdit de bloquer totalement le passage de l'adversaire. Un chemin doit toujours exister.",
            " ",
            "Lorsqu'un joueur arrive sur le bord opposé à son départ, il gagne la partie. Un message s'affichera si c'est le cas.",
            " ",
            "Si c'est une partie multi-joueur,", 
            " ",
            "le jeu continue jusqu'à ce qu'il reste uniquement un seul joueur qui n'a pas atteint le bord opposé."
        ]

        RULES_CONTENT_FONT = get_font(10)
        RULES_CONTENT_COLOR = "#d7fcd4"
        RULES_CONTENT_MARGIN = 20
        y_pos = 200

        for rule in RULES_CONTENT:
            rule_text = RULES_CONTENT_FONT.render(rule, True, RULES_CONTENT_COLOR)
            rule_rect = rule_text.get_rect(center=(640, y_pos))
            SCREEN.blit(rule_text, rule_rect)
            y_pos += rule_rect.height + RULES_CONTENT_MARGIN

        BACK_BUTTON = Button(image=None, pos=(640, 680),
                             text_input="BACK", font=get_font(30), base_color="White", hovering_color="Green")

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if BACK_BUTTON.checkForInput(pygame.mouse.get_pos()):
                    rules_page = False

        BACK_BUTTON.changeColor(pygame.mouse.get_pos())
        BACK_BUTTON.update(SCREEN)

        pygame.display.update()
