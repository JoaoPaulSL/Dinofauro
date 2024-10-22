import pygame
import sys
import random
from settings import SCREEN_WIDTH, SCREEN_HEIGHT
from dino import Dino
from obstacle import Obstacle

class Game:
    def __init__(self, screen):
        self.screen = screen
        self.clock = pygame.time.Clock()
        self.background = pygame.image.load("img/background.png").convert()
        self.dino = Dino()
        self.obstacles = []
        self.score = 0
        self.record = 0
        self.obstacle_speed = 5
        self.spawn_obstacle_event = pygame.USEREVENT
        pygame.time.set_timer(self.spawn_obstacle_event, 2000)  # Geração de obstáculos a cada 2 segundos
        self.game_over = False

    def restart(self):
        self.obstacles.clear()
        self.score = 0
        self.dino.rect.y = SCREEN_HEIGHT - 64
        self.dino.is_jumping = False
        self.game_over = False
        self.obstacle_speed = 5

    def run(self):
        self.handle_events()
        if not self.game_over:
            self.dino.update()
            self.update_game_state()
        self.draw()
        self.clock.tick(60)

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == self.spawn_obstacle_event:
                self.spawn_obstacle()  # Chama o método de geração de obstáculos
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                self.dino.jump()
            if self.game_over and event.type == pygame.KEYDOWN and event.key == pygame.K_r:
                self.restart()

    def spawn_obstacle(self):
        # Gera um novo obstáculo na posição x=800
        obstacle = Obstacle(800)
        self.obstacles.append(obstacle)

    def update_game_state(self):
        for obstacle in self.obstacles:
            obstacle.move(self.obstacle_speed)
            if self.check_collision(self.dino, obstacle):
                self.game_over = True
            if obstacle.rect.x < -obstacle.rect.width:
                self.obstacles.remove(obstacle)
                self.score += 5

                # Aumenta a dificuldade com base na pontuação
                if self.score % 300 == 0:
                    self.obstacle_speed += 1  # Aumenta a velocidade dos obstáculos

        # Atualiza o recorde apenas se o jogo não estiver em game over
        if self.score > self.record and not self.game_over:
            self.record = self.score

    def check_collision(self, dino, obstacle):
        dino_mask = dino.get_mask()
        obstacle_mask = obstacle.get_mask()
        offset = (obstacle.rect.x - dino.rect.x, obstacle.rect.y - dino.rect.y)
        return dino_mask.overlap(obstacle_mask, offset) is not None

    def draw(self):
        self.screen.blit(self.background, (0, 0))
        self.dino.draw(self.screen)
        for obstacle in self.obstacles:
            obstacle.draw(self.screen)

        font = pygame.font.Font(None, 36)
        score_text = font.render(f"Score: {self.score} | Record: {self.record}", True, (0, 0, 0))
        self.screen.blit(score_text, (10, 10))

        if self.game_over:
            font_game_over = pygame.font.Font(None, 72)
            game_over_text = font_game_over.render("Game Over", True, (255, 0, 0))
            self.screen.blit(game_over_text, (SCREEN_WIDTH // 2 - 100, SCREEN_HEIGHT // 2 - 50))

            restart_text = font.render("Pressione 'R' para reiniciar", True, (0, 0, 0))
            self.screen.blit(restart_text, (SCREEN_WIDTH // 2 - 150, SCREEN_HEIGHT // 2))

        pygame.display.flip()
