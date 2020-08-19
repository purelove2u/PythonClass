from tkinter import *

window = Tk()

insta = PhotoImage(file='./resource/instagram.png')
facebook = PhotoImage(file='./resource/facebook.png')
twitter = PhotoImage(file='./resource/twitter.png')

insta_btn = Button(window, image=insta)
facebook_btn = Button(window, image=facebook)
twitter_btn = Button(window, image=twitter)

insta_btn.pack(side=LEFT)
facebook_btn.pack(side=LEFT)
twitter_btn.pack(side=LEFT)

window.mainloop()