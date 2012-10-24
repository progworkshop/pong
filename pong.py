# pong.py
# A basic game for our prog workshop!

import pygame
import random

class Pong:
    def __init__(self, width=640, height=480, title="Prog Workshop - Pong!"):
        pygame.init()

        # Sets key repeat to a max of once every 5 ms
        pygame.key.set_repeat(5, 5)
        self.screen = pygame.display.set_mode((width, height))
        pygame.display.set_caption(title)
        self.clock = pygame.time.Clock()
        self.screen = pygame.display.get_surface()
        self._running = True
        
        self.player1 = Paddle(0,0,20,100)
        self.player2 = Paddle(width-20,0,20,100)
        
        self.ball = Ball(240,320,20,20)
        self.ball.setSpeed(random.random()*14-7, random.random()*14-7)

    def handle_event(self, event):
        if event.type == pygame.QUIT:
            self._running = False
        if event.type == pygame.KEYDOWN:
            # These should be put in a dict later on
            if event.key == 273: # Up arrow
                self.player1.moveUp()
            if event.key == 274: # Down
                self.player1.moveDown()
            if event.key == 119: # W
                self.player2.moveUp()
            if event.key == 115: # S
                self.player2.moveDown()
            #print event, event.unicode, event.key, event.mod

    def update_game(self):
        self.ball.update(self.screen, self.player1, self.player2)
    
    def render(self):
        background = pygame.Surface(self.screen.get_size()).convert()
        background.fill((250, 250, 250))
        self.screen.blit(background, (0,0))

        self.player1.render(self.screen)
        self.player2.render(self.screen)
        
        self.ball.render(self.screen)
        
        pygame.display.flip()
    
    def start(self):
        while self._running:
            self.clock.tick(60) # Limit to 60 fps
            
            # Handle events
            for event in pygame.event.get():
                self.handle_event(event)

            # Handle game logic
            self.update_game()

            # Handle rendering
            self.render()
            
        pygame.quit()

class Paddle(pygame.Rect):
    def moveUp(self):
        if self.top >= 10:
            self.top -= 10

    def moveDown(self):
        if self.bottom <= 480:
            self.top += 10

    def render(self, screen):
        pygame.draw.rect(screen, (0,0,0), self)

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
            self.setSpeed(random.random()*14-7, random.random()*14-7)
            
        if self.top < 0 or self.bottom > screen.get_height():
            self.speed[1] = -self.speed[1]
        
    
    def render(self, screen):
        pygame.draw.circle(screen, (0,0,0), (self.left+self.width/2, self.top+self.width/2), self.width/2)


if __name__ == "__main__":
    pong = Pong()
    pong.start()
