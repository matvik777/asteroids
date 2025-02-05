import pygame
from constants import *
from player import Player
from shot import Shot 
from asteroid import Asteroid
from record import game_over_screen, load_high_scores
from levelmanadger import LevelManadger

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
    
    
    while True:
        player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
        level_manager = LevelManadger(asteroids, updatables, drawbles)
        score = 0
        game_running = True

        while game_running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return

            updatables.update(dt)
            level_manager.update(dt)
            
            for asteroid in asteroids:
                for shot in shots:
                    if shot.collides_with(asteroid):
                        shot.kill()
                        asteroid.split()
                        score += 100
                        
            for asteroid in asteroids:
                if player.collides_with(asteroid):
                    game_running = False
                    break

            screen.fill("black")
            for sprite in drawbles:
                sprite.draw(screen)
                
            # Display current score
            score_text = font.render(f"Score: {score}", True, (255,255,255))
            screen.blit(score_text, (10,10))
            
            # Display high score
            high_scores = load_high_scores()
            if high_scores:
                high_score_text = font.render(f"High Score: {high_scores[0]['score']}", True, (255,255,255))
                screen.blit(high_score_text, (10,50))
            
            pygame.display.flip()
            dt = clock.tick(60)/1000

        # Clear all sprites
        for sprite in updatables:
            sprite.kill()
            
        # Show game over screen and handle high score input
        if game_over_screen(screen, score) is None:
            return

if __name__ == "__main__":
    main()