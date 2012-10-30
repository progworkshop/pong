import pygame
import random

class Ball(pygame.Rect):
    def __init__(self, left, top, width, height, game):
        super(Ball, self).__init__(left, top, width, height)
        self.game = game
    
    def setSpeed(self, x, y):
        self.speed = [x,y]

    def update(self):
        self.top += self.speed[1]
        self.left += self.speed[0]

        if self.colliderect(self.game.player1) or self.colliderect(self.game.player2):
            self.speed[0] = -self.speed[0]*1.2
        """The above case handles if we are blocked, but that may not always be the case.
            We also need to account for scoring against a player.
            A ball should check its position and if it has gone offscreen, it should
            let the scoreboard know who scored and then respawn itself to continue the game."""
                        
        if self.top < 0 or self.bottom > self.game.screen.get_height():
            self.speed[1] = -self.speed[1]
        
    
    def render(self):
        pygame.draw.circle(self.game.screen, (0,0,0), (self.left+self.width/2, self.top+self.width/2), self.width/2)
