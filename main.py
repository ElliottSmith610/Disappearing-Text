from tkinter import *

TIMER = 0
SECONDS = 10
FONT = ("Arial", 16, "normal")

#  To start the check with a button
# def start_writing():
#     text.config(state=NORMAL, bg="white")
#     text.focus()
#     old_text = ""
#     writing_check(SECONDS, old_text)

# TODO: Add Scrollbar to text area


def writing_check(seconds, old_text):

    new_text = text.get("1.0", "end")
    if seconds == 0:
        text.delete("1.0", "end")
        counter.config(text=f"")
        # text.config(state=DISABLED, bg="grey")

    if old_text == new_text and new_text != "\n":
        seconds -= 1
        if -1 < seconds <= 5:
            counter.config(text=f"{seconds}")
    else:
        old_text = new_text
        seconds = 10
        counter.config(text=f"")
    w.after(1000, writing_check, seconds, old_text)


# Interface
w = Tk()
w.title("Disappearing Text App")
w.geometry("600x500")
w.config(padx=20, pady=20)

title = Label(text="Continue writing or all your text will disappear!",
              font=FONT)
title.pack(pady=(0, 20))

# Originally Used a button to start the timer
# button = Button(text="Start", command=start_writing)
# button.pack()
counter = Label(text="", font=FONT)
counter.pack(pady=(20, 20))
text = Text(width=70, height=20, wrap=WORD, )  # state=DISABLED, bg="grey"
text.focus()
text.pack()

writing_check(SECONDS, text.get("1.0", "end"))
w.mainloop()
