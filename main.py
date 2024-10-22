import pygame
import sys
from game import Game

# Inicializa o Pygame
pygame.init()

# Definindo a tela
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 400
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Jogo Dinofauro")

# Cria uma instância do jogo
game = Game(screen)

# Loop principal do jogo
while True:
    game.run()
