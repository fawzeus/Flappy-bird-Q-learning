import pygame
import random
class Bird(pygame.sprite.Sprite):
    birds = [["images/redbird-downflap.png","images/redbird-midflap.png","images/redbird-upflap.png"],["images/yellowbird-downflap.png","images/yellowbird-midflap.png","images/yellowbird-upflap.png"],["images/bluebird-downflap.png","images/bluebird-midflap.png","images/bluebird-upflap.png"]]
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.game_over=False
        self.index=0
        self.Flying = False
        self.counter=0
        self.images=random.choice(self.birds)
        self.images =[pygame.image.load(i) for i in self.images]
        self.image= self.images[self.index]
        self.rect=self.image.get_rect()
        self.rect.center = [x,y]
        self.x=x
        self.y=y
        self.vel=0
    def update(self):
        if self.Flying:
            if self.vel<=8:
                self.vel+=0.5
            if self.y <=370 :
                self.y+= int (self.vel)
            if self.y<0:
                self.y=0
            if self.counter >= 50:
                self.index+=1
                self.index%=3
                self.counter=0
                self.image=self.images[self.index]
            else:
                self.counter+=1
            
            #rotate the bird
            self.image =pygame.transform.rotate(self.images[self.index],self.vel*-4)
        if self.game_over:
            self.image =pygame.transform.rotate(self.images[self.index],-90)

    def display(self,screen):
        screen.blit(self.image,(self.x,self.y))
    def jump(self):
        self.vel= -8
    def start_flying(self):
        self.Flying=True
    def is_not_flying(self):
        return self.Flying == False
    def is_flying(self):
        return self.Flying
    def check_if_game_over(self):
        if self.y>=370:
            self.Flying=False
            self.game_over=True
    def game_is_over(self):
        return self.game_over
    def make_game_over(self):
        self.game_over = True
        self.Flying = False

