from MapTools.Rectangle import Rectangle

class Map:
    def __init__(self, background_color, screen):
        self.screen = screen
        self.rects = []
        self.background_color = background_color

    def build(self):
        self.screen.fill(self.background_color)

        y = 40
        x= 40
        while y < 560:
            while x < 560:
                new_rect = Rectangle((x, y), 100, (208, 208, 208))
                new_rect.draw_rect(self.screen)
                self.rects.append(new_rect)
                x += 105
            
            x = 40
            y += 105

    def getRects(self):
        return self.rects