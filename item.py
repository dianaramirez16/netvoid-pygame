import pygame
TILE_SIZE = 40

class Item:
    def __init__(self, name, tile_pos, surface):
        self.name = name
        self.tile_pos = tile_pos
        self.surface = surface
        self.collected = False

    def draw(self, screen):
        if not self.collected:
            x, y = self.tile_pos
            draw_x = x * TILE_SIZE + (TILE_SIZE - self.surface.get_width()) // 2
            draw_y = y * TILE_SIZE + (TILE_SIZE - self.surface.get_height()) // 2
            screen.blit(self.surface, (draw_x, draw_y))

    def try_pickup(self, player_tile_pos):
        if not self.collected and self.tile_pos == player_tile_pos:
            self.collected = True
            print(f"Collected: {self.name}")