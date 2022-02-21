import sys
import random
import pygame

class Snake:
    # Toute le function utile pour le bon deroulement du jeu
    def __init__(self):
        self.screen = pygame.display.set_mode((800, 600))

        pygame.display.set_caption("Snake Game")
        self.game_in = True


    def function_principal(self):
        # permet de gerér les evenements, d'afficher certains composant du jeu

        while self.game_in:

            for evenement in pygame.event.get():
                if evenement.type == pygame.QUIT:
                    sys.exit()
            self.screen.fill((0, 0, 0))

            pygame.display.flip()

if __name__ == "__main__":
    pygame.init()
    Snake().function_principal()
    pygame.QUIT()
