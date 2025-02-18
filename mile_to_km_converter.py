from email.policy import default
from tkinter import *
window=Tk()
window.title("MILE TO KM CONVERTER")
window.minsize(width=500,height=300)
input=Entry()
input.grid(column=2,row=0)
mile_label=Label(text="Miles")
mile_label.grid(column=3,row=0)
is_equal_label=Label(text="is equal to")
is_equal_label.grid(column=1,row=2)
km_result_label=Label(text="0")
km_result_label.grid(column=2,row=2)
km_label=Label(text="Km")
km_label.grid(column=3,row=2)
def calculate():
    user_input=float(input.get())
    mile_to_km=user_input*1.6
    km_result_label.config(text=mile_to_km)
calculate_button=Button(text="Calculate", command=calculate)
calculate_button.grid(column=2,row=3)

window.mainloop()