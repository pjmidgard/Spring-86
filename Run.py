# importing the tkinter module and PIL
# that is pillow module
from tkinter import *
from PIL import ImageTk, Image
import os

def back(img_no):
 
    # We will have global variable to access these
    # variable and change whenever needed
    global label
    global button_run
    label.grid_forget()
 
    # for clearing the image for new image to pop up
    label = Label(image=List_images[img_no - 1])
    label.grid(row=1, column=0, columnspan=3)
    button_run = Button(root, text="Run")
  
    print(img_no)
 
 
    
 
    label.grid(row=1, column=0, columnspan=3)

    button_for.grid(row=5, column=2)
 
 

root = Tk()
 

root.title("Image Viewer")
 

root.geometry("700x700")
 

image_no_1 = ImageTk.PhotoImage(Image.open("smaple1.jfif"))

 

List_images = [image_no_1]
 
label = Label(image=image_no_1)
 
label.grid(row=1, column=0, columnspan=3)
 
button_run = Button(root, text="Run",
                        command=lambda: os.startfile('Spring-86.py'))

 
button_run.grid(row=5, column=2)

 
root.mainloop()
