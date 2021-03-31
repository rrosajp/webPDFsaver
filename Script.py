#matplt, fpdf and numpy, pyauto
import time
import numpy as np
import matplotlib.pyplot as plt
from fpdf import FPDF
import pyautogui
import tkinter as tk


def get_page():
	x1 = frame.winfo_rootx()
	x2 = frame.winfo_rootx() + frame.winfo_width()
	y1 = frame.winfo_rooty()
	y2 = frame.winfo_rootx() + frame.winfo_height()

	return np.array(pyautogui.screenshot(region=(frame.winfo_rootx(), frame.winfo_rooty(), frame.winfo_width(), frame.winfo_height())))

def flip_page():
	varinpmoy = int(inpmoy.get("1.0", "end-1c"))
	varinpmox = int(inpmox.get("1.0", "end-1c"))
	pyautogui.moveTo(varinpmox, varinpmoy)
	pyautogui.click()

def main():
	save_Loc = inputtxt2.get("1.0", "end-1c") 
	doc = inputtxt.get("1.0", "end-1c")
	varinpmoy = inpmoy.get("1.0", "end-1c")
	varinpmox = inpmox.get("1.0", "end-1c")
	num_pages = inputtxt3.get("1.0", "end-1c")
	

	for pg_num in range(int(num_pages)):
		print('On page', str(pg_num + 1))
		page = get_page()
		plt.imsave(save_Loc + doc + str(pg_num) + '.png', page)
		time.sleep(1)
		print(save_Loc)
		flip_page()
	
	frame.wm_attributes('-alpha', 1)
	mousex.pack_forget()
	mousey.pack_forget()
	inpmox.delete(1.0, tk.END)
	inpmox.insert(tk.END, "Done.") 
	inpmoy.pack_forget()
	autoDetIns.pack_forget()
	autodet.pack_forget()
	startIns.pack_forget()
	startButton.pack_forget()


def Start():

	wx, wy = frame.winfo_rootx(), frame.winfo_rooty()
	print(wx, wy)
	frame.wm_attributes('-alpha', 0)
	if __name__ == '__main__':
	  main()

def makeTrans():
	frame.update()
	frame.wm_attributes('-alpha',0.3)
	frame.update()

def next():
	ins.pack_forget()
	transButton.pack_forget()
	bookName.pack_forget()
	inputtxt.pack_forget()
	location.pack_forget()
	inputtxt2.pack_forget() 
	pageNum.pack_forget() 
	inputtxt3.pack_forget()
	nextButton.pack_forget() 
	frame.wm_attributes('-alpha',1)

	mousex.pack()
	inpmox.pack()
	mousey.pack()
	inpmoy.pack()
	autoDetIns.pack()
	autodet.pack()
	startIns.pack()
	startButton.pack()


	

# Top level window 
frame = tk.Tk() 
frame.title("Screenshot PDF maker") 
frame.geometry('400x400') 
frame.wm_attributes('-alpha',1)


# TextBox Creation 
inputtxt = tk.Text(frame, 
				height = 2, 
				width = 20) 

inputtxt2 = tk.Text(frame, 
				height = 2, 
				width = 20) 

inputtxt3 = tk.Text(frame, 
				height = 2, 
				width = 20) 



#next Button Creation 
nextButton = tk.Button(frame, 
						text = "Next", 
						command = next)

# transButton Creation 
transButton = tk.Button(frame, 
						text = "Make window transparent for ease", 
						command = makeTrans)


# Create label 
bookName = tk.Label(frame, text = "Book name") 
bookName.config(font =("Arial", 8)) 

# Create label 
ins = tk.Label(frame, text = "Arrange and shape the window so that it covers the entire page.\n Do not include title bar") 
ins.config(font =("Arial", 9)) 


# Create label 
location = tk.Label(frame, text = "Location") 
location.config(font =("Arial", 7)) 

# Create label 
pageNum = tk.Label(frame, text = "Number of pages") 
pageNum.config(font =("Arial", 7)) 

ins.pack()
transButton.pack()
bookName.pack()
inputtxt.pack()
location.pack()
inputtxt2.pack() 
inputtxt2.insert(tk.END, "D:\Books")
pageNum.pack() 
inputtxt3.pack()
nextButton.pack() 
frame.wait_visibility(frame)

#Mouse detector
# Create label 
mousex = tk.Label(frame, text = "Mouse X") 
mousex.config(font =("Arial", 7)) 
# Create label 
mousey = tk.Label(frame, text = "Mouse Y") 
mousey.config(font =("Arial", 7)) 

# Create label 
autoDetIns = tk.Label(frame, text = "Press the button and go to location. \n The co-ords will be picked up 3 seconds after press.") 
autoDetIns.config(font =("Arial", 7)) 

# Create label 
startIns = tk.Label(frame, text = "This window will disappear. You will hear a Beep everytime a screen shot is taken.") 
startIns.config(font =("Arial", 7)) 


#text inputs for mouse
inpmox = tk.Text(frame, 
				height = 2, 
				width = 20) 

inpmoy = tk.Text(frame, 
				height = 2, 
				width = 20) 

#buttons for mouse

def autodetmouse():
	time.sleep(3)
	temx, temy = pyautogui.position()
	inpmox.delete(1.0, tk.END)
	inpmoy.delete(1.0, tk.END)
	inpmox.insert(tk.END, temx) 
	inpmoy.insert(tk.END, temy)

autodet = tk.Button(frame, 
	text = "Auto detect mouse position", 
	command = autodetmouse)

startButton = tk.Button(frame, 
	text = "Start", 
	command = Start)

tk.mainloop()