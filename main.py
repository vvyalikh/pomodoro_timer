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
reps = 0
timer = None
# ---------------------------- TIMER RESET ------------------------------- # 
def reset_timer():
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00:00")
    title_label.config(text="Timer", fg=GREEN)
    check_marks.config(text="")
    #to reset reps and start from the very beginning
    global reps
    reps = 0

# ---------------------------- TIMER MECHANISM ------------------------------- #

def timer_button():
    global reps
    reps += 1
    work_sec = WORK_MIN*60
    short_break_sec = SHORT_BREAK_MIN*60
    long_break_sec = LONG_BREAK_MIN*60

    if reps % 8 == 0:
        countdown(long_break_sec)
        title_label.config(text="Long Break", fg=RED)
    elif reps % 2 == 0:
        countdown(short_break_sec)
        title_label.config(text="Short Break", fg=PINK)
    else:
        countdown(work_sec)
        title_label.config(text="Time to work", fg=GREEN)



# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def countdown(count):
    count_min = math.floor(count/60)
    count_sec = count % 60
    #dynamic typing. Change of variable type from int to a string
    if count_sec == 0:
        count_sec = "00"
    elif count_sec < 10:
        count_sec = f"0{count_sec}"

    #to change exact item in canvas
    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    print(count)
    if count > 0:
        global timer
        timer = window.after(1000, countdown, count-1)
    else:
        timer_button()
        marks = ""
        work_sessions = math.floor(reps/2)
        for _ in range(work_sessions):
            marks += "✔"
        check_marks.config(text=marks)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("p_timer")
window.config(padx=100, pady=50, bg=YELLOW)

# grid shows where title is on grid
title_label = Label(text="Timer", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 36, "bold"))
title_label.grid(column=1, row=0)


canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100.3, 112, image=tomato_img)
timer_text = canvas.create_text(105, 120, text="00:00", fill="white", font=(FONT_NAME, 20, "bold"))
#grid shows where tomato is on grid
canvas.grid(column=1, row=1)


start_button = Button(text="Start", fg=PINK, bg=YELLOW, font=(FONT_NAME, 18, "bold"), highlightthickness=5, command=timer_button)
start_button.grid(column=0, row=3)


reset_button = Button(text="Reset", fg=PINK, bg=YELLOW, font=(FONT_NAME, 18, "bold"), highlightthickness=5, command=reset_timer)
reset_button.grid(column=3, row=3)

check_marks = Label(fg=GREEN, bg=YELLOW, font=(FONT_NAME, 20, "italic"))
check_marks.grid(column=1, row=3)








window.mainloop()