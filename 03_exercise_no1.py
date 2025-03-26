from tkinter import *
root = Tk()

root.title("Welcome")
computer = Label(root, bg="green", fg="white", text="Computer",
                 font=("Times", 50, "italic"))
science = Label(root, bg="blue", fg="yellow", text="science is",
                font=("Courier", 50, "bold"))
awesome = Label(root, bg="orange", fg="red", text="awesome!",
                font=("Times", 50, "bold"))
computer.pack(fill="x")
science.pack(fill="x")
awesome.pack(fill="x")
root.mainloop()
