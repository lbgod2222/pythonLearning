import tkinter as tk
import turtle
# main panel
root = tk.Tk()
# label
label = tk.Label(root,text='Hey there')
label.pack()
# define the func first
def draw(event):
    for i in range(5):
        turtle.forward(100)
        turtle.right(144)
# button
button1 = tk.Button(root,text='OKAY')
button1.pack()
button1.bind('<Button-1>',draw) #bind function already exist
#menu
menu = tk.Menu(root)
submenu = tk.Menu(menu,tearoff=0) #tearoff menu
submenu.add_command(label='Open') #tearoff menu
submenu.add_command(label='Save') #tearoff menu
submenu.add_cascade(label='File',menu=submenu) #tearoff menu
root.config(menu=menu)
# 执行循环
root.mainloop()