# pong.py
# A basic game for our prog workshop!

import pygame

class Pong:
    def __init__(self, width=640, height=480, title="Prog Workshop - Pong!"):
        pygame.init()
        self.screen = pygame.display.set_mode((width, height))
        pygame.display.set_caption(title)
        self.clock = pygame.time.Clock()
        self.screen = pygame.display.get_surface()
        self._running = True

    def handle_event(self, event):
        if event.type == pygame.QUIT:
            self._running = False        

    def update_game(self):
        pass
    
    def render(self):
        background = pygame.Surface(self.screen.get_size()).convert()
        background.fill((250, 250, 250))
        self.screen.blit(background, (0,0))
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
