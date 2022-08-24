
from tkinter import *


window=Tk()
# btn=Button(window, text="This is Button widget", fg='blue')
# btn.place(x=80, y=100)
# window.title('Hello Python')
# window.geometry("300x200+10+10")
# window.mainloop()




temp = StringVar()

lbl=Label(window, text="This is Label widget")
lbl.place(x=60, y=50)

def cel_to_f():
    t = float(temp.get())
    t = t*9/5 + 32
    lbl.configure(text=str(t))

# window=Tk()
btn=Button(window, text="This is Button widget", command = cel_to_f)
btn.place(x=80, y=100)
txtfld=Entry(window, text="This is Entry Widget", bd=5, textvariable=temp)
txtfld.place(x=80, y=150)
window.title('Hello Python')
window.geometry("300x200+10+10")
window.mainloop()

# window=Tk()
# lbl=Label(window, text="This is Label widget", fg='red', font=("Helvetica", 16))
# lbl.place(x=60, y=50)
# window.title('Hello Python')
# window.geometry("300x200+10+10")
# window.mainloop()