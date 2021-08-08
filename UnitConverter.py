from tkinter import *
import tkinter.ttk

def unit_conversion():
    key = combobox.get()
    num = int(entry.get())
    value = unit[key]

    if value == "mm":
        num = num
    elif value == "cm":
        num = num * 10
    elif value == "m":
        num = num * 100
    elif value == "km":
        num = num * 1000

    value1_label.configure(text=(num, "mm"))
    value2_label.configure(text=(num / 10, "cm"))
    value3_label.configure(text=(num / 1000, "m"))
    value4_label.configure(text=(num / 1000000, "km"))

window=tkinter.Tk()
window.title("Unit Converter")
window.geometry("200x230")
window.resizable(False, False)
window.configure(bg = "lemonchiffon")

unit = {"millimeter [mm]":"mm", "centimeter [cm]":"cm", "meter [m]":"m", "kilometer [km]":"km"}

label = Label(window, text="value", bg = "lemonchiffon")
entry = Entry(window, width = 17, justify="right")
combobox = tkinter.ttk.Combobox(window, height=15, values=list(unit.keys()))
combobox.set("Unit selection")
button = Button(window, text = "conversion", command=unit_conversion, bg = "gold")
value1_label = Label(window, text="", bg="khaki", padx=12, pady=5, width=20)
value2_label = Label(window, text="", bg="khaki", padx=12, pady=5, width=20)
value3_label = Label(window, text="", bg="khaki", padx=12, pady=5, width=20)
value4_label = Label(window, text="", bg="khaki", padx=12, pady=5, width=20)

label.place(x=15, y=15)
entry.place(x=55, y=15)
combobox.place(x=15, y=45)
button.place(x=65, y=75)

value1_label.place(x=15, y=120)
value2_label.place(x=15, y=140)
value3_label.place(x=15, y=160)
value4_label.place(x=15, y=180)

window.mainloop()