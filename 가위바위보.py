import random
from tkinter import *
from tkinter import messagebox

#함수 선언 부분
def myFuncS():
    ai =random.choices(["가위","바위","보"])

    if ai =="가위":
        messagebox.showinfo("가위바위보","비겼습니다.")
    elif ai =="바위":
        messagebox.showinfo("가위바위보","졌습니다.")
    else:
        messagebox.showinfo("가위바위보","이겼습니다.")

def myFuncR():
    ai =random.choices(["가위","바위","보"])

    if ai =="바위":
        messagebox.showinfo("가위바위보","비겼습니다.")
    elif ai =="보":
        messagebox.showinfo("가위바위보","졌습니다.")
    else:
        messagebox.showinfo("가위바위보","이겼습니다.")
#메인코드부분
window =Tk()
window.geometry("600x400")

photo =PhotoImage(file = "gif/dog.gif")
button1 =Label(window, image=photo)
photo1 =PhotoImage(file = "gif/dog2.gif")
button2 =Label(window, image=photo1)

button3 =Button(window, text="가위",command =myFuncS)
button4 =Button(window, text="바위",command =myFuncR)
button5 =Button(window, text="보")
