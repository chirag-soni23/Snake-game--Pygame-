    pygame.init()

    # colors
    white = (255,255,255)
    red = (255,0,0)
    black = (0,0,0)


    screen_width = 900
    screen_height = 600

    # creating window
    gameWindow = pygame.display.set_mode((screen_width,screen_height))
    pygame.display.set_caption("Snake Game")
    pygame.display.update()