import tkinter
from tkinter import *
from PIL import ImageTk,Image,ImageDraw,ImageFont,ImageOps,ImageSequence 
import requests

from n1_electronics_page import electronics_page_funct
from n2_clothing_page import clothing_page_funct
from n3_grocery_page import grocery_page_funct
from n4_profile_page import profile_page_funct
#from n5_functions import get_main_img

root=Tk() #We're basically creating a blank window
root.title("Friple-A")
root.geometry("2000x2000")

def toggle_fullscreen():
	if (root.attributes('-fullscreen')):
		root.attributes('-fullscreen', False)
	else:
		root.attributes('-fullscreen', True)

theLabel = Label(root, text = "⚜ Friple-A Shopping ⚜", bg="#000000", fg = "#DCAF32") #Creating basic text; syntax Label(<where to put label>,<text>)
theLabel.config(width=200,height=1) #Changes width of the label box
theLabel.config(font=("Courier", 44)) #Change font of label Syntax - font=(<font name>, size)
theLabel.pack(fill=X) #Places it somewhere   ; Fill = X, enlarges the label along X direction if the window is enlarged; Fill = Y enlarges along Y axis

topframe = Frame(root,bg="black") #Creates a frame in the gui window
topframe.pack(fill=X)#To display the frame (invisible rectangle)

topframe.update()
print(topframe.winfo_width(),topframe.winfo_height())

def get_main_img(url,width,height):
	sample_img = Image.open(requests.get(url, stream=True).raw)
	sample_img= sample_img.resize((width,height), Image.ANTIALIAS)
	sample_img = ImageTk.PhotoImage(sample_img)
	return sample_img
#electronics_img = get_main_img("https://cdn.pixabay.com/photo/2017/10/22/21/06/flat-2879273_960_720.jpg",350,200)
#grocery_img = get_main_img("https://cdn.pixabay.com/photo/2016/04/21/11/32/groceries-1343141_960_720.jpg",350,200)
#clothing_img = get_main_img("https://cdn.pixabay.com/photo/2015/10/12/15/18/store-984393_960_720.jpg", 350, 200)
#profile_img = get_main_img("https://image.flaticon.com/icons/png/512/848/848043.png",200,200)
electronics_img = ImageTk.PhotoImage((Image.open("images\\1_main_electronics.jpg")).resize((350,200)))
grocery_img = ImageTk.PhotoImage((Image.open("images\\2_main_grocery.jpg")).resize((350,200)))
clothing_img = ImageTk.PhotoImage((Image.open("images\\3_main_clothing.jpg")).resize((350,200)))
logo_img = ImageTk.PhotoImage((Image.open("images\\4_main_logo.png")).resize((375,200)))
banner_img = ImageTk.PhotoImage((Image.open("images\\5_main_banner.png")).resize((1400,450)))

def main_page():
	global topframe
	def electronics_page_method():
		electronics_page_funct(topframe,main_page)
	def grocery_page_method():
		grocery_page_funct(topframe,main_page)
	def clothing_page_method():
		clothing_page_funct(topframe, main_page)
	def profile_page_method():
		clothing_page_funct(topframe, main_page)
	for widget in topframe.winfo_children():
		widget.destroy()

	def search_in_words(event=None):
		search_entry=search_box.get()
		print(search_entry)
		search_box.delete(0, 'end')


	button1=Button(topframe, text = "🎮 Electronics", fg = "#36454f", bg = "#DCAF32", command=electronics_page_method) #Adds a button. Syntax - Button(<where>, <text>, ForeGround = <colour>, BackGround = <colour>)
	button2=Button(topframe, text = "🛒 Grocery", fg = "#36454f", bg =  "#DCAF32", command = grocery_page_method)
	button3=Button(topframe, text = "👔 Clothing", fg = "#36454f", bg =  "#DCAF32", command=clothing_page_method)
	button4=Button(topframe, text = "🔍  ", anchor="e", fg = "#36454f", bg =  "#DCAF32", state="disabled")
	search_box=Entry(topframe,text= "Search",width=35, fg="black", bg="white") #36454f - Charcoal html
	search_box.bind('<Return>',search_in_words)

	#Creating Menubutton 
	settings_menubutton = Menubutton(topframe, relief='raised', text='⚙       ')
	settings_menubutton.config(width=22,bg="#36454f", height=2, fg="white")
	settings_menubutton.grid(row=1,column=4)
	settings_menubutton.menu =  Menu ( settings_menubutton, tearoff = 0 )
	settings_menubutton["menu"] =  settings_menubutton.menu
	settings_menubutton.menu.config(bg="grey",borderwidth=0,activeborderwidth=0, bd=0)

	loginVar = StringVar()
	checkoutVar = StringVar()
	settings_menubutton.menu.add_checkbutton ( label="▶ Login",variable=loginVar,command=grocery_page_method,selectcolor="blue")
	settings_menubutton.menu.add_checkbutton ( label="🛒 Checkout",variable=checkoutVar, command=grocery_page_method)
	settings_menubutton.menu.add_separator()
	settings_menubutton.menu.add_checkbutton ( label="⬜ Fullscreen", command=toggle_fullscreen)
	settings_menubutton.menu.add_checkbutton ( label="❌ Exit", command=root.quit)

	#Configuring earlier buttons
	button1.config(width=33, font="Palatino")
	button2.config(width=33, font="Palatino")
	button3.config(width=33, font="Palatino")
	button4.config(width=34, font="Palatino")
	#button5.config(width=20, font="Palatino")
	#entry4.config(width=43, font="Palatino")

	button1.grid(row=1, column =0) #grid - geometry manager pack 
	button2.grid(row=1, column =1)
	button3.grid(row=1, column =2)
	button4.grid(row=1, column =3, sticky = E)
	search_box.grid(row=1,column=3)
	#button5.grid(row=1,column=4)

	canvas_electronics = Canvas(topframe, width = 300, height = 230,bg="black",highlightthickness=0)  
	canvas_electronics.grid(row=2,column=0)
	canvas_electronics.create_image(20, 20, anchor=NW, image=electronics_img)

	#Grocery Image
	canvas_grocery = Canvas(topframe, width = 300, height = 230,bg="black",highlightthickness=0)  
	canvas_grocery.grid(row=2,column=1)
	canvas_grocery.create_image(20, 20, anchor=NW, image=grocery_img)

	#Clothing
	canvas_clothing = Canvas(topframe, width = 300, height = 230,bg="black",highlightthickness=0)  
	canvas_clothing.grid(row=2,column=2)
	canvas_clothing.create_image(20, 20, anchor=NW, image=clothing_img) 

	#Profile Pic
	canvas_profile = Canvas(topframe, width = 480, height = 230,bg="black",highlightthickness=0)  
	canvas_profile.grid(columnspan=2,row=2,column=3, sticky = E) 
	canvas_profile.create_image(20, 20, anchor=NW, image=logo_img)

	#Banner Pic
	canvas_profile = Canvas(topframe, width = 1520, height =700,bg="black",highlightthickness=0)  
	canvas_profile.grid(columnspan=6,row=3,column=0) 
	canvas_profile.create_image(20, 20, anchor=NW, image=banner_img) 
 

main_page()
root.mainloop()
