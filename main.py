import pygame
from game import Game
from settings import *

pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("My Pygame Game")
clock = pygame.time.Clock()

game = Game(screen)

running = True
while running:
    clock.tick(FPS)
    game.handle_events()
    game.update()
    game.draw(screen)
