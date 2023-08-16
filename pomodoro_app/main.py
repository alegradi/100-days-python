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
check_marks = ""
timer = None

# ---------------------------- TIMER RESET ------------------------------- # 


def reset_timer():
    global reps
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00:00")
    timer_label.config(text="Timer")
    check_marks_label.config(text="")
    reps = 0


# ---------------------------- TIMER MECHANISM ------------------------------- # 

def start_timer():
    global reps
    reps += 1

    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    if reps == 8:
        count_down(long_break_sec)
        timer_label.config(text="Break", fg=RED)
        reps = 0  # Reset sessions after a long break
    elif reps % 2 == 0:
        count_down(short_break_sec)
        timer_label.config(text="Break", fg=PINK)
    else:
        count_down(work_sec)
        timer_label.config(text="Work", fg=GREEN)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):
    global reps
    global check_marks
    global timer

    count_min = math.floor(count / 60)
    count_sec = count % 60
    if count_sec < 10:
        count_sec = "0" + str(count_sec)  # Unique python fuckery with dynamic typing

    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        timer = (window.after(1000, count_down, count - 1))  # Counter
    else:
        start_timer()

        if reps % 2 == 0:
            check_marks += "✔"
            check_marks_label.config(text=check_marks)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro app")
window.config(padx=100, pady=50, bg=YELLOW)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100, 140, text="00:00", fill="white", font=(FONT_NAME, 30, "bold"))
canvas.grid(column=1, row=1)

# Timer
timer_label = Label(text="Timer", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 20, "bold"))
timer_label.grid(column=1, row=0)

# Start button
start_button = Button(text="Start", bg="white", command=start_timer)
start_button.grid(column=0, row=2)

# Reset button
reset_button = Button(text="Reset", bg="white", command=reset_timer)
reset_button.grid(column=2, row=2)

# Check mark label
check_marks_label = Label(fg=GREEN, bg=YELLOW, font=(FONT_NAME, 16, "bold"))
check_marks_label.grid(column=1, row=3)

window.mainloop()