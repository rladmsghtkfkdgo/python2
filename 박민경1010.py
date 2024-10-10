from tkinter import *
from tkinter import messagebox
root = Tk()
root.title("연습 창")
root.geometry("300x400")
root.resizable(width=True, height=True)

label1 = Label(root, text="이봐 거기 너",font=(10))
label1.pack()
label2 =Label(root, text="공주 졸려", font=("궁서체",40), fg="pink")
label2.pack()
label3=Label(root,text="어서 나를 집으로 모셔가도록.",font=(20),bg="yellow",width=50,height=10,anchor=CENTER)
label3.pack()

def gohome() :
    messagebox.showinfo("", "옳지. 물부터 받아놓도록^^")
button1 = Button(root, text="귀가버튼", fg="red", command=gohome)
button1.pack()

root.mainloop()
