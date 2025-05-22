import pygame

TILE_SIZE = 40

def create_scrapmetal_surface():
    surface = pygame.Surface((10, 10), pygame.SRCALPHA)
    surface.fill((120, 120, 120))  # metallic gray base

    # Draw rivets or bolts as small circles
    bolt_color = (80, 80, 80)
    pygame.draw.circle(surface, bolt_color, (8, 8), 3)
    pygame.draw.circle(surface, bolt_color, (TILE_SIZE - 8, 8), 3)
    pygame.draw.circle(surface, bolt_color, (8, TILE_SIZE - 8), 3)
    pygame.draw.circle(surface, bolt_color, (TILE_SIZE - 8, TILE_SIZE - 8), 3)
    
    # Optional: add a scratch or crack line
    pygame.draw.line(surface, (100, 100, 100), (10, 20), (30, 30), 2)

    return surface
