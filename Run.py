# importing the tkinter module and PIL
# that is pillow module
from tkinter import *
from PIL import ImageTk, Image
import os
 
 
 
def back(img_no):
 
    # We will have global variable to access these
    # variable and change whenever needed
   
    global button_run
    
    button_run = Button(root, text="run",
                            command)
    
    print(img_no)
 
    # whenever the first image will be there we will
    # have the back button disabled
    
 
    
    button_for.grid(row=5, column=2)
 
 
# Calling the Tk (The initial constructor of tkinter)
root = Tk()
 
# We will make the title of our app as Image Viewer
root.title("Image Viewer")
 
# The geometry of the box which will be displayed
# on the screen
root.geometry("700x700")
 
# Adding the images using the pillow module which
# has a class ImageTk We can directly add the
# photos in the tkinter folder or we have to
# give a proper path for the images
image_no_1 = ImageTk.PhotoImage(Image.open("smaple1.jfif"))

 
# List of the images so that we traverse the list
List_images = [image_no_1]
 
button_run = Button(root, text="run",
                        command=lambda: os.startfile('Spring-86.py'))

 
# grid function is for placing the buttons in the frame

button_run.grid(row=5, column=2)

root.mainloop()
