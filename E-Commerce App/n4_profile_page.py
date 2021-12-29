from tkinter import *
def profile_page_funct(topframe,main_page):
	for widget in topframe.winfo_children():
		widget.destroy()
	button1=Button(topframe, text = "↩ Return", fg = "white", bg = "black", command=main_page)
	#button1.pack()
	button1.config(width=15, font="Palatino")
	button1.grid(row=1,column=1)