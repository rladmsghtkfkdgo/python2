import turtle as t #1
import random
import time

def find_card(x,y):
    min_idx = 0
    min_dis = 100

    for i in range(16): #9
        distance = turtles[i].distance(x,y)
        if distance < min_dis:
            min_dis = distance
            min_idx = i
    return min_idx

def score_update():
   score_pen.clear()
   score_pen.write(f"{m} {score}점/{attemp}번 시도", False,"center",("",15))

def result():
   t.goto(0,60)
   t.write(m,False,"center",("",30,"bold"))

def play(x,y):
    global click_num #클릭 횟수 (1,2)
    global score    #
    global attemp  #시도 횟수 
    global first_pick  #첫번째 클릭 이미지
    global second_pick #두번째 클릭 이미지

    if attemp == 12:
        t.goto(0,-60)
        t.write("Game Over", False, "center", ("", 30, "bold"))
    else:
        click_num += 1
        #클릭된 이미지 찾기
        card_idx = find_card(x,y)
        turtles[card_idx].shape(img_list[card_idx])
        if click_num ==1:
           first_pick=card_idx
        elif click_num==2:
           second_pick = card_idx
           click_num=0
           attemp += 1
           if img_list[first_pick] == img_list[second_pick]:
             score += 1
             score_update("정답")
             if score == 8:
                result("성공")
           else:
             score_update("오답")
             turtles[first_pick],shape(default_img)
             turtles[second_pick],shape(default_img)




t.bgcolor("pink") #60
t.setup(700,700)
t.penup() #움직이는 선 제거
t.hideturtle()
t.goto(0,280)
t.write("카드매칭 게임", False, "center", ("",30,"bold"))

#점수 팬 객체 생성
score_pen=t.Turtle()
score_pen.penup()
score_pen.hideturtle()
score_pen.goto(0.230)

#터틀 객체 생성

turtles = []
pos_x = [-210, -70, 70, 210]
pos_y = [-250, -110, 30, 170]

for x in range(4):
  for y in range(4):
    new_turtle = t.Turtle()
    new_turtle.up
    new_turtle.color("pink")
    new_turtle.speed(0)
    new_turtle.goto(pos_x[x],pos_y[y])
    turtles.append(new_turtle)

#이미지 지정
default_img = "images/default_img.gif"
t.addshape(default_img)


img_list = []

for i in range(8):
    img = f"images/img{i}.gif"
    t.addshape(img)
    img_list.append(img)
    img_list.append(img)

random.shuffle(img_list)
    
for i in range(16):
  turtles[i].shape(img_list[i])

time.sleep(1)

for i in range(16):
  turtles[i].shape(default_img)
    
#변수 선언
  
click_num = 0 #클릭 횟수 (1,2)
score = 0     #
attemp = 0    #시도 횟수 
first_pick = 0 #첫번째 클릭 이미지
second_pick = 0 #두번째 클릭 이미지



t.onscreenclick(play)

t.done()