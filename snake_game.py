import pygame
import random
import sys

# Initialize pygame
pygame.init()

# Set up display
width, height = 600, 400
win = pygame.display.set_mode((width, height))
pygame.display.set_caption("Snake Game")

# Load images
background_img = pygame.image.load("background.png")

# Colors for fallback if images are not provided
green = (0, 255, 0)
red = (255, 0, 0)
white = (255, 255, 255)

# Game variables
snake_pos = [100, 50]
snake_body = [[100, 50], [90, 50], [80, 50]]
snake_direction = 'RIGHT'
change_to = snake_direction

speed = 15
clock = pygame.time.Clock()

# Food
food_pos = [random.randrange(1, (width // 10)) * 10, random.randrange(1, (height // 10)) * 10]
food_spawn = True

# Score
score = 0

# Font
font = pygame.font.SysFont('times new roman', 35)

def game_over():
    game_over_text = font.render(f'Game Over! Score: {score}', True, red)
    win.fill((0, 0, 0))
    win.blit(game_over_text, [width // 6, height // 3])
    pygame.display.flip()
    pygame.time.sleep(2)
    pygame.quit()
    sys.exit()

while True:
    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and change_to != 'DOWN':
                change_to = 'UP'
            elif event.key == pygame.K_DOWN and change_to != 'UP':
                change_to = 'DOWN'
            elif event.key == pygame.K_LEFT and change_to != 'RIGHT':
                change_to = 'LEFT'
            elif event.key == pygame.K_RIGHT and change_to != 'LEFT':
                change_to = 'RIGHT'

    # Change direction
    snake_direction = change_to

    # Move snake
    if snake_direction == 'UP':
        snake_pos[1] -= 10
    elif snake_direction == 'DOWN':
        snake_pos[1] += 10
    elif snake_direction == 'LEFT':
        snake_pos[0] -= 10
    elif snake_direction == 'RIGHT':
        snake_pos[0] += 10

    # Snake body growing
    snake_body.insert(0, list(snake_pos))
    if snake_pos == food_pos:
        score += 10
        food_spawn = False
    else:
        snake_body.pop()

    # Spawn new food
    if not food_spawn:
        food_pos = [random.randrange(1, (width // 10)) * 10, random.randrange(1, (height // 10)) * 10]
    food_spawn = True

    # Game Over conditions
    if snake_pos[0] < 0 or snake_pos[0] >= width or snake_pos[1] < 0 or snake_pos[1] >= height:
        game_over()
    for block in snake_body[1:]:
        if snake_pos == block:
            game_over()

    # Display
    win.blit(background_img, (0, 0))

    # Draw snake
    for block in snake_body:
        pygame.draw.rect(win, green, pygame.Rect(block[0], block[1], 10, 10))

    # Draw food
    pygame.draw.rect(win, red, pygame.Rect(food_pos[0], food_pos[1], 10, 10))

    # Score display
    score_text = font.render(f'Score: {score}', True, white)
    win.blit(score_text, [0, 0])

    # Refresh game screen
    pygame.display.update()

    # Frame Per Second /Refresh Rate
    clock.tick(speed)
