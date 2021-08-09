from Background import Background
from Floor import Floor
from Obstacles import Obstacles


class Environment():
    def __init__(self, surface):
        self.surface = surface
        self.background = Background(surface)
        self.velocity = 4
        self.floor = Floor(surface, self.velocity)
        self.obstacles = Obstacles(surface, self.velocity)

    def getObstacleRects(self):
        return self.obstacles.getRects()
        
    def getFloorHeight(self):
        return self.floor.getHeight()
        
    def update(self, dt, TPF, lost):
        if not lost:
            self.floor.update(dt)
            self.obstacles.update(dt, TPF)
            
    def passedObstacle(self, bird):
        passed = False
        for obstacle in self.obstacles.pipes:
            if not obstacle.passed and obstacle.position.x < bird.position.x:
                obstacle.passed = True
                passed = True
        return passed
        
    def draw(self):
        self.background.draw()
        self.obstacles.draw()
        self.floor.draw()

        
        
