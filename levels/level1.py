import pygame

# Simple tilemap (G = grass, D = dirt)
TILEMAP = [
    "ABABABABABABABABABAB",
    "DDDDDDDABABABABABABA",
    "DDDDDDDDABABABABABAB",
    "BABABADDDABABABABABA",
    "ABABABADDDABABABABAB",
    "BABABABADDDABABABABA",
    "RRRTABABADDBABABABPB",
    "RRRTBABABDDABABABAPA",
    "RRRTABABADDBABABABAB",
    "BABABABABDDABABABAPA",
    "ABABABABADDBABABABAB",
    "BABABABABDDABABABABA",
    "ABAWWBWWAWWBWWABWWAB",
    "BABWWAWWBWWAWWBAWWBA",
    "ABAWWBWWAWWBWWABWWAB",
]

TILE_SIZE = 40
TELEPORT_TILE = "T"

robot_surface = pygame.Surface((TILE_SIZE, TILE_SIZE))
robot_surface.fill((255, 255, 255))  # background white

# Draw eyes
pygame.draw.circle(robot_surface, (0, 0, 0), (10, 10), 3)  # left eye
pygame.draw.circle(robot_surface, (0, 0, 0), (TILE_SIZE - 10, 10), 3)  # right eye

# Draw mouth
pygame.draw.rect(robot_surface, (0, 0, 0), (10, 25, TILE_SIZE - 20, 5))

TILE_TYPES = {
    "A": {"surface": pygame.Surface((TILE_SIZE, TILE_SIZE)), "solid": False},
    "B": {"surface": pygame.Surface((TILE_SIZE, TILE_SIZE)), "solid": False},
    "R": {"surface": pygame.Surface((TILE_SIZE, TILE_SIZE)), "solid": False},
    "C": {"surface": pygame.Surface((TILE_SIZE, TILE_SIZE)), "solid": False},   # C = computer = solid
    "D": {"surface": pygame.Surface((TILE_SIZE, TILE_SIZE)), "solid": False},   # D = desk = solid
    "W": {"surface": pygame.Surface((TILE_SIZE, TILE_SIZE)), "solid": True},   # W = wall = solid
    "T": {"surface": pygame.Surface((TILE_SIZE, TILE_SIZE)), "solid": False},   # W = wall = solid
    "P": {"surface": robot_surface, "solid": True},   # W = wall = solid
    ".": {"surface": None, "solid": False},
}

# Fill tile colors
TILE_TYPES["A"]["surface"].fill((243, 240, 255))  # light tile
TILE_TYPES["B"]["surface"].fill((209, 196, 255))  # dark tile
TILE_TYPES["C"]["surface"].fill((255, 255, 255))  # computer (white)
TILE_TYPES["D"]["surface"].fill((28, 24, 23))  # asphalt (gray)
TILE_TYPES["W"]["surface"].fill((100, 100, 100))  # wall (dark gray)
TILE_TYPES["R"]["surface"].fill((201,47,26))  # wall (dark gray)
TILE_TYPES["T"]["surface"].fill((201,47,6))  # teleport

def draw_level(screen):
    for row_index, row in enumerate(TILEMAP):
        for col_index, tile in enumerate(row):
            tile_data = TILE_TYPES.get(tile)
            if tile_data and tile_data["surface"]:
                screen.blit(tile_data["surface"], (col_index * TILE_SIZE, row_index * TILE_SIZE))

def is_tile_blocked(x, y):
    col = x // TILE_SIZE
    row = y // TILE_SIZE
    try:
        tile_code = TILEMAP[row][col]
        return TILE_TYPES.get(tile_code, {}).get("solid", False)
    except IndexError:
        return True  # Out of bounds = blocked
    
def get_tile_at_pixel(x, y):
    col = x // TILE_SIZE
    row = y // TILE_SIZE
    try:
        return TILEMAP[row][col]
    except IndexError:
        return None