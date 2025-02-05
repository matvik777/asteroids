import pygame
from constants import *
from circleshape import CircleShape
import random


class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
     # Базовая форма астероида, нормализованная по размеру
        base_points = [
            (-0.9, -0.3), (-0.4, -1), (0.4, -0.8),
            (1, -0.2), (0.8, 0.5), (0, 1), (-0.6, 0.6)
        ]
    
    # Масштабируем точки в зависимости от радиуса астероида
        points = [(self.position.x + x * self.radius, self.position.y + y * self.radius) 
                for x, y in base_points]
    
        pygame.draw.polygon(screen, "white", points, 2)


    def update(self, dt):
        self.position += self.velocity * dt
        
        if self.position.x > SCREEN_WIDTH + self.radius:
            self.position.x = -self.radius
        elif self.position.x < -self.radius:
            self.position.x = SCREEN_WIDTH + self.radius
        
        if self.position.y > SCREEN_HEIGHT + self.radius:
            self.position.y = -self.radius
        elif self.position.y < -self.radius:
            self.position.y = SCREEN_HEIGHT + self.radius
    
    def split(self):
        self.kill()
        
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        
        random_angle = random.uniform(20, 50)
        
        velocity1 = self.velocity.rotate(random_angle) *1.2
        velocity2 = self.velocity.rotate(-random_angle) *1.2
        
        new_radius = self.radius - ASTEROID_MIN_RADIUS
        
        asteroid1 = Asteroid(self.position.x, self.position.y, new_radius)
        asteroid2 = Asteroid(self.position.x, self.position.y, new_radius)
        
        asteroid1.velocity = velocity1
        asteroid2.velocity = velocity2