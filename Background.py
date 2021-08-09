import pygame
import os
from math import ceil
from pygame.math import Vector2


class Background():
    def __init__(self, surface):
        self.surface = surface
        self.dimensions = self.getBackgroundDimensions()
        self.backgroundImage = self.getbackgroundImage()
        self.ImageCount = ceil(self.surface.get_width() / self.dimensions.x)
        
    def getbackgroundImage(self):
        gameImage = pygame.image.load(os.path.join('Assets','GameImages.png')).convert()
        croppedRegion = (1, 1, 223, 398)
        return pygame.transform.scale(gameImage.subsurface(croppedRegion), (int(self.dimensions.x), int(self.dimensions.y)))
    
    def getBackgroundDimensions(self):
        scaleRatio = (398 / self.surface.get_height())
        height = self.surface.get_height()
        width = 223 / scaleRatio
        return Vector2(int(width), int(height))
    
    def draw(self): 
        for i in range(self.ImageCount):
            self.surface.blit(self.backgroundImage, ((i * (self.dimensions.x)), 0))