import tkinter
from tkinter import Tk,Label
import time
root=tkinter.Tk()
root.title("Digital clock")
def present_time():
    current_time=time.strftime("%I:%M:%S %p")
    digi_clock.config(text=current_time)
    digi_clock.after(200,present_time)
digi_clock=Label(root,font=('calibri',80,'bold'),background='cyan',foreground='black')
digi_clock.pack(anchor='center')
present_time()
root.mainloop()
