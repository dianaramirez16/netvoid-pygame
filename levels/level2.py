# Level 2 logic here
import pygame
from settings import TILE_SIZE


TILEMAP = [
    "BABABABABABABABABABA",
    "ABABAAAAAAAAAAAAAAAT",
    "BABAAAAAAAAAAAAAAAAT",
    "ABAAAAAAAAABABABABAB",
    "BABAAAAAAAAABABABABA",
    "ABAAAAAAAAAAABABABAB",
    "BABAAAAAAAAABABABABA",
    "ABAAAAAAAAAAABABABAB",
    "BABAAAAAAAAABABABABA",
    "ABAAAAAAAAAAABABABAB",
    "BABAAAAAAAAABABABABA",
    "ABAAAAAAAAAAABABABAB",
    "BABABABABABABABABABA",
    "ABABABABABABABABABAB",
    "BABABABABABABABABABA",
]

BLOCKED_TILES = {"w"}

TILE_SIZE = 40
TELEPORT_TILE = "T"
TILE_TYPES = {
    "A": {"surface": pygame.Surface((TILE_SIZE, TILE_SIZE)), "solid": False},
    "B": {"surface": pygame.Surface((TILE_SIZE, TILE_SIZE)), "solid": False},
    "C": {"surface": pygame.Surface((TILE_SIZE, TILE_SIZE)), "solid": False},   # C = computer = solid
    "D": {"surface": pygame.Surface((TILE_SIZE, TILE_SIZE)), "solid": True},   # D = desk = solid
    "W": {"surface": pygame.Surface((TILE_SIZE, TILE_SIZE)), "solid": True},   # W = wall = solid
    "T": {"surface": pygame.Surface((TILE_SIZE, TILE_SIZE)), "solid": False},   # W = wall = solid
    ".": {"surface": None, "solid": False},
}

# Fill tile colors
TILE_TYPES["A"]["surface"].fill((243, 240, 255))  # light tile
TILE_TYPES["B"]["surface"].fill((209, 196, 255))  # dark tile
TILE_TYPES["C"]["surface"].fill((255, 255, 255))  # computer (white)
TILE_TYPES["D"]["surface"].fill((181, 178, 176))  # desk (gray)
TILE_TYPES["W"]["surface"].fill((100, 100, 100))  # wall (dark gray)
TILE_TYPES["T"]["surface"].fill((0,0,0))  # teleport


def draw_level(screen):
    for row_index, row in enumerate(TILEMAP):
        for col_index, tile in enumerate(row):
            tile_surface = TILE_TYPES.get(tile)
            tile_info = TILE_TYPES.get(tile)
            if tile_info and tile_info["surface"]:
                screen.blit(tile_info["surface"], (col_index * TILE_SIZE, row_index * TILE_SIZE))

def get_tile_at_pixel(x, y):
    col = x // TILE_SIZE
    row = y // TILE_SIZE
    try:
        return TILEMAP[row][col]
    except IndexError:
        return None

def is_tile_blocked(tile):
    return tile in BLOCKED_TILES
