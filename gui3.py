from tkinter import *
count=0
def click():
    global count
    count+=1
    Label1.config(text=count)
    Label2.pack()
Window=Tk()
button=Button(Window,text="click mee")
button.config(command=click)
button.config(font=("Ink free",50,"bold"))
button.config(bg="#ff6200")
button.config(fg="#fffb1f")
button.config(activebackground="#FF0000")
button.config(activeforeground="#fffb1f")
image1=PhotoImage(file="C:\\Users\\USER\\Desktop\\github\\my--progaram\\image.png")
button.config(image=image1)
button.config(compound="top")
#button.config(state=DISABLED
Label1=Label(Window,text=count)
Label1.config(font=("MOnospace",50))

Label1.pack()
button.pack()
Label2=Label(Window,image=image1)
Window,mainloop()