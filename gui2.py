from tkinter import *
#Lable = an area widget that holds text and/or an image within window
Window=Tk()
photo=PhotoImage(file="C:\\Users\\USER\\Desktop\\github\\my--progaram\\image.png")
label=Label(Window,
            text="HELLO ZANTHA",
            font=("Arial",40,"bold"),
            fg="green",
            bg="black",
            relief=RAISED,
            bd=10,
            padx=20,
            pady=20,
            image=photo,
            compound="bottom")
label.pack()

#label.place(x=100,y=100)

Window.mainloop()