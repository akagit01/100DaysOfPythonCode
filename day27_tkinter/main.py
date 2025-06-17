import tkinter

window = tkinter.Tk()

window.title("My first GUI program")
window.minsize(width=600,height=300)
window.config(padx=100, pady=200, bg="gray")

#label generated from label class of tkinter
my_label=tkinter.Label()
#(text="My First Label",font=("Aerial",24,"bold"))
my_label.config(text="My First Label",font=("Aerial",24,"bold"))
#my_label.pack()
#my_label.place(x=100,y=0)
my_label.grid(column=0, row=0)

#entry
input=tkinter.Entry()
input.config(width=10)
#input.pack()
input.grid(column=1,row=1)

def button_Clicked():
    text_in_box = input.get()
    my_label.config(text=text_in_box)

#creating button
button=tkinter.Button()
button.config(text="submit",command=button_Clicked)
#button.pack()
button.grid(column=1, row=2)

button2=tkinter.Button()
button2.config(text="new button",width=10)
button2.grid(column=3, row=0)






window.mainloop()