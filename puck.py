import pygame as pg

class Puck(pg.sprite.Sprite):

    
    RADIUS = 10
    INITIAL_SPEED = 2
    CHANGE_DIRECTION = -1
    

    def __init__(self, SCREENRECT, WHITE, BLACK):
        pg.sprite.Sprite.__init__(self, self.containers)
        self.SCREENRECT = SCREENRECT
        self.START_PLACE = (self.SCREENRECT.centerx, 25)

        self.dx = self.INITIAL_SPEED
        self.dy = self.INITIAL_SPEED
        self.image = pg.Surface([self.RADIUS, self.RADIUS])
        self.image.fill(BLACK)
        self.image.set_colorkey(BLACK)
        pg.draw.circle(self.image, WHITE, ((self.RADIUS / 2),(self.RADIUS / 2)), self.RADIUS)
        self.rect = self.image.get_rect(midbottom=self.START_PLACE)


    def update(self):
        self.rect.x += self.dx
        self.rect.y += self.dy
        if self.rect.top <= 0:
            self.dy *= self.CHANGE_DIRECTION
        elif self.rect.bottom >= self.SCREENRECT.bottom:
            self.dy *= self.CHANGE_DIRECTION
        
        
  