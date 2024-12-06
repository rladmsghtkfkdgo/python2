# 일단 뱀 사진 있어야하고 우주선 게임마냥 방향키로 움직이는데 
# 먹이를 먹으면 몸구슬 +1 점수 +10 
# 뱀좌표는 처음구슬만 조종가능하고 나머지는 처음구슬 위치 따라가기.
# 머리변수가 몸변수에 닿으면 게임종료.
# 먹이는 랜덤좌표에 랜덤갯수로자동생성 같은좌표는 생성불가
# 이벤트먹이 먹으면 이속증가와 먹이증가 무지개로 빛나게 할 수 있으면 빛추가
import pygame
import random
import sys
import time

def paintEntry(entity,x,y):
    monitor.blit(entity,(int(x),int(y)))

def playgame():
    global monitor,snake

    r=random.randrange(0,256)
    g=random.randrange(0,256)
    b=random.randrange(0,256)

    snakeX=swidth/2
    snakeY=sheight/2
    dx,dy=0,0
    

    while True:
        (pygame.time.Clock()).tick(50)  #게임 진행을 늦춘ㄴ다
        monitor.fill((r,g,b)) 
    
        for e in pygame.event.get():
            if e.type in [pygame.QUIT]:
                pygame.quit()
                sys.exit()

        pygame.display.update()
        print('~',end='')

r,g,b=[0]*3                 #게임 배경색
swidth, sheight =1000,700    #화면 크기
monitor=None                #게임화면

pygame.init()
monitor=pygame.display.set_mode((swidth,sheight))
pygame.display.set_caption('뱀 키우기')

playgame()

