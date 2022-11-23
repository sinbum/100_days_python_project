from tkinter import *
import time

window = Tk()
window.title("My First GUI Program")
window.minsize(width=500, height=300)

# Label
my_label = Label(text="I Am a Label", font=("Arial", 12, "bold"))
my_label.pack()
my_label.config(text="New Text")


def button_clicked():
    print("I got clicked")
    new_text = input.get()
    my_label.config(text=new_text)


def timer():
    sec = int(input2.get())
    while sec != 0:
        sec = sec - 1
        time.sleep(1)
        my_label.config(text=str(sec))


# Button
button = Button(text="Click me", command=button_clicked)
button.pack()

# Entry
input = Entry(width=10)
input.pack()


# Button2
button2 = Button(text="Timer Start", command=timer)
button2.pack()

# Entry
input2 = Entry(width=10)
input2.pack()

print(input.get())

window.mainloop()
