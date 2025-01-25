# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
from constants import *

def main():
    pygame.init()

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))  # Создаем окно
    pygame.display.set_caption("Asteroids Game")  # Устанавливаем заголовок окна
    clock = pygame.time.Clock()  # Создаем объект Clock
    dt = 0  # Переменная для хранения delta time
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        screen.fill((0,0,0))  # Теперь внутри цикла
        pygame.display.flip()  # Теперь внутри цикла
        dt = clock.tick(60)   # Переводим миллисекунды в секунды
 
    print('''
    
    Starting asteroids!
    Screen width: 1280
    Screen height: 720    
    ''')

if __name__ == "__main__":
    main()
