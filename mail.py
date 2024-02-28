from tkinter import *

def miles_to_km():
    miles = float(miles_input.get())
    km = round(miles*1.609)
    Kilometer_result_label.config(text=f"{km}")


window = Tk()
window.title("Miles to Kilometer")
# window.minsize(width=500,height=300)
window.config(padx=20,pady=20)

#Entry
miles_input = Entry(width=10)
miles_input.grid(column=1, row=0)



# label1
miles_label = Label(text="Miles")
miles_label.grid(column=2,row = 0)

#label2 
is_equl_label = Label(text="is equals to ")
is_equl_label.grid(column=0,row = 1)

# Label3
Kilometer_result_label = Label(text="0")
Kilometer_result_label.grid(column=1,row = 1)
# lable4
Kilometer_label = Label(text="Km")
Kilometer_label.grid(column=2,row = 1)

#button
Calculate_button = Button(text="Calculate",command=miles_to_km)
Calculate_button.grid(column=1,row=2)


window.mainloop()



