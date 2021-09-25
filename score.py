import pygame as pg



class Score(pg.sprite.Sprite):

    SCORE_LEFT = 0
    SCORE_RIGHT = 0
    

    def __init__(self, SCREENRECT, WHITE):
        pg.sprite.Sprite.__init__(self)
        self.SCREENRECT = SCREENRECT
        self.font = pg.font.Font(None, 20)
        self.font.set_bold(1)
        self.color = pg.Color(WHITE)

        
        self.update()
        self.rect = self.image.get_rect().move(self.SCREENRECT.centerx - (self.image.get_rect().width / 2), 0)
        
        

    def update(self):
        msg = str(self.SCORE_LEFT) + " | " + str(self.SCORE_RIGHT)
        self.image = self.font.render(msg, 0, self.color)
        

  