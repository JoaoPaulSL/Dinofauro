import pygame
import random
from settings import SCREEN_HEIGHT

class Obstacle:
    def __init__(self, x):
        # 100% de chance de ser um cacto
        self.image = pygame.image.load("img/cactus.png").convert_alpha()
        height = random.choice([48, 64, 80])  # Altura aleatória para o cacto

        self.image = pygame.transform.scale(self.image, (64, height))
        self.rect = self.image.get_rect(topleft=(x, SCREEN_HEIGHT - height))

    def move(self, speed):
        self.rect.x -= speed

    def draw(self, screen):
        screen.blit(self.image, self.rect.topleft)

    def get_mask(self):
        return pygame.mask.from_surface(self.image)
