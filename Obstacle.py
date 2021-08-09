import pygame
import os
from random import randint
from pygame.math import Vector2



class Obstacle():
    def __init__(self, surface, gapHeight, velocity):
        self.surface = surface
        self.gapHeight = min(gapHeight, self.surface.get_height() - 200)
        self.dimensions = Vector2(117, 744)
        self.position = Vector2(self.surface.get_width() + 500,
                                randint(self.gapHeight/2 + 50, (self.surface.get_height() - self.gapHeight/2 - 150)))
        self.velocity = velocity
        self.passed = False
        self.downwardTubeImage = self.getDownwardTubeImage()
        self.upwardTubeImage = self.getUpwardTubeImage()
        self.upwardTubeRect = self.getUpwardTubeRect()
        self.downwardTubeRect = self.getDownwardTubeRect()

    def move(self, dt):
        self.position.x -= self.velocity * dt
        
    def getUpwardTubeImage(self):
        gameImage = pygame.image.load(os.path.join('Assets','GameImages.png'))
        croppedRegion = (44, 504, 41, 250)
        return pygame.transform.scale(gameImage.subsurface(croppedRegion), (int(self.dimensions.x), int(self.dimensions.y)))

    def getDownwardTubeImage(self):
        gameImage = pygame.image.load(os.path.join('Assets','GameImages.png'))
        croppedRegion = (88, 504, 41, 250)
        return pygame.transform.scale(gameImage.subsurface(croppedRegion), (int(self.dimensions.x), int(self.dimensions.y)))

    def getUpwardTubeRect(self):
        return self.upwardTubeImage.get_rect(center=(self.position.x, self.position.y + self.dimensions.y / 2 + self.gapHeight / 2))

    def getDownwardTubeRect(self):
        return self.downwardTubeImage.get_rect(center=(self.position.x, self.position.y - self.dimensions.y / 2 - self.gapHeight / 2))

    def update(self):
        self.upwardTubeRect = self.getUpwardTubeRect()
        self.downwardTubeRect = self.getDownwardTubeRect()

    def draw(self):
        self.surface.blit(self.upwardTubeImage, self.upwardTubeRect)
        self.surface.blit(self.downwardTubeImage, self.downwardTubeRect)