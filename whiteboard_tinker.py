from tkinter import *
from tkinter.colorchooser import askcolor
from tkinter import ttk
import tkinter as tk

root=Tk()
root.title(" Thukk White-Board")
root.geometry("1050x570+150+50")
root.configure(bg="#f2f3f5")
root.resizable(False,False)

current_x = 0
current_y = 0
color = 'black'

def locate_xy(work):
    global current_x, current_y
    current_x = work.x
    current_y = work.y

def addLine(work):
    global current_x  , current_y
    canvas.create_line((current_x,current_y,work.x,work.y),width=get_current_value(),fill=color,capstyle=ROUND,smooth=TRUE) 
    current_x, current_y =work.x, work.y

def show_color(new_color):
    global color

    color=new_color

def new_canvas():
    canvas.delete('all')
    display_pallete()


#icon
image_icon=PhotoImage(file="thukkpad.png")
root.iconphoto(False,image_icon)


color_box=PhotoImage(file="color selection.png")
Label(root,image=color_box, bg="#f2f3f5").place(x=12,y=40)

eraser=PhotoImage(file="eraser1.png")
Button(root, image=eraser,bg="#f2f3f5", command= new_canvas).place(x=30,y=400)

colors=Canvas(root,bg="#ffffff",width=30,height= 250,bd=0)
colors.place(x=30,y=60)

def display_pallete():
    id=colors.create_rectangle((8,10,27,30),fill="black")
    colors.tag_bind(id,'<Button-1>',lambda x: show_color("black")) 

    id=colors.create_rectangle((8,40,27,60),fill="gray")
    colors.tag_bind(id,'<Button-1>',lambda x: show_color("gray"))

    id=colors.create_rectangle((8,70,27,90),fill="brown4")
    colors.tag_bind(id,'<Button-1>',lambda x: show_color("brown4")) 

    id=colors.create_rectangle((8,100,27,120),fill="red")
    colors.tag_bind(id,'<Button-1>',lambda x: show_color("red")) 

    id=colors.create_rectangle((8,130,27,150),fill="yellow")
    colors.tag_bind(id,'<Button-1>',lambda x: show_color("yellow"))
    
    id=colors.create_rectangle((8,160,27,180),fill="green")
    colors.tag_bind(id,'<Button-1>',lambda x: show_color("green")) 

    id=colors.create_rectangle((8,190,27,210),fill="blue")
    colors.tag_bind(id,'<Button-1>',lambda x: show_color("blue"))

    id=colors.create_rectangle((8,220,27,240),fill="purple")
    colors.tag_bind(id,'<Button-1>',lambda x: show_color("purple"))

display_pallete()


canvas=Canvas(root,width=930,height=500, background="white",cursor="hand2")
canvas.place(x=100,y=10)

canvas.bind('<Button-1>',locate_xy)
canvas.bind('<B1-Motion>', addLine)

######################slider####################3
current_value=tk.DoubleVar()

def get_current_value():
    return '{:.2f}' .format(current_value.get())

def slider_changed(event):
    value_label.configure(text=get_current_value())



slider=ttk.Scale(root,from_=0,to=100,orient='horizontal', command=slider_changed, variable=current_value)
slider.place(x=30,y=530)

### vlaue labdel
value_label=ttk.Label(root,text=get_current_value())
value_label.place(x=27,y=550)


root.mainloop()

