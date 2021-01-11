from tkinter import *
from PIL import ImageTk, Image  # pil/pillow = python image library
from tkinter import messagebox

root = Tk()
root.title("Standard Calculator")
root.iconbitmap("numbers/4/icon.ico")

e = Entry(root, width=30, fg="black", bg="#f1f1f0", borderwidth=0, font=("Arial", 27), justify=RIGHT)
e.insert(0, 0)
e.bind("<Key>", lambda e: "break")
e.grid(row=1, column=0, columnspan=4, padx=20, pady=10, stick="nsew")

e1 = Entry(root, width=30, fg="grey", bg="#f1f1f0", borderwidth=0, font=("Arial", 15), justify=RIGHT)
e1.bind("<Key>", lambda e: "break")
e1.grid(row=0, column=0, columnspan=4, padx=20, pady=10, stick="nsew")

global math
math = ""
global f_num
f_num = 0
global f_num1
f_num1 = 1
global memory
memory = 0
global is_answer
is_answer = False


def button_click(number):
    global is_answer

    if is_answer:
        e.delete(0, END)
        e.insert(0, str(number))
        is_answer = False

    else:
        current = e.get()
        if current == '0':
            e.delete(0, END)
            e.insert(0, str(number))
        else:
            e.insert(END, str(number))


def button_add():
    first_number = e.get()
    global math
    global f_num
    math = "addition"
    f_num = f_num + float(first_number)
    e.delete(0, END)
    if is_answer:
        e1.delete(0, END)
    e1.insert(0, first_number + " + ")


def button_subtract():
    first_number = e.get()
    global math
    global f_num
    math = "subtraction"
    if f_num == 0:
        f_num = float(first_number)
    else:
        f_num -= float(first_number)

    e.delete(0, END)

    if is_answer:
        e1.delete(0, END)
    e1.insert(0, first_number + " - ")


def button_multiply():
    first_number = e.get()
    global math
    global f_num1
    math = "multiplication"
    f_num1 *= float(first_number)
    e.delete(0, END)

    if is_answer:
        e1.delete(0, END)
    e1.insert(0, first_number + " x ")


def button_divide():
    first_number = e.get()
    global math
    global f_num1
    math = "division"

    if f_num1 == 1:
        f_num1 = float(first_number)
    else:
        f_num1 /= float(first_number)

    e.delete(0, END)

    if is_answer:
        e1.delete(0, END)
    e1.insert(0, first_number + " " + chr(247) + " ")


def button_reciprocal():
    first_number = float(e.get())
    if int(first_number) == first_number:
        first_number = int(first_number)
    e.delete(0, END)
    result = first_number ** (-1)
    if int(result) == result:
        e.insert(0, int(result))
    else:
        e.insert(0, result)
    e1.delete(0, END)
    e1.insert(END, "1 " + chr(247) + " " + str(first_number) + " = ")


def button_square():
    first_number = float(e.get())
    if int(first_number) == first_number:
        first_number = int(first_number)
    e.delete(0, END)
    result = first_number ** 2
    if int(result) == result:
        e.insert(0, int(result))
    else:
        e.insert(0, result)
    e1.delete(0, END)
    e1.insert(END, "sqr(" + str(first_number) + ")" + " = ")


def button_square_root():
    first_number = float(e.get())
    if int(first_number) == first_number:
        first_number = int(first_number)
    e.delete(0, END)
    result = first_number ** 0.5
    if int(result) == result:
        e.insert(0, int(result))
    else:
        e.insert(0, result)
    e1.delete(0, END)
    e1.insert(END, "sqrt(" + str(first_number) + ")" + " = ")


def button_modulus():
    first_number = e.get()
    global f_num, math
    f_num = float(first_number)
    e.delete(0, END)
    math = "modulus"
    if is_answer:
        e1.delete(0, END)
    e1.insert(0, first_number + " % ")


def button_plus_minus():
    first_number = float(e.get())
    if first_number != '0':
        e.delete(0, END)
        if int(first_number) == first_number:
            first_number = int(first_number)
        e.insert(0, -first_number)


def button_c():
    if e.get() != '0':
        e.delete(0, END)
        e.insert(0, 0)
    else:
        pass


def button_ac():
    global f_num, f_num1
    f_num = 0
    f_num1 = 1
    if e.get() != '0':
        e.delete(0, END)
        e.insert(0, 0)
        e1.delete(0, END)
    else:
        pass


def button_del():
    first_number = e.get()
    if first_number != '0' and first_number != "cannot divide by zero":
        e.delete(0, END)
        e.insert(0, first_number[:-1])
    else:
        pass
    if e.get() == "":
        e.insert(0, 0)
    if is_answer:
        e1.delete(0, END)


def button_dot():
    first_number = e.get()
    if '.' not in first_number:
        e.delete(0, END)
        e.insert(0, first_number + '.')
    else:
        pass


