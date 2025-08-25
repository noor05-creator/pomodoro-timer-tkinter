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
reps = 1
timer = None
# ---------------------------- TIMER RESET ------------------------------- # 
def reset():

    window.after_cancel(timer)
    canvas.itemconfig(canvas_text,text="00:00")
    timer_label.config(text="Timer")
    tick_label.config(text="")
    global reps
    reps = 0

# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global reps
    work_sec = WORK_MIN *60
    short_break_sec = SHORT_BREAK_MIN *60
    long_break_sec = LONG_BREAK_MIN *60


    #work period
    if reps % 2 != 0:
        reps += 1
        timer_label.config(text="Work", fg=GREEN)

        count_down(work_sec)

    #long break
    elif reps / 2 == 4:
        reps += 1
        timer_label.config(text="Break", fg=RED)

        count_down(long_break_sec)
    else:
        timer_label.config(text="Break", fg=PINK)

        reps += 1
        count_down(short_break_sec)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):

    count_min = math.floor(count/60)
    count_sec = count % 60

    if count_sec < 10:
        count_sec = "0" + str(count_sec)

    canvas.itemconfig(canvas_text,text = f"{count_min}:{count_sec}")

    if count > 0:
        global timer
        print(count)
        timer = window.after(1000,count_down,count - 1)
    else:
        start_timer()
        mark = ""
        work_sessions = math.floor(reps / 2)
        for _ in range(work_sessions):
            mark += "✅"
        tick_label.config(text=mark)

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx = 100,pady = 50,bg= YELLOW)

canvas = Canvas(width = 210, height = 224, bg=YELLOW,highlightthickness=0)
tomato_img = PhotoImage(file = "tomato.png")
canvas.create_image(103,112,image=tomato_img)
canvas_text = canvas.create_text(103,130,text = "00:00",fill = "white",font = (FONT_NAME,35,"bold"))
canvas.grid(column = 2, row = 2)

timer_label = Label(text="Timer", font=(FONT_NAME, 35, "bold"), fg=GREEN, bg=YELLOW, highlightthickness=0)
timer_label.grid(row=0, column=2)


start_button = Button(text = "Start",command = start_timer)
start_button.grid(column = 1, row = 3)

reset_button = Button(text = "Reset",command = reset)
reset_button.grid(column = 4, row = 3)

tick_label = Label(fg = GREEN,bg=YELLOW,highlightthickness = 0)
tick_label.grid(column = 2, row = 4)






window.mainloop()