import sys
import pygame as pg
pg.init()

def main():
    size = width, height = 320, 240
    print(size)
    speed = [2, 2]
    black = 0, 0, 0
    screen = pg.display.set_mode(size, pg.HWSURFACE|pg.DOUBLEBUF|pg.RESIZABLE)

    while 1:
        for event in pg.event.get():
            if event.type == pg.QUIT: sys.exit()

        screen.fill(black)
        pg.draw.circle(screen, pg.Color(255,255,0,255), (width/2, height/2), 20)
        pg.display.flip()

if __name__ == "__main__":
    main()