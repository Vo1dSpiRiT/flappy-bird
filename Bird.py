import pygame
import os
from pygame.math import Vector2
from PhysicsObject import PhysicsObject

class Bird(PhysicsObject):
    def __init__(self, surface, x, y, gravity=0, mass=1):
        super().__init__(gravity, mass)
        self.surface = surface
        self.position = Vector2(x, y)
        self.dimensions = Vector2(26, 19) * 2.2
        self.angle = 0
        self.maxUpwardAngle = 20
        self.jumpValue = -10
        self.BIRD_IMAGES = self.getBirdImages()
        self.onGround = False
        self.score = 0
        self.rect = self.BIRD_IMAGES[0].get_rect(center=(self.position.x, self.position.y))
        self.selectedImage = self.BIRD_IMAGES[0]
        self.animationCount = 0
        self.animationCycle = 0.6
        self.currentAnimationDelay = 0
        

    def getBirdImages(self):
        gameImage = pygame.image.load(os.path.join('Assets','GameImages.png'))
        gameImages = []
        for i in range(2, -1, -1):
            croppedRegion = ((i * 44) + 5, 767, 26, 19)
            gameImages.append(pygame.transform.scale(gameImage.subsurface(croppedRegion),(int(self.dimensions.x), int(self.dimensions.y))))
        return gameImages
        
    def draw(self):
        self.surface.blit(self.selectedImage, self.rect)
        
        
    def update(self, dt, TPF, floorHeight):
        self.checkGround(floorHeight)
        if not self.onGround:
            self.applyGravity()
            self.applyForces(dt, maxDVel=12)
            self.resetForce()
            self.updateAngle()
            self.updateAnimationCount(TPF)
        self.getSelectedImage()
        self.updateRotation()
        self.updatePosition()

    def updateAnimationCount(self, TPF):
        self.currentAnimationDelay += TPF
        if self.angle == -90:
            self.animationCount = 1
        elif self.currentAnimationDelay > self.animationCycle / len(self.BIRD_IMAGES):
            self.animationCount += int(self.currentAnimationDelay / (self.animationCycle / len(self.BIRD_IMAGES)))
            self.currentAnimationDelay = 0
        self.animationCount %= 3
        
    def getSelectedImage(self):
        self.selectedImage = self.BIRD_IMAGES[self.animationCount]
            
        
    def updatePosition(self):
        self.rect.center = (self.position.x, self.position.y)

    def updateRotation(self):
        self.selectedImage = pygame.transform.rotozoom(self.selectedImage, self.angle, 1)
        self.selectedRect = self.selectedImage.get_rect(center=self.position)

    def updateAngle(self):
        if self.velocity.y < 5:
            self.angle = self.maxUpwardAngle
        elif self.angle > -90:
            self.angle -= 6
            
        if self.angle < -90:
            self.angle = -90
            
    def checkGround(self, floorHeight):
        if self.position.y + (self.dimensions.y / 2) >= floorHeight:
            self.onGround = True
        
    def jump(self):
        self.velocity = Vector2(0, self.jumpValue)


    