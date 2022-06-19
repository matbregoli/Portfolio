import pygame
import sys

class InputManager:
    def __init__(self, new_map):
        self.map = new_map

    def check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT: sys.exit()

    def write_rects(self):
        for rect in self.map.getRects():
            text_surface = rect.get_rect_font().render(rect.get_letter(), True, rect.get_letter_color())
            self.map.screen.blit(text_surface, (rect.get_input_rect().x+5, rect.get_input_rect().y+5))
            