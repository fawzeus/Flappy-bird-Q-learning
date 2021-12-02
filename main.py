from typing_extensions import runtime
import pygame
from pygame.constants import QUIT, SRCCOLORKEY
import random
import time
from Bird_Class import Bird

weidth = 280
height = 500
ground_scroll = 0
scroll_speed = 0.5
screen=pygame.display.set_mode((weidth,height))
pygame.display.set_caption("Flappy Bird")
base = pygame.image.load("images/base.png")
sky=pygame.image.load("images/background-day.png")
birds =["images/redbird-downflap.png","images/yellowbird-downflap.png","images/bluebird-downflap.png"]
icon = pygame.image.load("images/flappy.ico")
pygame.display.set_icon(icon)
bird_path = random.choice(birds)
bird = pygame.image.load(bird_path)
running = True
gameover=pygame.image.load("images/gameover.png")
bird = Bird(20,200)
i=0
while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            bird.jump()
            if bird.is_not_flying():
                bird.start_flying()
    screen.blit(sky,(0,0))
    #screen.blit(bird,(50,50))
    if bird.is_flying():
        ground_scroll-= scroll_speed
    if abs(ground_scroll) > 20 :
        ground_scroll = 0
    bird.display(screen)
    bird.update()
    bird.check_if_game_over()
    if bird.game_is_over():
        screen.blit(gameover,(40,100))
    screen.blit(base, (ground_scroll, 400)) 
    pygame.display.update()