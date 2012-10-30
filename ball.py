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
        # Ball is out of bounds
        elif self.left < 0 or self.right > self.game.screen.get_width():
            if self.left < 0:
                self.game.score.incrementScoreFor("p2")
            else:
                self.game.score.incrementScoreFor("p1")

            # Reset the ball in the center
            self.top = self.game.screen.get_height()/2
            self.left = self.game.screen.get_width()/2
            self.setSpeed(random.random()*14-7, random.random()*14-7)

            # Give the players a break!
            self.waitFor = 20
                        
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
