import pygame
from constants import *
from circleshape import CircleShape
from shot import Shot

class Player(CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, PLAYER_RADIUS)
        self.rotation = 0
        self.shoot_timer = 0

    def draw(self, screen):
        pygame.draw.polygon(screen, "white", self.triangle(), 2)

    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]

    def update(self, dt):
        if self.shoot_timer > 0:
            self.shoot_timer -= dt
        keys = pygame.key.get_pressed()
        
        if keys[pygame.K_a]:
            self.rotate(-dt)
        if keys[pygame.K_d]:
            self.rotate(dt)
        forward = pygame.   Vector2(0, 1).rotate(self.rotation)
        if keys[pygame.K_w]:
            self.velocity += forward * (PLAYER_ACCELERATION * dt)
        if keys[pygame.K_s]:
            self.velocity -= forward * (PLAYER_ACCELERATION * dt)
        self.velocity *= PLAYER_FRICTION
        self.position += self.velocity * dt
        if keys[pygame.K_SPACE]:
            self.shoot()
        
    def rotate(self, dt):
        self.rotation += PLAYER_TURN_SPEED * dt

    def move(self, dt):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        self.position += forward * PLAYER_SPEED * dt

    def shoot(self):
        if self.shoot_timer > 0:  
            return
        
        self.shoot_timer = PLAYER_SHOOT_COOLDOWN 
        direction = pygame.Vector2(0, 1).rotate(self.rotation)

        tip_position = self.position + direction * self.radius
        # Создаём объект Shot в **вершине треугольника**
        shot = Shot(tip_position.x, tip_position.y)
        shot.velocity = direction * PLAYER_SHOOT_SPEED