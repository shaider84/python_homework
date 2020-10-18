from tkinter import *

#Create main root widget
root = Tk()

#Create a Label Widget
my_label = Label(root, text="Hello World!!!!!!!")
my_label2 = Label(root, text="Hello World!2")

#define where in root to place my_label widget
#my_label2.pack()
#my_label.pack()

#Use the Grid system to define where to place items
my_label.grid(row=0, column=0 )
my_label2.grid(row=1, column=1 )

#main program loop
root.mainloop()