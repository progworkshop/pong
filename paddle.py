import pygame

class Paddle(pygame.Rect):
    def moveUp(self):
        if self.top >= 10:
            self.top -= 10

    def moveDown(self):
        if self.bottom <= 480:
            self.top += 10

    def render(self, screen):
        pygame.draw.rect(screen, (0,0,0), self)

