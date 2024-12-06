import pygame
import time
import random

pygame.init()

# 색상 정의
white = (255, 255, 255)
yellow = (255, 255, 102)
black = (0, 0, 0)
red = (213, 50, 80)
green = (0, 255, 0)
blue = (50, 153, 213)

# 게임 화면 크기
width = 600
height = 400
screen = pygame.display.set_mode((width, height))

# 뱀의 초기 설정
snake_block = 10
snake_speed = 15

# 뱀과 먹이의 초기 위치
snake_list = []
length_of_snake = 1
x1 = width / 2
y1 = height / 2
x1_change = 0
y1_change = 0

# 먹이의 위치
foodx = round(random.randrange(0, width - snake_block) / 10.0) * 10.0
foody = round(random.randrange(0, height - snake_block) / 10.0) * 10.0

# 게임 루프
game_over = False
while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                x1_change = -snake_block
                y1_change = 0
            elif event.key == pygame.K_RIGHT:
                x1_change = snake_block
                y1_change = 0
            elif event.key == pygame.K_UP:
                y1_change = -snake_block
                x1_change = 0
            elif event.key == pygame.K_DOWN:
                y1_change = snake_block
                x1_change = 0
    
    if event .type in [pygame.KEYDOWN]:
        if event.key ==pygame.K_LEFT :dx= -5
        elif event.key ==pygame.K_RIGHT :dx= +5
        elif event.key ==pygame.K_UP :dy= -5
        elif event.key ==pygame.K_DOWN :dy= +5

    # 뱀의 위치 업데이트
    x1 += x1_change
    y1 += y1_change

    # 게임 종료 조건
    if x1 >= width or x1 < 0 or y1 >= height or y1 < 0:
        game_over = True

    # 화면 업데이트
    screen.fill(blue)
    pygame.draw.rect(screen, green, [foodx, foody, snake_block, snake_block])
    pygame.display.update()

    time.sleep(0.1)

pygame.quit()
