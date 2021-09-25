import pygame as pg



class Bumper(pg.sprite.Sprite):

    SPEED = 3
    WIDTH = 10
    HEIGHT = 50
    START_PLACE = (30, 240)
    

    def __init__(self, SCREENRECT, WHITE, BLACK):
        pg.sprite.Sprite.__init__(self, self.containers)
        self.SCREENRECT = SCREENRECT
        self.image = pg.Surface([self.WIDTH, self.HEIGHT])
        self.image.fill(BLACK)
        self.image.set_colorkey(BLACK)
        pg.draw.rect(self.image, WHITE, [0,0,self.WIDTH,self.HEIGHT])
        self.rect = self.image.get_rect(midbottom=self.START_PLACE)


    def move(self, direction):
        self.rect.move_ip(0, direction * self.SPEED)
        self.rect = self.rect.clamp(self.SCREENRECT)