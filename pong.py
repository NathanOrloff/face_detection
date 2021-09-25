import random
import pygame as pg
import bumper
import puck
import score
import cpu
import time

SCREENRECT = pg.Rect(0, 0, 640, 480)
WIN_SCORE = 3
SPEED_LOW = 3
SPEED_HIGH = 7
BALL_START_PLACE = (SCREENRECT.centerx, 25)
BALL_START_DX = 2
BALL_START_DY = 2
CHANGE_DIRECTION = -1
WHITE = "#F8F0E3"
BLACK = "#1F1F1F"
RESET_TIME = 200



def main(winstyle=0):
    pg.init()
    pg.mixer = None
    fullscreen = False
    # time_prev = pg.time.get_ticks()
    # time_current = time_prev + RESET_TIME + 1

     # Set the display mode
    winstyle = 0  # |FULLSCREEN
    bestdepth = pg.display.mode_ok(SCREENRECT.size, winstyle, 32)
    screen = pg.display.set_mode(SCREENRECT.size, winstyle, bestdepth)

    

    # setup game window
    pg.display.set_caption("Pong")
    pg.mouse.set_visible(0)


    # create the background
    background = pg.Surface(SCREENRECT.size)
    screen.fill(BLACK)
    background.fill(BLACK)
    pg.display.flip()
    

    # Initialize Game Groups
    
    all = pg.sprite.RenderUpdates()

    # assign default groups to each sprite class
    bumper.Bumper.containers = all
    cpu.CPU.containers = all
    puck.Puck.containers = all
    score.Score.containers = all
    


   
    
    clock = pg.time.Clock()

    # initialize our starting sprites
    player = bumper.Bumper(SCREENRECT, WHITE, BLACK)
    comp = cpu.CPU(SCREENRECT, WHITE, BLACK)
    ball = puck.Puck(SCREENRECT, WHITE, BLACK)

   
    
    if pg.font:
        all.add(score.Score(SCREENRECT, WHITE))

    score_flag = 0
    
    
    while score.Score.SCORE_LEFT < WIN_SCORE and score.Score.SCORE_RIGHT < WIN_SCORE:
        if(score_flag):
            time.sleep(2)
            score_flag = 0

        # get input
        for event in pg.event.get():
            if event.type == pg.QUIT:
                return
            if event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE:
                return
            elif event.type == pg.KEYDOWN:
                if event.key == pg.K_f:
                    if not fullscreen:
                        print("Changing to FULLSCREEN")
                        screen_backup = screen.copy()
                        screen = pg.display.set_mode(
                            SCREENRECT.size, winstyle | pg.FULLSCREEN, bestdepth
                        )
                        screen.blit(screen_backup, (0, 0))
                    else:
                        print("Changing to windowed mode")
                        screen_backup = screen.copy()
                        screen = pg.display.set_mode(
                            SCREENRECT.size, winstyle, bestdepth
                        )
                        screen.blit(screen_backup, (0, 0))
                    pg.display.flip()
                    fullscreen = not fullscreen

        keystate = pg.key.get_pressed()

        # clear/erase the last drawn sprites
        all.clear(screen, background)

        
        # if time_current - time_prev >= RESET_TIME:
        #     time_prev = time_current

        # update all the sprites
        all.update()

        # handle player input
        direction = keystate[pg.K_DOWN] - keystate[pg.K_UP]
        player.move(direction)


    

        # Detect collisions between ball and players.
        if pg.sprite.collide_rect(player, ball):
            if ball.rect.centery <= comp.rect.centery:   
                ball.dy = random.randint(SPEED_LOW, SPEED_HIGH) * CHANGE_DIRECTION
            else:
                ball.dy = random.randint(SPEED_LOW, SPEED_HIGH)
            ball.dx = random.randint(SPEED_LOW, SPEED_HIGH) 
            



        # Detect collisions between ball and cpu.
        if pg.sprite.collide_rect(comp, ball):
            if ball.rect.centery <= comp.rect.centery:   
                ball.dy = random.randint(SPEED_LOW, SPEED_HIGH) * CHANGE_DIRECTION
            else:
                ball.dy = random.randint(SPEED_LOW, SPEED_HIGH)
            ball.dx = random.randint(SPEED_LOW, SPEED_HIGH) * CHANGE_DIRECTION 

    

        #set movement direction for cpu
        if ball.rect.centery < comp.rect.centery:
            comp.direction = -1
        elif ball.rect.centery > comp.rect.centery:
            comp.direction = 1
        else:
            comp.direction = 0



            
        #handle scoring and reset for next round
        if ball.rect.left <= SCREENRECT.left or ball.rect.right >= SCREENRECT.right:
            if ball.rect.left <= SCREENRECT.left:
                score.Score.SCORE_RIGHT += 1
                ball.dx = BALL_START_DX * CHANGE_DIRECTION
                ball.dy = BALL_START_DY
            else:
                score.Score.SCORE_LEFT += 1
                ball.dx = BALL_START_DX
                ball.dy = BALL_START_DY
            ball.rect = ball.image.get_rect(midbottom=BALL_START_PLACE)
            score_flag = 1
            # time_current = pg.time.get_ticks()
            
            


        # draw the scene
        dirty = all.draw(screen)
        pg.display.update(dirty)

        # cap the framerate at 40fps. Also called 40HZ or 40 times per second.
        clock.tick(40)



# call the "main" function if running this script
if __name__ == "__main__":
    main()
    pg.quit()