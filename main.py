import game.game as app

def main():
    game = app.Game(width=640, height=480, minDt=10)
    game.gameLoop()

if __name__ == "__main__":
    main()