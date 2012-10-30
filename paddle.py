import pygame

class Paddle(pygame.Rect):
    def __init__(self, left, top, width, height, game):
        super(Paddle, self).__init__(left, top, width, height)
        self.game = game
    
    def moveUp(self):
        """If there is sufficient room for me
            to move upward, set my position to
            the next discrete place I can be."""

    def moveDown(self):
        """If there is sufficient room for me
            to move downward, set my position to
            the next discrete place I can be."""

    def render(self):
        pygame.draw.rect(self.game.screen, (0,0,0), self)

