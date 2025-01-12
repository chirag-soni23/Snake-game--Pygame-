import pygame
import random

pygame.init()

# Colors
white = (255, 255, 255)
red = (255, 0, 0)
black = (0, 0, 0)
green = (0, 255, 0)

# Screen dimensions
screen_width = 900
screen_height = 600

# Creating window
gameWindow = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Snake Game")
pygame.display.update()

# Clock and font
clock = pygame.time.Clock()
font = pygame.font.SysFont(None, 55)


def text_screen(text, color, x, y):
    """Display text on the screen."""
    screen_text = font.render(text, True, color)
    gameWindow.blit(screen_text, [x, y])


def plot_snake(gameWindow, color, snk_list, snake_size):
    """Draw the snake on the screen."""
    for i, (x, y) in enumerate(snk_list):
        if i == len(snk_list) - 1:  # Snake head (last element)
            pygame.draw.rect(gameWindow, green, [x, y, snake_size, snake_size])
        else:  # Snake body
            pygame.draw.rect(gameWindow, color, [x, y, snake_size, snake_size])


def welcome():
    """Welcome screen."""
    exit_game = False
    while not exit_game:
        gameWindow.fill(white)
        text_screen("Welcome to Snake Game", black, 250, 250)
        text_screen("Press Enter to Start", black, 250, 300)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit_game = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    gameloop()

        pygame.display.update()
        clock.tick(60)


def gameloop():
    """Main game loop."""
    # Game variables
    exit_game = False
    game_over = False
    score = 0
    snake_x = 45
    snake_y = 55
    velocity_x = 0
    velocity_y = 0
    init_velocity = 5
    snk_list = []
    snk_length = 1

    # High score handling
    try:
        with open("hiscore.txt", "r") as f:
            hiscore = int(f.read())
    except FileNotFoundError:
        hiscore = 0

    food_x = random.randint(20, screen_width - 20)
    food_y = random.randint(20, screen_height - 20)

    snake_size = 20
    fps = 60

    while not exit_game:
        if game_over:
            gameWindow.fill(white)
            text_screen("Game Over! Press Enter To Continue", red, 100, 200)
            text_screen(f"Your Score: {score}", black, 100, 250)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit_game = True
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        welcome() 

            with open("hiscore.txt", "w") as f:
                f.write(str(hiscore))

        else:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit_game = True
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RIGHT and velocity_x == 0:
                        velocity_x = init_velocity
                        velocity_y = 0
                    if event.key == pygame.K_LEFT and velocity_x == 0:
                        velocity_x = -init_velocity
                        velocity_y = 0
                    if event.key == pygame.K_UP and velocity_y == 0:
                        velocity_y = -init_velocity
                        velocity_x = 0
                    if event.key == pygame.K_DOWN and velocity_y == 0:
                        velocity_y = init_velocity
                        velocity_x = 0
                    if event.key == pygame.K_q:
                        score += 10
                         
            snake_x += velocity_x
            snake_y += velocity_y

            # Food collision
            if abs(snake_x - food_x) < snake_size and abs(snake_y - food_y) < snake_size:
                score += 10
                food_x = random.randint(20, screen_width - 20)
                food_y = random.randint(20, screen_height - 20)
                snk_length += 5
                if score > hiscore:
                    hiscore = score

            gameWindow.fill(white)
            text_screen(f"Score: {score}  High Score: {hiscore}", red, 5, 5)

            # Draw food
            pygame.draw.rect(gameWindow, red, [food_x, food_y, snake_size, snake_size])

            # Snake movement
            head = [snake_x, snake_y]
            snk_list.append(head)

            if len(snk_list) > snk_length:
                del snk_list[0]

            # Collision with itself or walls
            if head in snk_list[:-1] or snake_x < 0 or snake_x > screen_width or snake_y < 0 or snake_y > screen_height:
                game_over = True

            plot_snake(gameWindow, black, snk_list, snake_size)

        pygame.display.update()
        clock.tick(fps)

    pygame.quit()
    quit()


welcome()
