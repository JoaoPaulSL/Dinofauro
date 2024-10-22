import pygame
import random
from settings import SCREEN_HEIGHT

class Obstacle:
    def __init__(self, x):
        if random.random() < 0.8:  # 80% de chance de ser um cacto
            self.image = pygame.image.load("img/cactus.png").convert_alpha()
            height = random.choice([48, 64, 80])  # Altura aleatória para o cacto
        else:  # 20% de chance de ser um pássaro
            self.image = pygame.image.load("img/cactus4.png").convert_alpha()  # Cacto aéreo
            height = 50  # Altura fixa para o pássaro

        self.image = pygame.transform.scale(self.image, (64, height))
        self.rect = self.image.get_rect(topleft=(x, SCREEN_HEIGHT - height))

    def move(self, speed):
        self.rect.x -= speed

    def draw(self, screen):
        screen.blit(self.image, self.rect.topleft)

    def get_mask(self):
        return pygame.mask.from_surface(self.image)
