import pygame

class Paddle(pygame.Rect):
    def __init__(self, left, top, width, height, game):
        super(Paddle, self).__init__(left, top, width, height)
        self.game = game
    
    def moveUp(self):
        if self.top >= 10:
            self.top -= 10

    def moveDown(self):
        if self.bottom <= self.game.screen.get_height():
            self.top += 10

    def render(self):
        pygame.draw.rect(self.game.screen, (0,0,0), self)

