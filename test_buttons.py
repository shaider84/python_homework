from tkinter import *

#Create main root widget
root = Tk()
root.title("Simple App")

#String Variables
my_label_text = StringVar()
my_label_text.set("Hello World!!!!!!!")

#Create a Label Widget
my_label = Label(root, textvariable = my_label_text)
my_label2 = Label(root, text="Hello World!2")

def myClick():
    my_label_text.set("Hah, I pressed button")



#Create a Button Widget
my_button = Button(root, text = "OK/Yes", padx=50, pady=50, command=myClick)
#define where in root to place my_label widget
#my_label2.pack()
#my_label.pack()

#Use the Grid system to define where to place items
my_label.grid(row=0, column=0 )
my_label2.grid(row=3, column=1)
my_button.grid(row= 4, column = 3)

#Inital state




#main program loop
root.mainloop()