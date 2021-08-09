from pygame.math import Vector2

class PhysicsObject():
    def __init__(self, gravity, mass):
        self.mass = mass
        self.gravity = gravity
        self.force = Vector2(0, 0)
        self.velocity = Vector2(0, 0)
        self.acceleration = Vector2(0, 0)
        
    def applyForces(self, dt=1, maxDVel=0, maxUVel=0, maxRVel=0,maxLVel=0):
        self.acceleration = self.force / self.mass
        self.velocity += self.acceleration * dt
        
        if maxDVel: self.limitDownwardVelocity(maxDVel)
        if maxUVel: self.limitUpwardVelocity(maxUVel)
        if maxRVel: self.limitRightVelocity(maxRVel)
        if maxLVel: self.limitLeftVelocity(maxLVel)
        
        self.position += self.velocity * dt + (self.acceleration * .5) * (dt * dt)

    def addForce(self, Vec):
        self.force += Vec

    def resetForce(self):
        self.force = Vector2(0, 0)

    def applyGravity(self):
        self.force += Vector2(0, self.gravity * self.mass)
        
    def limitDownwardVelocity(self, limit):
        if 0 < self.velocity.y > limit:
            self.velocity.y = limit
            
    def limitUpwardVelocity(self, limit):
        if 0 > self.velocity.y < limit:
            self.velocity.y = limit
            
    def limitRightVelocity(self, limit):
        if 0 < self.velocity.x > limit:
            self.velocity.x = limit
            
    def limitLeftVelocity(self, limit):
        if 0 > self.velocity.x < limit:
            self.velocity.x = limit