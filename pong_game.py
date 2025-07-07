import pygame
import random

# Initialize Pygame
pygame.init()

# Screen dimensions
WIDTH, HEIGHT = 800, 600

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Ball settings
BALL_SPEED = [4, 4]
BALL_RADIUS = 10

# Paddle settings
PADDLE_WIDTH, PADDLE_HEIGHT = 10, 100
PADDLE_SPEED = 6

# Initialize screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pong Game")

# Clock for controlling frame rate
clock = pygame.time.Clock()

# Ball position and velocity
ball_pos = [WIDTH // 2, HEIGHT // 2]
ball_vel = BALL_SPEED[:]

# Paddle positions
left_paddle = [10, HEIGHT // 2 - PADDLE_HEIGHT // 2]
right_paddle = [WIDTH - 20, HEIGHT // 2 - PADDLE_HEIGHT // 2]

# Game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Get keys
    keys = pygame.key.get_pressed()

    # Move paddles
    if keys[pygame.K_w] and left_paddle[1] > 0:
        left_paddle[1] -= PADDLE_SPEED
    if keys[pygame.K_s] and left_paddle[1] < HEIGHT - PADDLE_HEIGHT:
        left_paddle[1] += PADDLE_SPEED
    if keys[pygame.K_UP] and right_paddle[1] > 0:
        right_paddle[1] -= PADDLE_SPEED
    if keys[pygame.K_DOWN] and right_paddle[1] < HEIGHT - PADDLE_HEIGHT:
        right_paddle[1] += PADDLE_SPEED

    # Update ball position
    ball_pos[0] += ball_vel[0]
    ball_pos[1] += ball_vel[1]

    # Ball collision with top and bottom walls
    if ball_pos[1] - BALL_RADIUS <= 0 or ball_pos[1] + BALL_RADIUS >= HEIGHT:
        ball_vel[1] = -ball_vel[1]

    # Ball collision with paddles
    if (ball_pos[0] - BALL_RADIUS <= left_paddle[0] + PADDLE_WIDTH and left_paddle[1] <= ball_pos[1] <= left_paddle[1] + PADDLE_HEIGHT) or \
       (ball_pos[0] + BALL_RADIUS >= right_paddle[0] and right_paddle[1] <= ball_pos[1] <= right_paddle[1] + PADDLE_HEIGHT):
        ball_vel[0] = -ball_vel[0]

    # Ball out of bounds
    if ball_pos[0] < 0 or ball_pos[0] > WIDTH:
        ball_pos = [WIDTH // 2, HEIGHT // 2]
        ball_vel = BALL_SPEED[:]

    # Draw everything
    screen.fill(BLACK)
    pygame.draw.rect(screen, WHITE, (*left_paddle, PADDLE_WIDTH, PADDLE_HEIGHT))
    pygame.draw.rect(screen, WHITE, (*right_paddle, PADDLE_WIDTH, PADDLE_HEIGHT))
    pygame.draw.circle(screen, WHITE, ball_pos, BALL_RADIUS)

    # Update display
    pygame.display.flip()

    # Cap the frame rate
    clock.tick(60)

pygame.quit()