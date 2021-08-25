from tkinter import *
from PIL import ImageTk,Image,ImageDraw,ImageFont,ImageOps,ImageSequence 
import requests

root=Tk() #We're basically creating a blank window
root.geometry("2000x2000")

theLabel = Label(root, text = "Friple-A Shopping", bg="black", fg = "white") #Creating basic text; syntax Label(<where to put label>,<text>)
theLabel.config(width=200) #Changes width of the label box
theLabel.config(font=("Courier", 44)) #Change font of label Syntax - font=(<font name>, size)
theLabel.pack(fill=X) #Places it somewhere   ; Fill = X, enlarges the label along X direction if the window is enlarged; Fill = Y enlarges along Y axis

topframe = Frame(root) #Creates a frame in the gui window
topframe.pack()#To display the frame (invisible rectangle)

topframe.update()
print(topframe.winfo_width())

url = "https://cdn.pixabay.com/photo/2017/10/22/21/06/flat-2879273_960_720.jpg"
electronics_img = Image.open(requests.get(url, stream=True).raw)
electronics_img= electronics_img.resize((350,200),Image.ANTIALIAS)
electronics_img = ImageTk.PhotoImage(electronics_img)

url = "https://cdn.pixabay.com/photo/2016/04/21/11/32/groceries-1343141_960_720.jpg"
grocery_img = Image.open(requests.get(url, stream=True).raw)
grocery_img= grocery_img.resize((350,200), Image.ANTIALIAS)
grocery_img = ImageTk.PhotoImage(grocery_img)

url = "https://cdn.pixabay.com/photo/2015/10/12/15/18/store-984393_960_720.jpg"
clothing_img = Image.open(requests.get(url, stream=True).raw)
clothing_img= clothing_img.resize((350,200), Image.ANTIALIAS)
clothing_img = ImageTk.PhotoImage(clothing_img)

#url = "https://i.postimg.cc/pTPMtQGY/Profile-shop.png"
url = "https://image.flaticon.com/icons/png/512/848/848043.png"
profile_img = Image.open(requests.get(url, stream=True).raw)
profile_img= profile_img.resize((200,200), Image.ANTIALIAS)
profile_img = ImageTk.PhotoImage(profile_img)

'''
url = "https://i.ibb.co/bFmmcd3/e-commerce.jpg"
commerce_img = Image.open(requests.get(url, stream=True).raw)
commerce_img = commerce_img.resize((1200,580), Image.ANTIALIAS)
commerce_img = ImageTk.PhotoImage(commerce_img)
'''

def main_page():
	global electronics_img, grocery_img, clothing_img, profile_img
	global topframe
	for widget in topframe.winfo_children():
		widget.destroy()

	def settings_show():
		menu = button5['menu']
		menu.delete(0, tkinter.END)
		menu.add_command(label='new choice 1')
		menu.add_command(label='new choice 2')
		menu.add_separator()
		menu.add_command(label='new choice 3')
		optvar.set('new choice 1')

	button1=Button(topframe, text = "🎮 Electronics", fg = "white", bg = "black", command=electronics_page) #Adds a button. Syntax - Button(<where>, <text>, ForeGround = <colour>, BackGround = <colour>)
	button2=Button(topframe, text = "🛒 Grocery", fg = "white", bg =  "#000000", command = grocery_page)
	button3=Button(topframe, text = "👔 Clothing", fg = "white", bg =  "#000000", command=clothing_page)
	button4=Button(topframe, text = "🔍 Search", fg = "white", bg =  "#000000", command=profile_page)
	button5=Button(topframe, text = "⚙", fg="white", bg="black", command=settings_show)
	#entry4 = Entry(topframe, text = "🔍 Search", fg = "white", bg =  "grey")

	button1.config(width=30, font="Palatino")
	button2.config(width=30, font="Palatino")
	button3.config(width=30, font="Palatino")
	button4.config(width=30, font="Palatino")
	button5.config(width=20, font="Palatino")
	#entry4.config(width=43, font="Palatino")

	button1.grid(row=1, column =0) #grid - geometry manager pack 
	button2.grid(row=1, column =1)
	button3.grid(row=1, column =2)
	button4.grid(row=1, column =3, sticky = E)
	button5.grid(row=1,column=4)
	
	def show():
		label.config( text = clicked.get())
  
	# Dropdown menu options
	options = ["Profile","Settings","Orders"]
	  
	# datatype of menu text
	clicked = StringVar()
	  
	# initial menu text
	clicked.set( "Settings")
	  
	# Create Dropdown menu
	drop = OptionMenu( topframe , clicked , *options )
	drop.grid(row=2)
	  
	# Create button, it will change label text
	button_settings = Button( root , text = "Settings" , command = show ).pack()
	  
	# Create Label
	label = Label( topframe , text = " " )
	label.grid(row=2)

	canvas_electronics = Canvas(topframe, width = 300, height = 300)  
	canvas_electronics.grid(row=2,column=0)  
	canvas_electronics.create_image(20, 20, anchor=NW, image=electronics_img) 

	#Grocery Image
	canvas_grocery = Canvas(topframe, width = 300, height = 300)  
	canvas_grocery.grid(row=2,column=1) 
	canvas_grocery.create_image(20, 20, anchor=NW, image=grocery_img) 

	#Clothing
	canvas_clothing = Canvas(topframe, width = 300, height = 300)  
	canvas_clothing.grid(row=2,column=2) 
	canvas_clothing.create_image(20, 20, anchor=NW, image=clothing_img) 

	#Profile Pic
	canvas_profile = Canvas(topframe, width = 300, height = 300)  
	canvas_profile.grid(row=2,column=3, sticky = E) 
	canvas_profile.create_image(20, 20, anchor=NW, image=profile_img) 

	#canvas_commerce = Canvas(topframe, width = 1200, height = 580)  
	#canvas_commerce.grid(row=3,column=0, columnspan =4) 
	#canvas_commerce.create_image(30, 30, anchor=NW, image=commerce_img) 
#canvas_button=Button(topframe, text = 'Click Me !', image = profile_img, )
#canvas_button.grid(row=2,column=3)
def electronics_page():
	global topframe
	for widget in topframe.winfo_children():
		widget.destroy()
	button1=Button(topframe, text = "🎮 Electronics", fg = "white", bg = "black", command=main_page)
	button1.pack() 
def grocery_page():
	global topframe
	for widget in topframe.winfo_children():
		widget.destroy()
	button1=Button(topframe, text = "🛒 Grocery", fg = "white", bg = "black", command=main_page)
	button1.pack() 
def clothing_page():
	global topframe
	for widget in topframe.winfo_children():
		widget.destroy()
	button1=Button(topframe, text = "👔 Clothing", fg = "white", bg = "black", command=main_page)
	button1.pack() 
def profile_page():
	global topframe
	for widget in topframe.winfo_children():
		widget.destroy()
	button1=Button(topframe, text = "🔍 Search", fg = "white", bg = "black", command=main_page)
	button1.pack() 


main_page()
root.mainloop()
