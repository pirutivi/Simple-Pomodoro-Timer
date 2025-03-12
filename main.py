from tkinter import *
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps=0
time=None

# ---------------------------- TIMER RESET ------------------------------- #
def reset():
    window.after_cancel(time)
    canvas.itemconfig(timer,text="00:00")
    label_timer.config(text="Time")
    check_marks.config(text="")
    global reps
    reps=0

# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer():
    global reps
    reps+=1

    work_sec=WORK_MIN*60
    short_break_sec=SHORT_BREAK_MIN*60
    long_break_sec=LONG_BREAK_MIN*60

    if reps%8==0:
        count_down(long_break_sec)
        label_timer.config(text="Break",fg=RED)
    elif reps%2==0:
        count_down(short_break_sec)
        label_timer.config(text="Break", fg=PINK)
    else:
        count_down(work_sec)
        label_timer.config(text="Work", fg=GREEN)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):
    count_min=math.floor(count/60)
    count_sec=count%60
    if count<10:
        count=f"0{count_sec}"
    canvas.itemconfig(timer,text=f"{count_min}:{count_sec}")
    if count>0:
        global time
        time=window.after(1000,count_down,count-1)
    else:
        start_timer()
        marks=""
        work_session=math.floor(reps/2)
        for i in range(work_session):
            marks+="✔"
        check_marks.config(marks)


# ---------------------------- UI SETUP -------------------------------#

window=Tk()
window.title("Pomodoro")
window.config(padx=100,pady=50,bg=YELLOW)


canvas=Canvas(width=200,height=224,bg=YELLOW,highlightthickness=0)
photo_image=PhotoImage(file="tomato.png")
canvas.create_image(100,112,image=photo_image)
timer=canvas.create_text(100,130,text="00.00",fill="white",font=(FONT_NAME,"35","bold"))
canvas.grid(column=1,row=1)



label_timer=Label(text="Timer",fg=GREEN,bg=YELLOW,font=(FONT_NAME,50,"bold"))
label_timer.grid(column=1,row=0)

start_button=Button(text="Start",highlightthickness=0,command=start_timer)
start_button.grid(column=0,row=2)

reset_button=Button(text="Reset",highlightthickness=0,command=reset)
reset_button.grid(column=2,row=2)

check_marks=Label(text="✔",fg=GREEN,bg=YELLOW)
check_marks.grid(column=1,row=3)



window.mainloop()