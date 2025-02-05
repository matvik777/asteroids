import pygame
import random
from asteroid import Asteroid
from constants import *

class LevelManadger:
    def __init__(self, asteroids, updatables, drawables):
        self.asteroids = asteroids
        self.updatables = updatables
        self.drawables = drawables
        self.level = 1  # Текущий уровень
        self.spawn_new_wave()

    def spawn_new_wave(self):
        """Создает новую волну астероидов, увеличивая сложность."""
        num_asteroids = 2 + self.level  # Больше астероидов с каждым уровнем
        
        for _ in range(num_asteroids):
            x, y = self.get_spawn_position()
            radius = ASTEROID_MAX_RADIUS
            asteroid = Asteroid(x, y, radius)
            
            # Даем случайную скорость астероидам
            asteroid.velocity = pygame.Vector2(random.uniform(-100, 100), random.uniform(-100, 100))
            
        print(f"🌍 Новый уровень: {self.level}. Астероидов: {num_asteroids}")

    def get_spawn_position(self):
        """Генерирует случайную позицию появления астероидов."""
        edge = random.choice(["top", "bottom", "left", "right"])
        
        if edge == "top":
            return random.randint(0, SCREEN_WIDTH), -ASTEROID_MAX_RADIUS
        elif edge == "bottom":
            return random.randint(0, SCREEN_WIDTH), SCREEN_HEIGHT + ASTEROID_MAX_RADIUS
        elif edge == "left":
            return -ASTEROID_MAX_RADIUS, random.randint(0, SCREEN_HEIGHT)
        else:
            return SCREEN_WIDTH + ASTEROID_MAX_RADIUS, random.randint(0, SCREEN_HEIGHT)

    def update(self, dt):
        """Проверяет, уничтожены ли все астероиды, и запускает новую волну."""
        if len(self.asteroids) == 0:  # Все астероиды уничтожены
            self.level += 1
            self.spawn_new_wave()
