from tkinter import *
from tkinter import messagebox


def keyEvent(event):
    messagebox.showinfo("키보드이벤트", "입력 키 :" + chr(event.keycode))


window = Tk()
window.geometry("200x200")
window.bind("<Key>", keyEvent)
window.mainloop()