def button_mc():
    global memory, is_answer
    memory = 0
    is_answer = True


def button_mr():
    e.delete(0, END)
    global memory, is_answer
    if int(memory) == float(memory):
        e.insert(0, int(memory))
    else:
        e.insert(0, float(memory))
    is_answer = True


def button_m_plus():
    first_number = e.get()
    global memory, is_answer
    memory += float(first_number)
    is_answer = True


def button_m_minus():
    first_number = e.get()
    global memory, is_answer
    memory -= float(first_number)
    is_answer = True


def popup():
    response = messagebox.showwarning("Warning!", "cannot divide by zero")


def button_equal():
    global f_num, f_num1, is_answer

    second_number = e.get()
    e.delete(0, END)
    e1.insert(END, second_number + " = ")

    if math == "addition":
        result = f_num + float(second_number)
        if int(result) == result:
            e.insert(END, int(result))
        else:
            e.insert(0, result)
    elif math == "subtraction":
        result = f_num - float(second_number)
        if int(result) == result:
            e.insert(0, int(result))
        else:
            e.insert(0, result)
    elif math == "multiplication":
        result = f_num1 * float(second_number)
        if int(result) == result:
            e.insert(0, int(result))
        else:
            e.insert(0, result)
    elif math == "division":
        if float(second_number) == 0:
            e.delete(0, END)
            e.insert(0, "cannot divide by zero")
            popup()
        else:
            result = f_num1 / float(second_number)
            if int(result) == result:
                e.insert(0, int(result))
            else:
                e.insert(0, result)
    elif math == "modulus":
        if float(second_number) == 0:
            e.delete(0, END)
            e.insert(0, "cannot divide by zero")
            popup()
        else:
            result = f_num % float(second_number)
            if int(result) == result:
                e.insert(0, int(result))
            else:
                e.insert(0, result)
    else:
        e.insert(0, second_number)

    f_num = 0
    f_num1 = 1
    is_answer = True


# create images for buttons:
img_0 = PhotoImage(file="numbers/4/number 0.png").subsample(2, 2)
img_1 = PhotoImage(file="numbers/4/number 1.png").subsample(2, 2)
img_2 = PhotoImage(file="numbers/4/number 2.png").subsample(2, 2)
img_3 = PhotoImage(file="numbers/4/number 3.png").subsample(2, 2)
img_4 = PhotoImage(file="numbers/4/number 4.png").subsample(2, 2)
img_5 = PhotoImage(file="numbers/4/number 5.png").subsample(2, 2)
img_6 = PhotoImage(file="numbers/4/number 6.png").subsample(2, 2)
img_7 = PhotoImage(file="numbers/4/number 7.png").subsample(2, 2)
img_8 = PhotoImage(file="numbers/4/number 8.png").subsample(2, 2)
img_9 = PhotoImage(file="numbers/4/number 9.png").subsample(2, 2)
img_C = PhotoImage(file="numbers/4/C.png").subsample(2, 2)
img_AC = PhotoImage(file="numbers/4/AC.png").subsample(2, 2)
img_dot = PhotoImage(file="numbers/4/dot.png").subsample(2, 2)
img_equal = PhotoImage(file="numbers/4/equal.png").subsample(2, 2)
img_plus = PhotoImage(file="numbers/4/plus.png").subsample(2, 2)
img_minus = PhotoImage(file="numbers/4/minus.png").subsample(2, 2)
img_plus_minus = PhotoImage(file="numbers/4/plus_minus.png").subsample(2, 2)
img_mod = PhotoImage(file="numbers/4/mod.png").subsample(2, 2)
img_divide = PhotoImage(file="numbers/4/divide.png").subsample(2, 2)
img_multiply = PhotoImage(file="numbers/4/multiply.png").subsample(2, 2)
img_del = PhotoImage(file="numbers/4/del.png").subsample(2, 2)
img_square = PhotoImage(file="numbers/4/square.png").subsample(2, 2)
img_square_root = PhotoImage(file="numbers/4/square_root.png").subsample(2, 2)
img_reciprocal = PhotoImage(file="numbers/4/reciprocal.png").subsample(2, 2)
img_mc = PhotoImage(file="numbers/4/mc.png").subsample(2, 2)
img_mr = PhotoImage(file="numbers/4/mr.png").subsample(2, 2)
img_m_plus = PhotoImage(file="numbers/4/m_plus.png").subsample(2, 2)
img_m_minus = PhotoImage(file="numbers/4/m_minus.png").subsample(2, 2)

# define buttons:

button_mc = Button(root, image=img_mc, padx=20, pady=20, bg="black", command=button_mc)
button_mr = Button(root, image=img_mr, padx=20, pady=20, bg="black", command=button_mr)
button_m_plus = Button(root, image=img_m_plus, padx=20, pady=20, bg="black", command=button_m_plus)
button_m_minus = Button(root, image=img_m_minus, padx=20, pady=20, bg="black", command=button_m_minus)

