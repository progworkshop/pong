import pygame

class Scoreboard(pygame.font.Font):
    def __init__(self, size, p1score, p2score, game):
            super(Scoreboard, self).__init__(None, size)
            self.p1score = p1score
            self.p2score = p2score
            self.game = game

    def renderScore(self):
        text = self.render("%d - %d" % (self.p1score, self.p2score), 1, (10,10,10))
        textpos = text.get_rect(centerx=self.game.screen.get_width()/2)
        self.game.screen.blit(text, textpos)

    def incrementScoreFor(self, player):
        if player == "p1":
            self.p1score += 1
        if player == "p2":
            self.p2score += 1
