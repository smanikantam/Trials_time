from tkinter import *
root=Tk()
root.title("trials time")
root.geometry("400x300")
def b1():
	print("hello")
	l=Label(root,text="created new")
	l.pack()
def getx_y(event):
	global x1,y1
	x1,y1=event.x,event.y
def move_c(event):
	global x1,y1
	can.create_line((x1,y1,event.x,event.y),fill="black",width=5)
	x1,y1=event.x,event.y
def dele():
	can.delete("all")
can=Canvas(root,width=350,height=250,bg="white")
can.pack()
can.bind("<Button-1>",getx_y)
can.bind("<B1-Motion>",move_c)

b=Button(root,text="click",command=dele)
b.pack()


root.mainloop()