# Hello zerolight, regards Stephen Surtees
import game.game as app

def main():
    """ A small solar system. Create objects by holding mouse down and
    dragging for direction and power """
    game = app.Game(width=720, height=720, minDt=10)
    game.gameLoop()

if __name__ == "__main__":
    main()