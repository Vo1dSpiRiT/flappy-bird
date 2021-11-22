from Scripts.Obstacle import Obstacle


class Obstacles:
    def __init__(self, surface, velocity):
        self.surface = surface
        self.pipes = []
        self.nextObstacleDelay = 1.3
        self.timePassed = self.nextObstacleDelay
        self.velocity = velocity
        
        
    def getRects(self):
        rects = []
        for pipe in self.pipes:
            rects.extend([pipe.upwardTubeRect, pipe.downwardTubeRect])

        return rects
        
    
    def addObstacle(self):
        self.pipes.append(Obstacle(self.surface, 200, self.velocity))

    def update(self, dt, TPF):
        self.timePassed += TPF
        if self.timePassed > self.nextObstacleDelay:
            self.timePassed = 0
            self.addObstacle()
        
        if self.pipes:
            if self.pipes[0].position.x < - self.pipes[0].dimensions.x:
                self.pipes.remove(self.pipes[0])
            for pipe in self.pipes:
                pipe.move(dt)
                pipe.update()

            
    def draw(self):
        for pipe in self.pipes:
            pipe.draw()