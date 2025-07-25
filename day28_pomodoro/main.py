from tkinter import *
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 1
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
CHECK_ICON="✅"
timer = None

# ---------------------------- TIMER RESET ------------------------------- # 

def reset_timer():
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text=f"00:00")
    label.config(text="Timer", fg=GREEN)
    check_mark_icon.config(text="")
    global reps
    reps=0

# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global reps
    reps += 1

    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    if reps % 8 == 0:
        count_down(long_break_sec)
        label.config(text="break",fg=RED)
    elif reps % 2 == 0:
        count_down(short_break_sec)
        label.config(text="break", fg=PINK)
    else:
        count_down(work_sec)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):
    global CHECK_ICON

    count_min=math.floor(count / 60)
    count_sec=count % 60
    if count_sec < 10:
        count_sec=f"0{count_sec}"
        canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")

    elif count_min < 10:
        count_min=f"0{count_min}"
        canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    else:
        canvas.itemconfig(timer_text,text=f"{count_min}:{count_sec}")

    if count > 0:
       global timer
       timer =  window.after(1000,count_down,count - 1)
    else:
        start_timer()
        check_mark_icon.config(text=CHECK_ICON * (math.floor(reps / 2)), bg=GREEN)
# ---------------------------- UI SETUP ------------------------------- #
window=Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

label=Label(text="Timer",font=("Aerial",30,"bold"),fg=GREEN, bg=YELLOW)
label.grid(row=0, column=2)

canvas=Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img=PhotoImage(file="tomato.png")
canvas.create_image(100,112,image=tomato_img)
timer_text=canvas.create_text(100 ,130, text="00:00", fill="white", font=(FONT_NAME,35,"bold"))
canvas.grid(row=2, column=2)

#count_down(5)

button=Button(text="Start", highlightthickness=0, command=start_timer)
button.grid(row=3,column=1)

check_mark_icon=Label(text="")
check_mark_icon.grid(row=3, column=2)

button=Button(text="Reset", command=reset_timer)
button.grid(row=3,column=4)



window.mainloop()