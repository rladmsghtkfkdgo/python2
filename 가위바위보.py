import random
from tkinter import *
from tkinter import messagebox

#함수 선언 부분
def myFuncS():
    ai =random.choices(["가위","바위","보"])
    button1.place(x=80,y=10000000)
    button2.place(x=200,y=1000000)
    button6.place(x=80,y=10)

    if ai =="가위":
        button9.place(x=300,y=10)
        messagebox.showinfo("가위바위보","비겼습니다.")
    elif ai =="바위":
        button7.place(x=300,y=10)
        messagebox.showinfo("가위바위보","졌습니다.")
    else:
        button8.place(x=300,y=10)
        messagebox.showinfo("가위바위보","이겼습니다.")

def myFuncR():
    ai =random.choices(["가위","바위","보"])
    button1.place(x=80,y=10)
    button2.place(x=200,y=1000000000)
    button6.place(x=10,y=10000000000)
    if ai =="바위":
        button7.place(x=300,y=10)
        messagebox.showinfo("가위바위보","비겼습니다.")
    elif ai =="보":
        button8.place(x=300,y=10)
        messagebox.showinfo("가위바위보","졌습니다.")
    else:
        button9.place(x=300,y=10)
        messagebox.showinfo("가위바위보","이겼습니다.")

def myFuncP():
    ai =random.choices(["가위","바위","보"])
    button1.place(x=80,y=1000000000)
    button2.place(x=80,y=10)
    button6.place(x=10,y=10000000000)
    if ai =="바위":
        button7.place(x=300,y=10)
        messagebox.showinfo("가위바위보","이겼습니다.")
    elif ai =="보":
        button8.place(x=300,y=10)
        messagebox.showinfo("가위바위보","비겼습니다.")
    else:
        button9.place(x=300,y=10)
        messagebox.showinfo("가위바위보","졌습니다.")
#메인코드부분
window =Tk()
window.geometry("600x400")
window.title("가위바위보(박민경)")

photo1 =PhotoImage(file = "gif/rock.PNG")
button1 =Label(window, image=photo1)
photo2 =PhotoImage(file = "gif/paper.PNG")
button2 =Label(window, image=photo2)
photo3 =PhotoImage(file = "gif/si.PNG")
button6 =Label(window, image=photo3)

photo4 =PhotoImage(file = "gif/rock.PNG")
button7 =Label(window, image=photo4)
photo5 =PhotoImage(file = "gif/paper.PNG")
button8 =Label(window, image=photo5)
photo6 =PhotoImage(file = "gif/si.PNG")
button9 =Label(window, image=photo6)

button3 =Button(window, text="가위",command =myFuncS)
button4 =Button(window, text="바위",command =myFuncR)
button5 =Button(window, text="보",command =myFuncP)

button1.place(x=400,y=10)
button2.place(x=200,y=10)
button6.place(x=10,y=10)
button7.place(x=10000,y=10)
button8.place(x=10000,y=10)
button9.place(x=10000,y=10)

button3.pack(side=BOTTOM,padx=30,pady=5)
button4.pack(side=BOTTOM,padx=30,pady=5)
button5.pack(side=BOTTOM,padx=30,pady=5)
window.mainloop() 
