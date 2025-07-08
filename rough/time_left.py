from tkinter import *

window=Tk()
window.minsize(width=300, height=200)
window.title('miles to km converter')
window.config(padx=100,pady=100)

my_label=Label()
my_label.config()
#my_label.pack()

def convert_to_km():
    miles=miles_box.get()
    km=1.6*int(miles)
    km_value.config(text=km)

label=Label(text="enter miles")
label.grid(row=0,column=3  )

miles_box=Entry()
miles_box.grid(row=1, column=3)

km_value=Label()
km_value.grid(row=2, column=3)

unit_label=Label(text="km")
unit_label.grid(row=2, column=4)




button = Button(text="convert to km",command=convert_to_km)
button.grid(row=3,column=3)


window.mainloop()