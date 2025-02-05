# record.py
import pygame
import json
import os
from constants import *

class InputBox:
    def __init__(self, x, y, w, h, text=''):
        self.rect = pygame.Rect(x, y, w, h)
        self.color = pygame.Color('lightskyblue3')
        self.text = text
        self.font = pygame.font.SysFont(None, 32)
        self.txt_surface = self.font.render(text, True, self.color)
        self.active = False

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.rect.collidepoint(event.pos):
                self.active = not self.active
            else:
                self.active = False
            self.color = pygame.Color('dodgerblue2') if self.active else pygame.Color('lightskyblue3')
        if event.type == pygame.KEYDOWN:
            if self.active:
                if event.key == pygame.K_RETURN:
                    return self.text
                elif event.key == pygame.K_BACKSPACE:
                    self.text = self.text[:-1]
                else:
                    if len(self.text) < 10:
                        self.text += event.unicode
                self.txt_surface = self.font.render(self.text, True, self.color)
        return None

    def draw(self, screen):
        screen.blit(self.txt_surface, (self.rect.x+5, self.rect.y+5))
        pygame.draw.rect(screen, self.color, self.rect, 2)

def load_high_scores():
    if os.path.exists('high_scores.json'):
        with open('high_scores.json', 'r') as f:
            return json.load(f)
    return []

def save_high_scores(scores):
    with open('high_scores.json', 'w') as f:
        json.dump(scores, f)

def game_over_screen(screen, score):
    font = pygame.font.SysFont(None, 48)
    input_box = InputBox(SCREEN_WIDTH/2 - 100, SCREEN_HEIGHT/2, 200, 32)
    high_scores = load_high_scores()
    
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return None
            
            name = input_box.handle_event(event)
            if name:
                high_scores.append({"name": name, "score": score})
                high_scores.sort(key=lambda x: x["score"], reverse=True)
                high_scores = high_scores[:5]  # Keep only top 5
                save_high_scores(high_scores)
                return True

        screen.fill("black")
        
        game_over_text = font.render("GAME OVER", True, (255, 255, 255))
        score_text = font.render(f"Score: {score}", True, (255, 255, 255))
        enter_name_text = font.render("Enter your name:", True, (255, 255, 255))
        
        screen.blit(game_over_text, (SCREEN_WIDTH/2 - game_over_text.get_width()/2, SCREEN_HEIGHT/3))
        screen.blit(score_text, (SCREEN_WIDTH/2 - score_text.get_width()/2, SCREEN_HEIGHT/3 + 50))
        screen.blit(enter_name_text, (SCREEN_WIDTH/2 - enter_name_text.get_width()/2, SCREEN_HEIGHT/2 - 40))
        
        input_box.draw(screen)
        
        # Display high scores
        y_offset = SCREEN_HEIGHT/2 + 50
        high_score_title = font.render("High Scores:", True, (255, 255, 255))
        screen.blit(high_score_title, (SCREEN_WIDTH/2 - high_score_title.get_width()/2, y_offset))
        
        for i, score_data in enumerate(high_scores):
            score_text = font.render(f"{score_data['name']}: {score_data['score']}", True, (255, 255, 255))
            screen.blit(score_text, (SCREEN_WIDTH/2 - score_text.get_width()/2, y_offset + 40 + i * 30))

        pygame.display.flip()
