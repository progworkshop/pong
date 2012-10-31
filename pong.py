# pong.py
# A basic game for our prog workshop!

import pygame
import random
from ball import Ball
from paddle import Paddle
from scoreboard import Scoreboard

class Pong:
    def __init__(self, width=640, height=480, title="Prog Workshop - Pong!"):
        pygame.init()

        # Sets key repeat to a max of once every 5 ms
        #pygame.key.set_repeat(5, 5)
        self.screen = pygame.display.set_mode((width, height))
        pygame.display.set_caption(title)
        self.clock = pygame.time.Clock()
        self.screen = pygame.display.get_surface()
        self._running = True
        
        self.player1 = Paddle(0,0,20,100,self)
        self.player2 = Paddle(width-20,0,20,100,self)
        
        self.ball = Ball(width/2,height/2,20,20,self)
        self.ball.setSpeed(random.random()*14-7, random.random()*14-7)

        self.balls = []

        self.score = Scoreboard(self, 36)

    def handle_event(self, event):
        if event.type == pygame.QUIT:
            self._running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            ball = Ball(self.screen.get_width()/2,self.screen.get_height()/2,20,20,self)
            ball.setSpeed(random.random()*14-7, random.random()*14-7)
            self.balls.append(ball)
            
    def update_game(self):
        keys_pressed = pygame.key.get_pressed()
        if keys_pressed[pygame.K_UP]:
            self.player2.moveUp()
        if keys_pressed[pygame.K_DOWN]:
            self.player2.moveDown()
        if keys_pressed[pygame.K_w]:
            self.player1.moveUp()
        if keys_pressed[pygame.K_s]:
            self.player1.moveDown()
        self.ball.update()
        for ball in self.balls:
            ball.update()
    
    def render(self):
        background = pygame.Surface(self.screen.get_size()).convert()
        background.fill((250, 250, 250))
        self.screen.blit(background, (0,0))

        self.player1.render()
        self.player2.render()
        
        self.ball.render()

        for ball in self.balls:
            ball.render()

        self.score.renderScore()
        
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

if __name__ == "__main__":
    pong = Pong()
    pong.start()
