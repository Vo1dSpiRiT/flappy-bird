import pygame
from pygame.math import Vector2
from Scripts.Bird import Bird
from Scripts.Environment import Environment
pygame.font.init()

resolution = Vector2(450, 700)
WIN = pygame.display.set_mode((int(resolution.x), int(resolution.y)))
pygame.display.set_caption("FLAPPY BIRD!")

textFont = pygame.font.SysFont('comicsans', 20)
scoreFont = pygame.font.SysFont('comicsans', 30)
TARGET_FPS = 60
GRAVITY = 0.7

environment = None
bird = None

def draw_window(TimePerFrame, score):
    environment.draw()
    bird.draw()
    drawFPS(TimePerFrame)
    drawScore(score)
    pygame.display.update()
    
def getFPS(TimePerFrame):
    return round(1 / TimePerFrame)

def drawFPS(TimePerFrame):
    CurrentFPS = getFPS(TimePerFrame)
    FPS_Text = textFont.render("FPS: "  + str(CurrentFPS), 1, (255, 255, 255))
    WIN.blit(FPS_Text, (int(resolution.x) - 80, -4))
    
def drawScore(score):
    score_Text = scoreFont.render("Score: " + str(score), 1, (255, 255, 255))
    WIN.blit(score_Text, ((resolution.x - score_Text.get_width())//2, 50))

def collided(bird, obstacles):
    if bird.onGround:
        return True
    for obstacle in obstacles:
        if bird.rect.colliderect(obstacle):
            return True
    return False

def getNextObstacles(bird, obstacles):
    nextObstacles = []
    for obstacle in obstacles:
        if obstacle[0].x + obstacle[0].width < bird.position.x - bird.dimensions.x/2:
            nextObstacles.append(obstacle)
    
def setup():
    global bird, environment
    bird = Bird(WIN, 100, 100, GRAVITY)
    environment = Environment(WIN)

def main():
    clock = pygame.time.Clock()
    running = True
    lost = False
    setup()
    floorHeight = environment.getFloorHeight()
    while running:
        TimePerFrame  = clock.tick(60) * .001
        dt = TimePerFrame * TARGET_FPS

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    bird.jump()
                    
        environment.update(dt, TimePerFrame, lost)
        bird.update(dt, TimePerFrame, floorHeight)
        lost = collided(bird, environment.getObstacleRects())
        if lost:
            setup()
            lost = False
            bird.score = 0
        if environment.passedObstacle(bird):
            bird.score += 1
        draw_window(TimePerFrame, score=bird.score)

    pygame.quit()



if __name__ == "__main__":
    main()
