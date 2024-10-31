from tkinter import *
import math
from sympy import sympify

def button_click(number):
    # For inserting characters
    current = input_space.get()
    input_space.delete(0, END)
    input_space.insert(0, str(current) + str(number))

def clear_btn():
    input_space.delete(0, END)

def del_btn():
    current = input_space.get()
    current = current[:-1]
    input_space.delete(0, END)
    input_space.insert(0, str(current))

def result_btn():
    result = input_space.get()
    if result not in history:
        history.append(result)
    try:
        result_value = sympify(result.replace("π", str(math.pi))).evalf()  # Replace π with pi's value
        input_space.delete(0, END)

        if abs(result_value - int(result_value)) < 1e-9:    # condition checks if result is an integer
            result_value = int(result_value)  # Display as integer
        else:   # Display as float with 3 decimal places
            result_value = f"{result_value:.3f}"

        input_space.insert(0, str(result_value))
    except Exception:
        input_space.delete(0, END)
        input_space.insert(0, "Error")

def previous_btn():
    global i
    if 0 <= i < len(history):
        i = i-1
    else:
        i = len(history)-1
    input_space.delete(0, END)
    input_space.insert(0, str(history[i]))

window = Tk()
window.maxsize(400, 400)
window.title("Simple Calculator")

history, i = [], -1
input_space = Entry(window, width=25, borderwidth=2, font=("Arial", 18), justify=RIGHT)
input_space.grid(row=0, column=0, columnspan=4, padx=5, pady=5)
button_params = {"width": 2, "height": 2, "font": ("Arial", 10)}

# Creating the buttons of the calculator
button_1 = Button(window, text="1", padx=30, pady=15, command=lambda: button_click(1), **button_params)
button_2 = Button(window, text="2", padx=30, pady=15, command=lambda: button_click(2), **button_params)
button_3 = Button(window, text="3", padx=30, pady=15, command=lambda: button_click(3), **button_params)
button_4 = Button(window, text="4", padx=30, pady=15, command=lambda: button_click(4), **button_params)
button_5 = Button(window, text="5", padx=30, pady=15, command=lambda: button_click(5), **button_params)
button_6 = Button(window, text="6", padx=30, pady=15, command=lambda: button_click(6), **button_params)
button_7 = Button(window, text="7", padx=30, pady=15, command=lambda: button_click(7), **button_params)
button_8 = Button(window, text="8", padx=30, pady=15, command=lambda: button_click(8), **button_params)
button_9 = Button(window, text="9", padx=30, pady=15, command=lambda: button_click(9), **button_params)
button_0 = Button(window, text="0", padx=30, pady=15, command=lambda: button_click(0), **button_params)
button_pi = Button(window, text="π", padx=30, pady=15, command=lambda: button_click("π"), **button_params)

button_clear = Button(window, text="clr", padx=30, pady=15, command=clear_btn, **button_params)
button_del = Button(window, text="del", padx=30, pady=15, command=del_btn, **button_params)
button_previous = Button(window, text="↩", padx=30, pady=15, command=previous_btn, **button_params)
button_dot = Button(window, text=".", padx=30, pady=15, command=lambda: button_click("."), **button_params)
button_add = Button(window, text="+", padx=30, pady=15, command=lambda: button_click("+"), **button_params)
button_minus = Button(window, text="-", padx=30, pady=15, command=lambda: button_click("-"), **button_params)
button_mul = Button(window, text="*", padx=30, pady=15, command=lambda: button_click("*"), **button_params)
button_div = Button(window, text="/", padx=30, pady=15, command=lambda: button_click("/"), **button_params)
button_equal = Button(window, text="=", padx=30, pady=15, command=result_btn, **button_params)

# Placing buttons on the screen
button_clear.grid(row=1, column=0)
button_del.grid(row=1, column=1)
button_previous.grid(row=1, column=2)
button_div.grid(row=1, column=3)

button_7.grid(row=2, column=0)
button_8.grid(row=2, column=1)
button_9.grid(row=2, column=2)
button_mul.grid(row=2, column=3)

button_4.grid(row=3, column=0)
button_5.grid(row=3, column=1)
button_6.grid(row=3, column=2)
button_minus.grid(row=3, column=3)

button_1.grid(row=4, column=0)
button_2.grid(row=4, column=1)
button_3.grid(row=4, column=2)
button_add.grid(row=4, column=3)

button_pi.grid(row=5, column=0)
button_0.grid(row=5, column=1)
button_dot.grid(row=5, column=2)
button_equal.grid(row=5, column=3)

window.mainloop()
