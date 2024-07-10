import tkinter as tk
import math

calculation = ""

def add_to_calculation(symbol):
    global calculation
    calculation += str(symbol)
    text_result.delete(1.0, "end")
    text_result.insert(1.0, calculation)

def evalute_calculation():
    global calculation
    try:
        calculation = str(eval(calculation))
        text_result.delete(1.0, "end")
        text_result.insert(1.0, calculation)
    except:
        clear_field()
        text_result.insert(1.0, "error")

def clear_field():
    global calculation
    calculation = ""
    text_result.delete(1.0, "end")

def delete_last_character():
    global calculation
    if calculation:
        calculation = calculation[:-1]
        text_result.delete(1.0, "end")
        text_result.insert(1.0, calculation)

root = tk.Tk()
root.geometry("450x620")
root.title("Dark Theme Calculator")

# Dark color scheme
root.configure(bg="#333333")  # Dark gray background

# Function to create buttons with custom styling
def create_button(text, command=None, width=7, height=2, bg="#666666", fg="#ffffff"):
    return tk.Button(root, text=text, command=command, width=width, height=height, bg=bg, fg=fg, font=("Arial", 14))

text_result = tk.Text(root, height=2, width=18, font=("Arial",24), bg="#444444", bd=5, fg="#ffffff")
text_result.grid(columnspan=5, pady=10)

# Buttons with custom colors and styles
btn_1 = create_button("1", lambda: add_to_calculation(1), bg="#555555")
btn_1.grid(row=5, column=1, padx=5, pady=5)
btn_2 = create_button("2", lambda: add_to_calculation(2), bg="#555555")
btn_2.grid(row=5, column=2, padx=5, pady=5)
btn_3 = create_button("3", lambda: add_to_calculation(3), bg="#555555")
btn_3.grid(row=5, column=3, padx=5, pady=5)
btn_4 = create_button("4", lambda: add_to_calculation(4), bg="#555555")
btn_4.grid(row=4, column=1, padx=5, pady=5)
btn_5 = create_button("5", lambda: add_to_calculation(5), bg="#555555")
btn_5.grid(row=4, column=2, padx=5, pady=5)
btn_6 = create_button("6", lambda: add_to_calculation(6), bg="#555555")
btn_6.grid(row=4, column=3, padx=5, pady=5)
btn_7 = create_button("7", lambda: add_to_calculation(7), bg="#555555")
btn_7.grid(row=3, column=1, padx=5, pady=5)
btn_8 = create_button("8", lambda: add_to_calculation(8), bg="#555555")
btn_8.grid(row=3, column=2, padx=5, pady=5)
btn_9 = create_button("9", lambda: add_to_calculation(9), bg="#555555")
btn_9.grid(row=3, column=3, padx=5, pady=5)
btn_0 = create_button("0", lambda: add_to_calculation(0), bg="#555555")
btn_0.grid(row=6, column=2, padx=5, pady=5)
btn_00 = create_button("00", lambda: add_to_calculation("00"), bg="#555555")
btn_00.grid(row=6, column=1, padx=5, pady=5)
btn_plus = create_button("+", lambda: add_to_calculation("+"), bg="#008CBA")
btn_plus.grid(row=3, column=4, padx=5, pady=5)
btn_minus = create_button("-", lambda: add_to_calculation("-"), bg="#008CBA")
btn_minus.grid(row=4, column=4, padx=5, pady=5)
btn_mul = create_button("*", lambda: add_to_calculation("*"), bg="#008CBA")
btn_mul.grid(row=5, column=4, padx=5, pady=5)
btn_div = create_button("/", lambda: add_to_calculation("/"), bg="#008CBA")
btn_div.grid(row=6, column=4, padx=5, pady=5)
btn_open = create_button("(", lambda: add_to_calculation("("), bg="#666666")
btn_open.grid(row=7, column=1, padx=5, pady=5)
btn_close = create_button(")", lambda: add_to_calculation(")"), bg="#666666")
btn_close.grid(row=7, column=2, padx=5, pady=5)
btn_decimal = create_button(".", lambda: add_to_calculation("."), bg="#555555")
btn_decimal.grid(row=6, column=3, padx=5, pady=5)
btn_equals = create_button("=", evalute_calculation, width=15, bg="#4CAF50", fg="#ffffff")  # Green background for "=" button
btn_equals.grid(row=7, column=3, columnspan=2, padx=5, pady=5)
btn_clear = create_button("clear", clear_field, width=15, bg="#F44336", fg="#ffffff")  # Red background for "clear" button
btn_clear.grid(row=2, column=1, columnspan=2, padx=5, pady=5)
btn_delete = create_button("⌫", delete_last_character, width=7, bg="#2196F3", fg="#ffffff")  # Blue background for "⌫" button
btn_delete.grid(row=2, column=3, columnspan=2, padx=5, pady=5)

root.mainloop()
