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

# ---------------------------- TIMER RESET ------------------------------- # 

# ---------------------------- TIMER MECHANISM ------------------------------- #
def timer_button():
    countdown(5*60)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def countdown(count):
    count_min = math.floor(count/60)
    count_sec = count % 60

    #to change exact item in canvas
    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    print(count)
    if count > 0:
        window.after(1000, countdown, count-1)

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("p_timer")
window.config(padx=100, pady=50, bg=YELLOW)


#grid shows where title is on grid
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


reset_button = Button(text="Reset", fg=PINK, bg=YELLOW, font=(FONT_NAME, 18, "bold"), highlightthickness=5)
reset_button.grid(column=3, row=3)

check_marks = Label(text="✔", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 20, "italic"))
check_marks.grid(column=1, row=3)








window.mainloop()