import game.game as app
import pygame as pg
pg.init()

def main():
    game = app.Game(width=320, height=240, minDt=10)
    game.gameLoop()

if __name__ == "__main__":
    main()