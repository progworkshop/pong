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
        elif self.left < 0 or self.right > self.game.screen.get_width():
            self.top = self.game.screen.get_height()/2
            self.left = self.game.screen.get_width()/2
            self.setSpeed((random.random()+1)*7-5, (random.random()+1)*7-5)
            
        if self.top < 0 or self.bottom > self.game.screen.get_height():
            self.speed[1] = -self.speed[1]
        
    
    def render(self):
        pygame.draw.circle(self.game.screen, (0,0,0), (self.left+self.width/2, self.top+self.width/2), self.width/2)
