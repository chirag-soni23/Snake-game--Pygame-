import pygame
import random
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
score = 0
snake_x = 45
snake_y = 55
velocity_x = 0
velocity_y = 0
init_velocity = 5

food_x = random.randint(20, int(screen_width / 2))
food_y = random.randint(20, int(screen_height / 2))

snake_size = 20
fps = 60

# clock
clock = pygame.time.Clock()
font = pygame.font.SysFont(None,55)
def text_screen(text,color,x,y):
    screen_text = font.render(text,True,color)
    gameWindow.blit(screen_text,[x,y])
   
snk_list = []
snk_length = 1
def plot_snake(gameWindow,color,snk_list,snake_size):
    for x,y in snk_list:
        pygame.draw.rect(gameWindow,color,[x,y,snake_size,snake_size])
        
    

# creating a game loop
while not exit_game:
    
    if game_over:
        gameWindow.fill(white)
        text_screen("Game Over! Press Enter To Continue",red,screen_width/2,screen_height/2)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit_game = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    pass    
    else:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit_game = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    velocity_x = init_velocity
                    velocity_y = 0   
                if event.key == pygame.K_LEFT:
                    velocity_x = -init_velocity 
                    velocity_y = 0  
                if event.key == pygame.K_UP:
                    velocity_y = -init_velocity
                    velocity_x = 0   
                if event.key == pygame.K_DOWN:
                    velocity_y = init_velocity  
                    velocity_x = 0 
                
        
        snake_x += velocity_x
        snake_y += velocity_y
        
        if abs(snake_x - food_x) < 6 and abs(snake_y - food_y) < 6:
            score += 1
            food_x = random.randint(20, int(screen_width / 2))
            food_y = random.randint(20, int(screen_height / 2)) 
            snk_length += 5
            
        gameWindow.fill(white)
        text_screen("Score: "+str(score*10),red,5,5)
        # snake food
        pygame.draw.rect(gameWindow,red,[food_x,food_y,snake_size,snake_size])
        # snake head
        head = []
        head.append(snake_x)
        head.append(snake_y)
        snk_list.append(head)
        
        if len(snk_list)>snk_length:
            del snk_list[0]
        
        # game over
        if snake_x < 0 or snake_x > screen_width or snake_y < 0 or snake_y > screen_height:
            game_over = True   
        # pygame.draw.rect(gameWindow,black,[snake_x,snake_y,snake_size,snake_size]) 
        plot_snake(gameWindow,black,snk_list,snake_size)
    pygame.display.update()
    clock.tick(fps)


# quit game
pygame.quit()
quit()       
    
        