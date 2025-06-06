import os
# This stops pygame from printing its initialization message
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"
import pygame
os.environ['SDL_AUDIODRIVER'] = 'dummy' # ignore sound errors, maybe remove later
from constants import *
from player import *
from asteroid import *
from asteroidfield import *



def main():
    
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    pygame.init()
    clock = pygame.time.Clock()
    dt = 0

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    

    
    Player.containers = (updatable,drawable)
    Asteroid.containers = (asteroids,updatable,drawable)
    AsteroidField.containers = (updatable)
    Shot.containers = (updatable,drawable,shots)


    player = Player(SCREEN_WIDTH/2,SCREEN_HEIGHT/2)
    asteroidfield = AsteroidField()

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        screen.fill("black")
        updatable.update(dt)

        for ast in asteroids:
            if ast.collision(player):
                print("Game over!")
                return
            for s in shots:
                if ast.collision(s):
                    s.kill()
                    ast.split()


        for drawables in drawable:
            drawables.draw(screen)
        
        pygame.display.flip()

        dt = clock.tick(60)/1000        




if __name__ == "__main__":
    main()