from tkinter import *
import math

PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = 0

def reset_timer():
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text= "00:00")
    canvas.label.config(text="Timer")
    canvas.check.config(text="")



def start_timer():
    global reps
    reps += 1

    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    if reps % 8 == 0:
        count_down(long_break_sec)
        canvas.label.config(text="BREAK", font=(FONT_NAME, 60, "bold"), fg=RED)

    elif reps % 2 == 0:
        count_down(short_break_sec)
        canvas.label.config(text="BREAK", font=(FONT_NAME, 60, "bold"), fg=PINK)
    else:
        count_down(work_sec)
        canvas.label.config(text="WORK", font=(FONT_NAME, 60, "bold"), fg=GREEN)



def count_down(count):
    count_min = math.floor(count / 60)
    count_sec = count % 60
    if count_sec == 0:
        count_sec = "00"
    elif count_sec < 10:
        count_sec = f"0{count_sec}"
    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count >0:
        global timer
        timer = window.after(1000,count_down, count-1)
    else:
        start_timer()
        mark = ""
        work_sessions = math.floor(reps/2)
        for _ in range(work_sessions):
            mark += "✔"
        canvas.check.config(text=mark)


window = Tk()
window.title("POMODORO")
window.config(padx=10, pady=5, bg=YELLOW)


canvas = Canvas(width=600, height=600, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="pngwing.com.png")
canvas.create_image(300, 300, image=tomato_img)
canvas.grid(column=1, row=1)

timer_text = canvas.create_text(300, 360, text="00:00",fill="white", font=(FONT_NAME, 60,"bold"))
canvas.label = Label(text="Timer", font=(FONT_NAME,60,"bold"), fg=GREEN)
canvas.label.grid(column=1, row=0)
canvas.label.config(bg = YELLOW)

canvas.button_start= Button(text = "Start",font=(FONT_NAME, 15,"bold"), width=20, height=2, command=start_timer, highlightthickness=0)
canvas.button_start.grid(column=0, row=3)

canvas.button_reset= Button(text = "Reset",font=(FONT_NAME, 15,"bold"),width=20, height=2, command= reset_timer,  highlightthickness=0)
canvas.button_reset.grid(column=3, row=3)

canvas.check = Label(font=(FONT_NAME,30,"bold"),fg=GREEN)
canvas.check.grid(column=1, row=3)
canvas.check.config(bg=YELLOW)







window.mainloop()