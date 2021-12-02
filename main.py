import pygame
import random
import time
from Bird_Class import Bird
from Pipe_Class import Pipe
weidth = 280
height = 500
ground_scroll = 0
scroll_speed = 2

clock =pygame.time.Clock()
frequency = 3000
last_pipe = pygame.time.get_ticks() - frequency


fps =60
images = ["images/pipe-red.png","images/pipe-green.png"]
screen=pygame.display.set_mode((weidth,height))
pygame.display.set_caption("Flappy Bird")
base = pygame.image.load("images/base.png")
sky=pygame.image.load("images/background-day.png")

icon = pygame.image.load("images/flappy.ico")
pygame.display.set_icon(icon)

running = True
gameover=pygame.image.load("images/gameover.png")
bird = Bird(20,200)

pipe_group = pygame.sprite.Group()
bird_group = pygame.sprite.Group()
bird_group.add(bird)


while running:

    
    clock.tick(fps)
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
        pipe_group.update()
        time_now = pygame.time.get_ticks()
        if time_now -last_pipe > frequency:
            pipe_height = random.randint(70,260)
            path = random.choice(images)
            btm_pipe =Pipe(path,weidth,pipe_height,-1)
            top_pipe =Pipe(path,weidth,pipe_height,1)
            pipe_group.add(btm_pipe,top_pipe)
            last_pipe = time_now
    if abs(ground_scroll) > 20 :
        ground_scroll = 0

    if pygame.sprite.groupcollide(bird_group,pipe_group,False,False):
        bird.make_game_over()

    pipe_group.draw(screen)
    bird.display(screen)
    bird.update()
    bird.check_if_game_over()
    screen.blit(base, (ground_scroll, 400)) 
    if bird.game_is_over():
        screen.blit(gameover,(40,100))
    pygame.display.update()