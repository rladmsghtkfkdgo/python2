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

# 게임 타이틀 설정
pygame.display.set_caption("Snake Game")

# 뱀의 설정
snake_block = 10
snake_speed = 15
clock = pygame.time.Clock()

# 뱀의 초기 상태
snake_list = []
length_of_snake = 1
x1 = width / 2
y1 = height / 2
x1_change = 0
y1_change = 0

# 먹이 색상 생성 함수
def generate_food_color():
    while True:
        color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        if color != black: 
            return color

# 먹이의 초기 위치와 색상
foodx = round(random.randrange(0, width - snake_block) / 10.0) * 10.0
foody = round(random.randrange(0, height - snake_block) / 10.0) * 10.0
food_color = generate_food_color()

# 점수 초기화
score = 0
high_score = 0

# 기존 최고 점수 읽기 (파일 입출력)
try:
    with open("high_score.txt", "r") as file:
        high_score = int(file.read())
except FileNotFoundError:
    high_score = 0

# 폰트 초기화
font_style = pygame.font.SysFont("bahnschrift", 25)  
score_font = pygame.font.SysFont("comicsansms", 20)  

# 메시지 출력 함수
def message(msg, color, x, y):
    message_surface = font_style.render(msg, True, color)
    screen.blit(message_surface, [x, y])


def display_score(current_score, best_score):
    value = score_font.render(f"Score: {current_score}", True, yellow)
    high_score_value = score_font.render(f"High Score: {best_score}", True, yellow)
    screen.blit(value, [10, 10]) 
    screen.blit(high_score_value, [10, 30])


# 메인 루프
game_over = False
close_game = False

while not game_over:

    # 게임 종료 확인 루프
    while close_game:
        screen.fill(blue)
        message("Game Over! Press Q-Quit or C-Continue", red, width / 6, height / 3)
        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    game_over = True
                    close_game = False
                if event.key == pygame.K_c:
                    # 게임 리셋
                    x1 = width / 2
                    y1 = height / 2
                    x1_change = 0
                    y1_change = 0
                    snake_list = []
                    length_of_snake = 1
                    score = 0
                    foodx = round(random.randrange(0, width - snake_block) / 10.0) * 10.0
                    foody = round(random.randrange(0, height - snake_block) / 10.0) * 10.0
                    food_color = generate_food_color()
                    close_game = False

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT and x1_change == 0:
                x1_change = -snake_block
                y1_change = 0
            elif event.key == pygame.K_RIGHT and x1_change == 0:
                x1_change = snake_block
                y1_change = 0
            elif event.key == pygame.K_UP and y1_change == 0:
                y1_change = -snake_block
                x1_change = 0
            elif event.key == pygame.K_DOWN and y1_change == 0:
                y1_change = snake_block
                x1_change = 0

    # 뱀의 위치 업데이트
    x1 += x1_change
    y1 += y1_change

    # 게임 종료 조건
    if x1 >= width or x1 < 0 or y1 >= height or y1 < 0:
        close_game = True

    # 화면 업데이트
    screen.fill(blue)
    pygame.draw.rect(screen, food_color, [foodx, foody, snake_block, snake_block])

    # 뱀 몸체 업데이트
    snake_head = [x1, y1]
    snake_list.append(snake_head)
    if len(snake_list) > length_of_snake:
        del snake_list[0]

    # 뱀이 자기 자신과 충돌했는지 확인
    for block in snake_list[:-1]:
        if block == snake_head:
            close_game = True

    # 뱀 그리기
    for block in snake_list:
        pygame.draw.rect(screen, black, [block[0], block[1], snake_block, snake_block])

    # 먹이를 먹었는지 확인
    if x1 == foodx and y1 == foody:
        foodx = round(random.randrange(0, width - snake_block) / 10.0) * 10.0
        foody = round(random.randrange(0, height - snake_block) / 10.0) * 10.0
        food_color = generate_food_color() 
        length_of_snake += 1
        score += 10 

        # 최고 점수 업데이트
        if score > high_score:
            high_score = score

    # 점수 표시
    display_score(score, high_score)

    pygame.display.update()
    clock.tick(snake_speed)

# 최고 점수 저장
with open("high_score.txt", "w") as file:
    file.write(str(high_score))

pygame.quit()
