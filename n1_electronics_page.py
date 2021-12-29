from tkinter import *
def electronics_page_funct(topframe,main_page):
	for widget in topframe.winfo_children():
		widget.destroy()
	button1=Button(topframe, text = "↩ Return", fg = "white", bg = "black", command=main_page)
	button1.config(width=15, font="Palatino")
	button1.grid(row=1,column=1) 
	'''
	settings_menu=Menu(root)
	root.config(menu=settings_menu)
	subMenu=Menu(settings_menu)
	settings_menu.add_cascade(label="Settings",menu=subMenu)
	subMenu.add_command(label="Profile", command=grocery_page_method)
	subMenu.add_command(label="Checkout", command=grocery_page_method)
	subMenu.add_separator()
	subMenu.add_command(label="Exit", command=grocery_page_method)
	'''