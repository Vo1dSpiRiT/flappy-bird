import pygame
import os
from math import ceil
from pygame.math import Vector2


class Floor():
    def __init__(self, surface, velocity):
        self.surface = surface
        self.dimensions = Vector2(251, 85) * 2.5
        self.velocity = velocity
        self.floorImage = self.getFloorImage()
        self.ImageCount = ceil(self.surface.get_width() / self.dimensions.x) + 1
        self.position = self.getPosition()
        
    def getFloorImage(self):
        gameImage = pygame.image.load(os.path.join('Assets','GameImages.png')).convert()
        croppedRegion = (460, 0, 251, 85)
        return pygame.transform.scale(gameImage.subsurface(croppedRegion), (int(self.dimensions.x), int(self.dimensions.y)))

    def getPosition(self):
        x = 0
        height = min(0.12 * self.surface.get_height(), 90)
        y = self.surface.get_height() - height
        return Vector2(x, y)
    
    def getHeight(self):
        return self.position.y

    def update(self, dt):
        self.position.x -= self.velocity * dt
        if self.position.x <= -self.dimensions.x:
            self.position.x = 0

    def draw(self):
        for i in range(self.ImageCount):
            self.surface.blit(self.floorImage,((i * (self.dimensions.x) + self.position.x), self.position.y))