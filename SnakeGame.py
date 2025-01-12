import pygame
import random
pygame.init()

# Colors
white = (255, 255, 255)
red = (255, 0, 0)
black = (0, 0, 0)
green = (0, 255, 0)

screen_width = 900
screen_height = 600

# Creating window
gameWindow = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Snake Game")
pygame.display.update()

# Clock
clock = pygame.time.Clock()
font = pygame.font.SysFont(None, 55)


def text_screen(text, color, x, y):
    screen_text = font.render(text, True, color)
    gameWindow.blit(screen_text, [x, y])


def plot_snake(gameWindow, color, snk_list, snake_size):
    for i, (x, y) in enumerate(snk_list):
        if i == len(snk_list) - 1:  # Snake head (last element) will be green
            pygame.draw.rect(gameWindow, green, [x, y, snake_size, snake_size])
        else:  # Remaining body in black
            pygame.draw.rect(gameWindow, color, [x, y, snake_size, snake_size])


# Creating a game loop
def gameloop():
    # Game specific variables
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

    # High score file handling
    try:
        with open("hiscore.txt", "r") as f:
            hiscore = f.read()
    except:
        hiscore = "0"

    hiscore = int(hiscore)

    food_x = random.randint(20, int(screen_width / 2))
    food_y = random.randint(20, int(screen_height / 2))

    snake_size = 20
    fps = 60

    while not exit_game:

        if game_over:
            gameWindow.fill(white)
            text_screen("Game Over! Press Enter To Continue", red, 100, 200)
            text_screen(f"Your Score: {score}", black, 100, 250)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit_game = True
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        gameloop()

            # Save high score
            with open("hiscore.txt", "w") as f:
                f.write(str(hiscore))

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
                    if event.key == pygame.K_q:
                        score += 5
            snake_x += velocity_x
            snake_y += velocity_y

            if abs(snake_x - food_x) < 20 and abs(snake_y - food_y) < 20:
                score += 10
                food_x = random.randint(20, int(screen_width / 2))
                food_y = random.randint(20, int(screen_height / 2))
                snk_length += 5
                if score > hiscore:
                    hiscore = score

            gameWindow.fill(white)
            text_screen(f"Score: {score}  High Score: {hiscore}", red, 5, 5)

            # Snake food
            pygame.draw.rect(gameWindow, red, [food_x, food_y, snake_size, snake_size])

            # Snake head
            head = [snake_x, snake_y]
            snk_list.append(head)

            if len(snk_list) > snk_length:
                del snk_list[0]

            # Game over conditions
            if head in snk_list[:-1] or snake_x < 0 or snake_x > screen_width or snake_y < 0 or snake_y > screen_height:
                game_over = True

            plot_snake(gameWindow, black, snk_list, snake_size)

        pygame.display.update()
        clock.tick(fps)

    # Quit game
    pygame.quit()
    quit()


gameloop()
