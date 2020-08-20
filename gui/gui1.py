from tkinter import *

window = Tk()
window.title("윈도우 보여주기")
# 윈도우 창 크기 지정(Width,Height,x좌표,y좌표)
window.geometry("400x100+200+200")
# 창의 크기를 조절할 수 있도록 지정
window.resizable(True,False)
window.mainloop()
