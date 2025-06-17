from tkinter import *

window=Tk()
window.minsize(width=400, height=100)
window.config(padx=50, pady=50)
window.title("Mile to Km Converter")


text_box=Entry()
text_box.grid(row=0,column=3)

label=Label()
label.config(text="Miles")
label.grid(row=0, column=4)

label2=Label()
label2.config(text="is equal to ")
label2.grid(row=1,column=1)

value=32
display=Label()

display.grid(row=1, column=3)

label4=Label()
label4.config(text="Km")
label4.grid(row=1, column=4)

def calculate_km():
    print("button clicked")
    miles = int(text_box.get())
    kilometers = round(miles * 1.60934)
    display.config(text=kilometers)



button=Button()
button.config(text="Calculate",command=calculate_km)
button.grid(row=2,column=3)








window.mainloop()