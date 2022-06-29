import pygame
import sys

class InputManager:
    def __init__(self, new_map):
        self.map = new_map
        self.current_rect = 0
        self.current_line = 40
        self.word = 'HOLAS'

    def check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT: sys.exit()
            
            if event.type == pygame.KEYDOWN:

                if (event.key == pygame.K_BACKSPACE): # Cases in which the user wants to erase
                    if(self.map.getRect(self.current_rect - 1).getY() == self.current_line):
                        self.current_rect -= 1
                        self.map.getRect(self.current_rect).empty_letter()
                
                elif(event.key != pygame.K_RETURN): # Cases in which the user wants to write
                    if(self.map.getRect(self.current_rect).getY() == self.current_line):
                        self.map.getRect(self.current_rect).set_letter(event.unicode.upper()) 
                        self.current_rect += 1

                else: # Cases in which the user wants to check the word
                    if(self.current_rect % 5 == 0):
                        self.check_line()
                        
                        self.current_line += 105

    def write_rects(self):
        for rect in self.map.getRects():
            text_surface = rect.get_rect_font().render(rect.get_letter(), True, rect.get_letter_color())
            self.map.screen.blit(text_surface, (rect.get_input_rect().x+5, rect.get_input_rect().y+5))

    def check_line(self):
        aux = self.current_rect - 5
        for i in range(0, 5):
            rect = self.map.getRect(aux)
            if rect.get_letter() == self.word[i]:
                rect.setColor((154,205,50))
            else:
                rect.setColor((250,128,114))
            aux += 1