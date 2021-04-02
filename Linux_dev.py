# Web PDF Saver (Standard GUI-Linux). Liscensed under Apache-2.0. 
# THIS IS NOT A RELEASE, for internal testing purposes only.

# Not in standard library- img2pdf, pyautogui, PIL
import img2pdf
import time
import tkinter as tk
from PIL import ImageGrab
import pyautogui
import os

#Main window creation

# Top level window 
frame = tk.Tk() 
frame.title("Screenshot PDF maker") 
frame.geometry('400x400') 
frame.wm_attributes('-alpha',1)

# Transparent Button Creation 
def makeTrans():
	frame.update()
	frame.wm_attributes('-alpha',0.3)
	frame.update()
	
transButton = tk.Button(frame, 
	text = "Make window transparent for ease", 
	command = makeTrans)


# TextBox Creation 
inplabBookName = tk.Text(frame, 
	height = 2, 
	width = 20) 

inpSaveLoc = tk.Text(frame, 
	height = 2, 
	width = 20) 

inpPageNo = tk.Text(frame, 
	height = 2, 
	width = 20) 

# Create labels for main page
labBookName = tk.Label(frame, text = "Book name") 
labBookName.config(font =("Arial", 8)) 

labIns = tk.Label(frame, text = "Arrange and shape the window so that it covers the entire page.\n Do not include title bar") 
labIns.config(font =("Arial", 9)) 

labSaveLoc = tk.Label(frame, text = "Location") 
labSaveLoc.config(font =("Arial", 7)) 

labPageNum = tk.Label(frame, text = "Number of pages") 
labPageNum.config(font =("Arial", 7)) 

#Pack everything
labIns.pack()
transButton.pack()
labBookName.pack()
inplabBookName.pack()
labSaveLoc.pack()
inpSaveLoc.pack() 
inpSaveLoc.insert(tk.END, os.path.expanduser("~/books"))
labPageNum.pack() 
inpPageNo.pack()
frame.wait_visibility(frame)

#Next Button
var = tk.IntVar()
nextButton = tk.Button(frame, text="Next", command=lambda: var.set(10))
nextButton.pack()

nextButton.wait_variable(var)

#Perpare mouse detection screen

#Remove old elements
labIns.pack_forget()
transButton.pack_forget()
labBookName.pack_forget()
inplabBookName.pack_forget()
labSaveLoc.pack_forget()
inpSaveLoc.pack_forget() 
labPageNum.pack_forget() 
inpPageNo.pack_forget()
nextButton.pack_forget() 
frame.wm_attributes('-alpha', 1)

# Create labels
labMouseX = tk.Label(frame, text = "Mouse X") 
labMouseX.config(font =("Arial", 7)) 

labMouseY = tk.Label(frame, text = "Mouse Y") 
labMouseY.config(font =("Arial", 7))


#text inputs for mouse screen
inpmox = tk.Text(frame, 
	height = 2, 
	width = 20) 

inpmoy = tk.Text(frame, 
	height = 2, 
	width = 20) 

inpWait = tk.Text(frame, 
	height = 2, 
	width = 20) 

autoDetlabIns = tk.Label(frame, text = "Press the button and go to labSaveLoc. \n The co-ords will be picked up 3 seconds after press.") 
autoDetlabIns.config(font =("Arial", 7)) 

waitlabIns = tk.Label(frame, text = "Seconds of delay it takes to change page after clicking")
waitlabIns.config(font =("Arial", 7)) 

startlabIns = tk.Label(frame, text = "This window will disappear. You will hear a Beep everytime a screen shot is taken.") 
startlabIns.config(font =("Arial", 7)) 
inpmoy.insert(tk.END, "1")

#buttons for mouse screen
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


#Pack everything for mouse screen
labMouseX.pack()
inpmox.pack()
labMouseY.pack()
inpmoy.pack()
autoDetlabIns.pack()
autodet.pack()
waitlabIns.pack()
inpWait.pack()
startlabIns.pack()

# Start button creation
var = tk.IntVar()
startButton = tk.Button(frame, text="Start", command=lambda: var.set(1))
startButton.pack()

frame.update_idletasks()
frame.update()

startButton.wait_variable(var)

 #Remove all elements and show "processing..."
labMouseX.pack_forget()
labMouseY.pack_forget()
autoDetlabIns.pack_forget()
autodet.pack_forget()
startlabIns.pack_forget()
startButton.pack_forget()
frame.wm_attributes('-alpha', 0)

frame.update_idletasks()
frame.update()
#Main processing

def main():
	save_Loc = inpSaveLoc.get("1.0", "end-1c") 
	doc = inplabBookName.get("1.0", "end-1c")
	num_pages = int(inpPageNo.get("1.0", "end-1c"))
	waitTime = int(inpWait.get("1.0", "end-1c"))
	varInpMoY = int(inpmoy.get("1.0",'end-1c'))
	varInpMoX = int(inpmox.get("1.0",'end-1c'))
	inpmox.insert(tk.END, "processing...") 
	inpmoy.pack_forget()
	print(varInpMoY, varInpMoX)
	os.makedirs(save_Loc + "/" + doc)
	imgs =[]

	for pg_num in range(num_pages):
		print('On page', str(pg_num + 1))
		im = ImageGrab.grab(bbox=(frame.winfo_rootx(), frame.winfo_rooty(), frame.winfo_width(), frame.winfo_height()))
		list1 = [save_Loc, "/", doc, "/", str(pg_num + 1),".png"]
		finSavLoc = "".join(list1)
		print(finSavLoc)
		im.save(finSavLoc)
		imgs.append(finSavLoc)
		time.sleep(waitTime)
		print(save_Loc)		
		#Flip page
		pyautogui.moveTo(varInpMoX, varInpMoY)
		pyautogui.click()
			
	inpmox.insert(tk.END, "Combinig PDF...") 
	with open(save_Loc + "/" + doc + "/" + doc +".pdf" ,"wb") as f:
		f.write(img2pdf.convert(imgs))
 
if __name__ == "__main__":
    main()
