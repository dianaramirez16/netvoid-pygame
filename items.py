# items.py
from item import Item
import pygame

TILE_SIZE = 40

def create_scrapmetal_surface():
    surface = pygame.Surface((20, 20), pygame.SRCALPHA)
    
    pygame.draw.rect(surface,(95,95,95),(8,8,10,7))
    pygame.draw.rect(surface,(230,230,230),(10,7,6,6))
    pygame.draw.circle(surface, (230,230,230), (12, 20), 4)
    pygame.draw.polygon(surface, (95,95,95),((8,9),(11,4),(15,2),(18,11)))
    
    return surface

def load_items():
    scrap = Item("scrapmetal", (5, 7), create_scrapmetal_surface())
    return [scrap]
