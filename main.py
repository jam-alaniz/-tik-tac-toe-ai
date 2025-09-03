import pygame
from pygame.locals import *


pygame.init()

screen_width = 500
screen_height = 500


screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('TikTacToe')


def draw_grid():
    bg = (255, 255, 200)
    grid = (50, 50, 50)
    screen.fill(bg)
    for x in range(1,3):
        pygame.draw.line(screen, grid, (0, x * 166.6), (screen_width, x * 166.6))
        pygame.draw.line(screen, grid, (x * 166.6, 0), (x * 166.6, screen_height))




run = True

while run:
    draw_grid()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    
    pygame.display.update()