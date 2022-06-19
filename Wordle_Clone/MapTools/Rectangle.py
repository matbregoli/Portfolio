import pygame

class Rectangle:

    def __init__(self, coords, width, rect_color):
        self.outline_rect = pygame.Rect(coords[0], coords[1], width, width)
        self.rect_color = rect_color
        self.input_rect = pygame.Rect(coords[0]+25, coords[1]+20, width, width)
        self.input_color = (0,0,0)
        self.base_font = pygame.font.SysFont(None, 80)
        self.letter = 'm'

    def draw_rect(self, screen):
        pygame.draw.rect(screen, self.rect_color, self.outline_rect, 2, 3)

    def get_rect_font(self):
        return self.base_font

    def get_letter(self):
        return self.letter

    def get_letter_color(self):
        return self.input_color

    def get_input_rect(self):
        return self.input_rect