button_modulus = Button(root, image=img_mod, padx=20, pady=20, bg="black", command=button_modulus)
button_c = Button(root, image=img_C, padx=20, pady=20, bg="black", command=button_c)
button_ac = Button(root, image=img_AC, padx=20, pady=20, bg="black", command=button_ac)
button_del = Button(root, image=img_del, padx=20, pady=20, bg="black", command=button_del)

button_reciprocal = Button(root, image=img_reciprocal, padx=20, pady=20, bg="black", command=button_reciprocal)
button_square = Button(root, image=img_square, padx=20, pady=20, bg="black", command=button_square)
button_square_root = Button(root, image=img_square_root, padx=20, bg="black", pady=20, command=button_square_root)
button_divide = Button(root, image=img_divide, padx=20, pady=20, bg="black", command=button_divide)

button_7 = Button(root, image=img_7, padx=20, pady=20, bg="black", command=lambda: button_click(7))
button_8 = Button(root, image=img_8, padx=20, pady=20, bg="black", command=lambda: button_click(8))
button_9 = Button(root, image=img_9, padx=20, pady=20, bg="black", command=lambda: button_click(9))
button_multiply = Button(root, image=img_multiply, padx=20, pady=20, bg="black", command=button_multiply)

button_4 = Button(root, image=img_4, padx=20, pady=20, bg="black", command=lambda: button_click(4))
button_5 = Button(root, image=img_5, padx=20, pady=20, bg="black", command=lambda: button_click(5))
button_6 = Button(root, image=img_6, padx=20, pady=20, bg="black", command=lambda: button_click(6))
button_subtract = Button(root, image=img_minus, padx=20, pady=20, bg="black", command=button_subtract)

button_1 = Button(root, image=img_1, padx=20, pady=20, bg="black", command=lambda: button_click(1))
button_2 = Button(root, image=img_2, padx=20, pady=20, bg="black", command=lambda: button_click(2))
button_3 = Button(root, image=img_3, padx=20, pady=20, bg="black", command=lambda: button_click(3))
button_add = Button(root, image=img_plus, padx=20, pady=20, bg="black", command=button_add)

button_plus_minus = Button(root, image=img_plus_minus, padx=20, pady=20, bg="black", command=button_plus_minus)
button_0 = Button(root, image=img_0, padx=20, pady=20, bg="black", command=lambda: button_click(0))
button_dot = Button(root, image=img_dot, padx=20, pady=20, bg="black", command=button_dot)
button_equal = Button(root, image=img_equal, padx=20, pady=20, bg="black", command=button_equal)

# Configure : so that buttons resize dynamically with change in window size

root.geometry("400x550")

for i in range(8):
    for j in range(4):
        Grid.rowconfigure(root, i, weight=1)
        Grid.columnconfigure(root, j, weight=1)

# put buttons on the screen:

button_plus_minus.grid(row=8, column=0, stick="nsew")
button_0.grid(row=8, column=1, sticky="nsew")
button_dot.grid(row=8, column=2, sticky="nsew")
button_equal.grid(row=8, column=3, sticky="nsew")

button_1.grid(row=7, column=0, sticky="nsew")
button_2.grid(row=7, column=1, sticky="nsew")
button_3.grid(row=7, column=2, sticky="nsew")
button_add.grid(row=7, column=3, sticky="nsew")

button_4.grid(row=6, column=0, sticky="nsew")
button_5.grid(row=6, column=1, sticky="nsew")
button_6.grid(row=6, column=2, sticky="nsew")
button_subtract.grid(row=6, column=3, sticky="nsew")

button_7.grid(row=5, column=0, sticky="nsew")
button_8.grid(row=5, column=1, sticky="nsew")
button_9.grid(row=5, column=2, sticky="nsew")
button_multiply.grid(row=5, column=3, sticky="nsew")

button_ac.grid(row=4, column=0, sticky="nsew")
button_c.grid(row=4, column=1, sticky="nsew")
button_del.grid(row=4, column=2, sticky="nsew")
button_divide.grid(row=4, column=3, sticky="nsew")

button_modulus.grid(row=3, column=0, sticky="nsew")
button_square_root.grid(row=3, column=1, sticky="nsew")
button_square.grid(row=3, column=2, sticky="nsew")
button_reciprocal.grid(row=3, column=3, sticky="nsew")

button_mc.grid(row=2, column=0, sticky="nsew")
button_mr.grid(row=2, column=1, sticky="nsew")
button_m_plus.grid(row=2, column=2, sticky="nsew")
button_m_minus.grid(row=2, column=3, sticky="nsew")

root.mainloop()
