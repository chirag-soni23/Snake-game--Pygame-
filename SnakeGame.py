import pygame
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

# game specific variables
exit_game = False
game_over = False


# creating a game loop
while not exit_game:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit_game = True
    
    
    gameWindow.fill(white) 
    pygame.display.update()


# quit game
pygame.quit()
quit()       
    
        