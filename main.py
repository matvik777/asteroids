# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
from constants import *
def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))  # Создаем окно
    pygame.display.set_caption("Asteroids Game")  # Устанавливаем заголовок окна
    while True:
    	for event in pygame.event.get():
    		if event.type == pygame.QUIT:
        		return
    
    screen.fill(black)
    pygame.display.flip()
   
   
   
    print('''
	
 	Starting asteroids!
	Screen width: 1280
	Screen height: 720	
	''')

if __name__ == "__main__":
    main()
