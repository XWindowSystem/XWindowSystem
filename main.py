from tkinter import *
def hello():
  print("Hello World!")
root = Tk()
root.geometry("300x400")
lbl = Label(root, text="Hello", fg="red")
btn = Button(root, text="Click", command=hello)
root.mainloop()
