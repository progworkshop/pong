import pygame
import random

class Ball(pygame.Rect):
    def __init__(self, left, top, width, height, game):
        super(Ball, self).__init__(left, top, width, height)
        self.game = game
        self.waitFor = 0
    
    def setSpeed(self, x, y):
        self.speed = [x,y]

    def update(self):
        # This is used for waiting/delaying the game
        # You can freeze the ball in-place for self.waitFor frames.
        if self.waitFor > 0:
            self.waitFor -= 1
            return
        
        self.top += self.speed[1]
        self.left += self.speed[0]

        # Ball hit player1's paddle
        if (self.left <= self.game.player1.right and
            self.bottom >= self.game.player1.top and
            self.top <= self.game.player1.bottom):
            self.speed[0] *= -1.2
            self.left = self.game.player1.right
        # Ball hit player2's paddle
        elif (self.right >= self.game.player2.left and
            self.bottom >= self.game.player2.top and
            self.top <= self.game.player2.bottom):
            self.speed[0] *= -1.2
            self.right = self.game.player2.left
        """The above case handles if we are blocked, but that may not always be the case.
            We also need to account for scoring against a player.
            A ball should check its position and if it has gone offscreen, it should
            let the scoreboard know who scored and then respawn itself to continue the game."""
                        
        # Ball hit the top border
        if self.top <= 0:
            self.top = 0
            self.speed[1] = -self.speed[1]
        # Ball hit the bottom border
        elif self.bottom >= self.game.screen.get_height():
            self.bottom = self.game.screen.get_height()
            self.speed[1] = -self.speed[1]
    
    def render(self):
        pygame.draw.circle(self.game.screen, (0,0,0), (self.left+self.width/2, self.top+self.width/2), self.width/2)
