from tkinter import *

root = Tk()
root.title("Basic Calculator")
root.iconphoto(True, PhotoImage(file="/home/soumyo/PycharmProjects/Basic Calculator/icon.png"))


# Creating Functions
def btn_click(number):
    # entrybox.delete(0, END)  # Deleting before inserting a value
    current = entrybox.get()
    entrybox.delete(0, END)
    entrybox.insert(0, str(current) + str(number))  # Inserting the number


def btn_clear():
    entrybox.delete(0, END)  # Deleting values inside EntryBox


def btn_add():
    first_number = entrybox.get()
    global f_num
    global math
    math = "addition"
    f_num = int(first_number)
    entrybox.delete(0, END)


def btn_sub():
    first_number = entrybox.get()
    global f_num
    global math
    math = "subtraction"
    f_num = int(first_number)
    entrybox.delete(0, END)


def btn_mul():
    first_number = entrybox.get()
    global f_num
    global math
    math = "multiplication"
    f_num = int(first_number)
    entrybox.delete(0, END)


def btn_div():
    first_number = entrybox.get()
    global f_num
    global math
    math = "division"
    f_num = int(first_number)
    entrybox.delete(0, END)


def btn_eql():
    if math == "addition":
        second_number = entrybox.get()
        entrybox.delete(0, END)
        entrybox.insert(0, f_num + int(second_number))

    elif math == "subtraction":
         second_number = entrybox.get()
         entrybox.delete(0, END)
         entrybox.insert(0, f_num - int(second_number))

    elif math == "multiplication":
         second_number = entrybox.get()
         entrybox.delete(0, END)
         entrybox.insert(0, f_num * int(second_number))

    elif math == "division":
         second_number = entrybox.get()
         entrybox.delete(0, END)

         if int(second_number) == 0:
             entrybox.insert(0, "Invalid")

         else:
             entrybox.insert(0, f_num / int(second_number))


# Creating an EntryBox
entrybox = Entry(root, width=14, borderwidth=5, justify=RIGHT, font=("Arial", 25))
entrybox.grid(row=0, column=0, columnspan=3, padx=5, pady=5)

# Creating Buttons

# Number Buttons
# Creating Buttons
btn_1 = Button(root, text="1", padx=40, pady=20, command=lambda: btn_click(1))
btn_2 = Button(root, text="2", padx=40, pady=20, command=lambda: btn_click(2))
btn_3 = Button(root, text="3", padx=40, pady=20, command=lambda: btn_click(3))
btn_4 = Button(root, text="4", padx=40, pady=20, command=lambda: btn_click(4))
btn_5 = Button(root, text="5", padx=40, pady=20, command=lambda: btn_click(5))
btn_6 = Button(root, text="6", padx=40, pady=20, command=lambda: btn_click(6))
btn_7 = Button(root, text="7", padx=40, pady=20, command=lambda: btn_click(7))
btn_8 = Button(root, text="8", padx=40, pady=20, command=lambda: btn_click(8))
btn_9 = Button(root, text="9", padx=40, pady=20, command=lambda: btn_click(9))
btn_0 = Button(root, text="0", padx=40, pady=20, command=lambda: btn_click(0))
# Putting buttons on root window
btn_1.grid(row=3, column=0)
btn_2.grid(row=3, column=1)
btn_3.grid(row=3, column=2)

btn_4.grid(row=2, column=0)
btn_5.grid(row=2, column=1)
btn_6.grid(row=2, column=2)

btn_7.grid(row=1, column=0)
btn_8.grid(row=1, column=1)
btn_9.grid(row=1, column=2)

btn_0.grid(row=4, column=0)

# Operator Buttons
# Creating Buttons
add_btn = Button(root, text="+", padx=39, pady=20, command=btn_add)
subtract_btn = Button(root, text="-", padx=41, pady=20, command=btn_sub)
multiply_btn = Button(root, text="*", padx=40, pady=20, command=btn_mul)
division_btn = Button(root, text="/", padx=41, pady=20, command=btn_div)

eql_btn = Button(root, text="=", padx=90, pady=20, command=btn_eql)
clr_btn = Button(root, text="Clear", padx=79, pady=20, command=btn_clear)

# Putting Buttons on Screen
add_btn.grid(row=5, column=0)
subtract_btn.grid(row=6, column=0)
multiply_btn.grid(row=6, column=1)
division_btn.grid(row=6, column=2)
eql_btn.grid(row=5, column=1, columnspan=2)
clr_btn.grid(row=4, column=1, columnspan=2)







root.mainloop()