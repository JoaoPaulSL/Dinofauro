import pygame
from settings import SCREEN_HEIGHT

class Dino:
    def __init__(self):
        self.image = pygame.image.load("img/dino.png").convert_alpha()
        self.image = pygame.transform.scale(self.image, (64, 64))  # Tamanho do dinossauro
        self.rect = self.image.get_rect(topleft=(50, SCREEN_HEIGHT - 64))  # Posiciona no chão
        self.is_jumping = False
        self.y_velocity = 0

    def jump(self):
        if not self.is_jumping:
            self.is_jumping = True
            self.y_velocity = -10  # Força do pulo

    def update(self):
        if self.is_jumping:
            self.rect.y += self.y_velocity
            self.y_velocity += 0.5  # Gravidade
            if self.rect.bottom >= SCREEN_HEIGHT - 20:
                self.rect.bottom = SCREEN_HEIGHT - 20
                self.is_jumping = False

    def draw(self, screen):
        screen.blit(self.image, self.rect.topleft)

    def get_mask(self):
        return pygame.mask.from_surface(self.image)  # Retorna a máscara do dinossauro
