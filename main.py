import pygame
from constants import *
from player import Player
from asteroidfield import *
from shot import Shot 
from asteroid import Asteroid
def main():
    pygame.init()
    pygame.font.init()
    font = pygame.font.SysFont(None, 36)
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
     
    dt = 0
    
    
    updatables = pygame.sprite.Group()
    drawbles = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    
    Shot.containers = (shots, updatables, drawbles)
    Player.containers = (updatables, drawbles)
    Asteroid.containers = (asteroids, updatables, drawbles)
    AsteroidField.containers = (updatables,)
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    asteroid_field = AsteroidField()
    
    score = 0
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        updatables.update(dt)
        
        for asteroid in asteroids:
            for shot in shots:
                if shot.collides_with(asteroid):
                    shot.kill()
                    asteroid.split()
                    score += 100
                    
        for asteroid in asteroids:
            if player.collides_with(asteroid):
                print("Game over!")
                return  # Завершение программы

        screen.fill("black")
        for sprite  in drawbles:
            sprite.draw(screen)
            
        score_text = font.render(f"Score: {score}", True, (255,255,255))
        screen.blit(score_text, (10,10))
        pygame.display.flip()

        # limit the framerate to 60 FPS
        dt = clock.tick(60)/1000


if __name__ == "__main__":
    main()
