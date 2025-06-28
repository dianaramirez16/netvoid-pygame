# items.py
from item import Item
import pygame
import os

TILE_SIZE = 40

def create_scrapmetal_surface():
    surface = pygame.Surface((20, 20), pygame.SRCALPHA)
    
    #pygame.draw.rect(surface,(95,95,95),(8,8,10,7))
    #pygame.draw.rect(surface,(230,230,230),(10,7,6,6))
    #pygame.draw.circle(surface, (230,230,230), (12, 20), 4)
    #pygame.draw.polygon(surface, (95,95,95),((8,9),(11,4),(15,2),(18,11)))
    
    return surface

def load_image(filename):
    path = os.path.join("assets", "items", filename)
    return pygame.image.load(path).convert_alpha()

def load_items():
    items_data=[
        ("scrap-metal.png", "scrapmetal", (5, 7)),
        ("chemical.png", "chemical", (3, 4)),
        ("elec-scrap.png", "electrical-scrap", (8, 2)),
        ("fabric-scrap.png", "fabric", (6, 5)),
        ("glass-scrap.png", "glass", (7, 3)),
        ("ichor.png", "ichor", (4, 6)),
        ("paper-scrap.png", "paper", (9, 1)),
        ("rubber-scrap.png", "rubber", (2, 5)),
        ("wild-plant.png", "wild-plant", (1, 7)),
        ("wood-scrap.png", "wood", (10, 4)),
        ("crystal.png", "crystal", (11, 3)),
        ("rubble.png", "rubble", (12, 2)),
    ]
    items=[]
    
    for filename,name,tile_pos in items_data:
        image=load_image(filename)
        item=Item(name=name, tile_pos=tile_pos,surface=image)
        items.append(item)
        print(items)
    
    return items
