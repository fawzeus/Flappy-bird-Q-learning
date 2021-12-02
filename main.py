from typing_extensions import runtime
import pygame
from pygame.constants import QUIT

weidth = 864
height = 720

screen=pygame.display.set_mode((weidth,height))
pygame.display.set_caption("Flappy Bird")

running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False