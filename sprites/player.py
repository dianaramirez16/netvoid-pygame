import pygame
from settings import TILE_SIZE
from levels import level1, level2

class Player(pygame.sprite.Sprite):
    def __init__(self, x, y, level_module):
        super().__init__()
        self.image = pygame.Surface((TILE_SIZE, TILE_SIZE))
        self.image.fill((0, 0, 255))  # Blue square
        self.rect = self.image.get_rect(topleft=(x, y))
        self.speed = TILE_SIZE  # Move half-tile at a time
        self.level = level_module

    def move(self, dx, dy):
        new_x = self.rect.x + dx
        new_y = self.rect.y + dy
        center_x = new_x + self.rect.width // 2
        center_y = new_y + self.rect.height // 2

        # Only move if the new tile is not blocked
        tile = self.level.get_tile_at_pixel(center_x, center_y)
        if not self.level.is_tile_blocked(center_x, center_y):
            self.rect.x = new_x
            self.rect.y = new_y

    def handle_keys(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.move(-self.speed, 0)
        elif keys[pygame.K_RIGHT]:
            self.move(self.speed, 0)
        elif keys[pygame.K_UP]:
            self.move(0, -self.speed)
        elif keys[pygame.K_DOWN]:
            self.move(0, self.speed)

    def update(self):
        self.handle_keys()
