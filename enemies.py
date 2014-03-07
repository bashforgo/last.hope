import pygame
import random
import math
import helper
from constants import (SCREEN_WIDTH, SCREEN_HEIGHT)


class Asteroid(pygame.sprite.Sprite):

    def __init__(self,pos,size):
        pygame.sprite.Sprite.__init__(self)
        self.size = size
        if size == 0:
            self.baseImage = pygame.image.load("asteroid0.tga")
            self.where = random.randrange(1,5)
            if self.where == 1:
                self.center = [random.randrange(-300,0),random.randrange(-300,SCREEN_HEIGHT+300)]
            elif self.where == 2:
                self.center = [random.randrange(SCREEN_WIDTH,SCREEN_WIDTH+300),random.randrange(-300,SCREEN_HEIGHT+300)]
            elif self.where == 3:
                self.center = [random.randrange(-300,SCREEN_WIDTH+300),random.randrange(-300,0)]
            elif self.where == 4:
                self.center = [random.randrange(SCREEN_HEIGHT,SCREEN_HEIGHT+300),random.randrange(-300,SCREEN_HEIGHT+300)]
        if size == 1:
            self.baseImage = pygame.image.load("asteroid10.tga")
        if size == 2:
            self.baseImage = pygame.image.load("asteroid11.tga")
        if size == 3:
            self.baseImage = pygame.image.load("asteroid20.tga")
        if size == 4:
            self.baseImage = pygame.image.load("asteroid21.tga")
        if size == 1 or size == 2 or size == 3 or size == 4:
            self.center = pos
            self.angle = random.randrange(0,360)
        self.rect = pygame.rect.Rect(self.center,self.baseImage.get_size())
        if size == 0:
            self.angle = random.randrange(50,150)/100*math.degrees(math.atan2(self.rect.center[0]-pos[0], self.rect.center[1]-pos[1]))
        self.speed = random.triangular(1.0, 4.0)
        self.speedx =  self.speed*math.cos(math.radians(self.angle+90))
        self.speedy = -self.speed*math.sin(math.radians(self.angle+90))
        self.rotaSpeed = random.randrange(0,7)
        self.angle = random.randrange(0,360)

    def update(self):
        self.angle += self.rotaSpeed
        self.image,self.rect = helper.rot_center(self.baseImage, self.rect, self.angle)
        if self.rect.left>SCREEN_WIDTH:
            self.rect.right=0
        if self.rect.top>SCREEN_HEIGHT:
            self.rect.bottom=0
        if self.rect.right<0:
            self.rect.left=SCREEN_WIDTH
        if self.rect.bottom<0:
            self.rect.top=SCREEN_HEIGHT
        self.rect.x += self.speedx
        self.rect.y += self.speedy