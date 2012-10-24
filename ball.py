import pygame
import random

class Ball(pygame.Rect):
    def setSpeed(self, x, y):
        self.speed = [x,y]

    def update(self, screen, player1, player2):
        # Passing these args isn't too great
        # It'd be easier to change the constructor to take in the Pong game
        
        self.top += self.speed[1]
        self.left += self.speed[0]

        if self.colliderect(player1) or self.colliderect(player2):
            self.speed[0] = -self.speed[0]*1.2
        elif self.left < 0 or self.right > screen.get_width():
            self.top = 240
            self.left = 320
            self.setSpeed((random.random()+1)*7-5, (random.random()+1)*7-5)
            
        if self.top < 0 or self.bottom > screen.get_height():
            self.speed[1] = -self.speed[1]
        
    
    def render(self, screen):
        pygame.draw.circle(screen, (0,0,0), (self.left+self.width/2, self.top+self.width/2), self.width/2)
