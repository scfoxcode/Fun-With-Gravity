# Hello zerolight, regards Stephen
import game.game as app

def main():
    game = app.Game(width=720, height=720, minDt=10)
    game.gameLoop()

if __name__ == "__main__":
    main()