# 위젯 배치
from tkinter import *

window = Tk()

for i in range(3):
    btn1 = Button(window, text="버튼" + str(i + 1))
    btn1.pack(side=LEFT)

# btn1 = Button(window, text="버튼1")
# btn2 = Button(window, text="버튼2")
# btn3 = Button(window, text="버튼3")


# 수평배치
# btn1.pack(side=LEFT)
# btn2.pack(side=LEFT)
# btn3.pack(side=LEFT)

# btn1.pack(side=RIGHT)
# btn2.pack(side=RIGHT)
# btn3.pack(side=RIGHT)

# 수직배치
# btn1.pack(side=TOP)
# btn2.pack(side=TOP)
# btn3.pack(side=TOP)

# fill : 채우기
# padx, pady : 바깥쪽 여백
# ipadx, ipady : 안쪽 여백
# btn1.pack(side=BOTTOM, fill=X, padx=10, pady=10)
# btn2.pack(side=BOTTOM, ipadx=10, ipady=10)
# btn3.pack(side=BOTTOM)

window.mainloop()
