from tkinter import *

window = Tk()

photo1 = PhotoImage(file="./resource/cat2.gif")
label1 = Label(window, image=photo1)

photo2 = PhotoImage(file="./resource/dog2.gif")
label2 = Label(window, image=photo2)

label1.pack(side=LEFT)
label2.pack(side=LEFT)
window.mainloop()
