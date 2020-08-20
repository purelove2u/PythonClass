from tkinter import *

window = Tk()

btn_msg = ["삽입", "수정", "삭제"]
btn_back = ["blue", "green", "yellow"]

for i in range(3):
    btn1 = Button(window, text=btn_msg[i], bg=btn_back[i])
    btn1.pack(side=TOP)

window.mainloop()
