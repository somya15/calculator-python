# Calculator using tkinter module of python


from tkinter import *
from tkinter import messagebox
import math


class Calculator:
    def number_display(self, x):
        if display_screen.get() == '0':
            display_screen.delete(0, END)
            display_screen.insert(0, str(x))
        else:
            length = len(display_screen.get())
            if length >= 16:
                return
            display_screen.insert(length, str(x))

    def operator_display(self, x):
        all_text = display_screen.get()
        last_char = all_text[-1]
        if last_char in ['+', '-', '/', '*']:
            return
        length = len(display_screen.get())
        if length >= 16:
            return
        display_screen.insert(length, str(x))

    def result_display(self, event=None):
        try:
            result = eval(display_screen.get())
            result = str(round(result, 10))
            index = result.find('.')
            if index == -1:
                index = len(result)
            if index > 14:
                messagebox.showinfo(title="My Calculator", message="Answer out of range")
            else:
                display_screen.delete(0, END)
                display_screen.insert(0, result[:14])
        except:
            messagebox.showinfo(title="My Calculator", message="Invalid expression! Please enter a correct expression!")

    def zero_display(self):
        if display_screen.get() != "0":
            length = len(display_screen.get())
            if length == 16:
                return
            display_screen.insert(length, "0")

    def clear_all(self):
        display_screen.delete(0, END)
        display_screen.insert(0, "0")

    def delete(self):
        length = len(display_screen.get())
        if length > 1:
            display_screen.delete(length - 1, END)
        elif length == 1:
            display_screen.delete(0, END)
            display_screen.insert(0, "0")

    def character_display(self, x):
        length = len(display_screen.get())
        if length == 16:
            return
        display_screen.insert(length, x)

    def sqrt(self):
        try:
            result = eval(display_screen.get())
            result = str(math.sqrt(result))
            display_screen.delete(0, END)
            display_screen.insert(0, result[:14])
        except:
            messagebox.showinfo(title="My Calculator", message="Invalid expression! Please enter a correct expression!")

    def one_by_x(self):
        try:
            result = eval(display_screen.get())
            result = str(1.0 / result)
            display_screen.delete(0, END)
            display_screen.insert(0, result[:14])
        except:
            messagebox.showinfo(title="My Calculator", message="Invalid expression! Please enter a correct expression!")

    def factorial(self):
        try:
            result = eval(display_screen.get())
            if result > 16:
                messagebox.showinfo(title="My Calculator", message="Answer out of range")
            else:
                display_screen.delete(0, END)
                display_screen.insert(0, math.factorial(result))
        except:
            messagebox.showinfo(title="My Calculator", message="Invalid expression! Please enter a correct expression!")

    def absolute(self):
        try:
            result = eval(display_screen.get())
            display_screen.delete(0, END)
            display_screen.insert(0, abs(result))
        except:
            messagebox.showinfo(title="My Calculator", message="Invalid expression! Please enter a correct expression!")

    def square(self):
        try:
            result = eval(display_screen.get())
            if result >= 10000000:
                messagebox.showinfo(title="My Calculator", message="Answer out of range")
            else:
                result = str(result * result)
                display_screen.delete(0, END)
                display_screen.insert(0, result[:14])
        except:
            messagebox.showinfo(title="My Calculator", message="Invalid expression! Please enter a correct expression!")

    def sin(self):
        try:
            result = eval(display_screen.get())
            result = str(math.sin(result))
            display_screen.delete(0, END)
            display_screen.insert(0, result[:14])
        except:
            messagebox.showinfo(title="My Calculator", message="Invalid expression! Please enter a correct expression!")

    def cos(self):
        try:
            result = eval(display_screen.get())
            result = str(math.cos(result))
            display_screen.delete(0, END)
            display_screen.insert(0, result[:14])
        except:
            messagebox.showinfo(title="My Calculator", message="Invalid expression! Please enter a correct expression!")

    def tan(self):
        try:
            x = eval(display_screen.get())
            result = str(math.tan(x))
            index = result.find('.')
            if index == -1:
                index = len(result)
            if index > 14:
                messagebox.showinfo(title="My Calculator", message="Answer out of range")
            else:
                display_screen.delete(0, END)
                display_screen.insert(0, result[:14])
        except:
            messagebox.showinfo(title="My Calculator", message="Invalid expression! Please enter a correct expression!")

    def e_power(self):
        try:
            x = eval(display_screen.get())
            if x > 31:
                messagebox.showinfo(title="My Calculator", message="Answer out of range")
            else:
                result = str(math.pow(math.e, x))
                display_screen.delete(0, END)
                display_screen.insert(0, result[:14])
        except:
            messagebox.showinfo(title="My Calculator", message="Invalid expression! Please enter a correct expression!")

    def sin_inverse(self):
        try:
            result = eval(display_screen.get())
            result = str(math.asin(result))
            display_screen.delete(0, END)
            display_screen.insert(0, result[:14])
        except:
            messagebox.showinfo(title="My Calculator", message="Invalid expression! Please enter a correct expression!")

    def cos_inverse(self):
        try:
            result = eval(display_screen.get())
            result = str(math.acos(result))
            display_screen.delete(0, END)
            display_screen.insert(0, result[:14])
        except:
            messagebox.showinfo(title="My Calculator", message="Invalid expression! Please enter a correct expression!")

    def tan_inverse(self):
        try:
            result = eval(display_screen.get())
            result = str(math.atan(result))
            display_screen.delete(0, END)
            display_screen.insert(0, result[:14])
        except:
            messagebox.showinfo(title="My Calculator", message="Invalid expression! Please enter a correct expression!")

    def log(self):
        try:
            x = eval(display_screen.get())
            result = str(round(math.log10(x), 10))
            display_screen.delete(0, END)
            display_screen.insert(0, result[:14])
        except:
            messagebox.showinfo(title="My Calculator", message="Invalid expression! Please enter a correct expression!")

    def sinh(self):
        try:
            x = eval(display_screen.get())
            result = str(round(math.sinh(x), 10))
            display_screen.delete(0, END)
            display_screen.insert(0, result[:14])
        except:
            messagebox.showinfo(title="My Calculator", message="Invalid expression! Please enter a correct expression!")

    def cosh(self):
        try:
            x = eval(display_screen.get())
            result = str(round(math.cosh(x), 10))
            display_screen.delete(0, END)
            display_screen.insert(0, result[:14])
        except:
            messagebox.showinfo(title="My Calculator", message="Invalid expression! Please enter a correct expression!")

    def tanh(self):
        try:
            x = eval(display_screen.get())
            result = str(round(math.tanh(x), 10))
            display_screen.delete(0, END)
            display_screen.insert(0, result[:14])
        except:
            messagebox.showinfo(title="My Calculator", message="Invalid expression! Please enter a correct expression!")

    def ln(self):
        try:
            x = eval(display_screen.get())
            result = str(round(math.log(x), 10))
            display_screen.delete(0, END)
            display_screen.insert(0, result[:14])
        except:
            messagebox.showinfo(title="My Calculator", message="Invalid expression! Please enter a correct expression!")


# ============================================================== MENU BAR FUNCTIONS

def standard():
    root.geometry("327x431+50+20")


def scientific():
    root.geometry("644x431+50+20")


def exit_option():
    answer = messagebox.askyesno("My Calculator", "Do you want to exit? ")
    if answer > 0:
        root.destroy()


def cut_text():
    try:
        copy_text()
        display_screen.delete("sel.first", "sel.last")
    except:
        pass


def copy_text():
    try:
        display_screen.clipboard_clear()
        display_screen.clipboard_append(display_screen.selection_get())
    except:
        pass


def paste_text():
    try:
        display_screen.insert(INSERT, display_screen.clipboard_get())
    except:
        pass


def view_about():
    about = Tk()
    about.title("About")
    about.geometry("310x300+60+50")
    about.resizable(False, False)
    text1 = Label(about, justify=CENTER,
                  text="  This is a calculator made using\n Tkinter module of python.\nIt has two modes- Standard\nand Scientific which\ncan be changed from\nthe file menu.\n\nMade by: Ankita Sihag",
                  pady=50, font="Helvatica 15")
    text1.grid(sticky="nsew")


# ============================================================== MAIN

root = Tk()
root.title("My Calculator")
root.geometry("327x431+50+20")
root.resizable(False, False)
root.config(background="#b3e6ff")

root_frame = Frame(root)
root_frame.grid()

calculator = Calculator()

# ============================================================== MENU BAR

main_menu = Menu(root_frame)

# -------------------------------------------------------------- FILE MENU
file_menu = Menu(main_menu, tearoff=0)
main_menu.add_cascade(label='File', menu=file_menu)
file_menu.add_command(label="Standard", command=standard)
file_menu.add_command(label="Scientific", command=scientific)
file_menu.add_separator()
file_menu.add_command(label="Exit", command=exit_option)

# -------------------------------------------------------------- EDIT MENU
edit_menu = Menu(main_menu, tearoff=0)
main_menu.add_cascade(label='Edit', menu=edit_menu)
edit_menu.add_command(label="Cut", command=cut_text)
edit_menu.add_command(label="Copy", command=copy_text)
edit_menu.add_separator()
edit_menu.add_command(label="Paste", command=paste_text)

# -------------------------------------------------------------- ABOUT MENU
about_menu = Menu(main_menu, tearoff=0)
main_menu.add_cascade(label="About", menu=about_menu)
about_menu.add_command(label="View about", command=view_about)

root.config(menu=main_menu)

# ============================================================== DISPLAY SCREEN

display_screen = Entry(root_frame, justify=RIGHT, bd=10, width=16, bg="#b3e6ff", font="Calibri 28", relief="ridge")
display_screen.grid(row=0, column=0, columnspan=4, pady=1)
display_screen.insert(0, '0')

# ============================================================== STANDARD VIEW

# -------------------------------------------------------------- ROW 0

btn_clear_all = Button(root_frame, text="C", width=5, height=2, font="Helvatica 16 bold", bd=4, bg="#b3e6ff",
                       activebackground="#cceeff", command=calculator.clear_all)
btn_clear_all.grid(row=1, column=0, pady=1)

btn_delete = Button(root_frame, text="Del", width=5, height=2, font="Helvatica 16 bold", bd=4, bg="#b3e6ff",
                    activebackground="#cceeff", command=calculator.delete)
btn_delete.grid(row=1, column=1, pady=1)

btn_open_bracket = Button(root_frame, text="(", width=5, height=2, font="Helvatica 16 bold", bd=4, bg="#b3e6ff",
                          activebackground="#cceeff", command=lambda x='(': calculator.character_display(x))
btn_open_bracket.grid(row=1, column=2, pady=1)

btn_close_bracket = Button(root_frame, text=")", width=5, height=2, font="Helvatica 16 bold", bd=4, bg="#b3e6ff",
                           activebackground="#cceeff", command=lambda x=')': calculator.character_display(x))
btn_close_bracket.grid(row=1, column=3, pady=1)

# -------------------------------------------------------------- NUMBERS

numbers = "789456123"
i = 0
btn_numbers = []
for j in range(2, 5):
    for k in range(3):
        btn_numbers.append(
            Button(root_frame, text=numbers[i], width=5, height=2, font="Helvatica 16 bold", bd=4, bg="#66ccff",
                   activebackground="#80d4ff"))
        btn_numbers[i].grid(row=j, column=k, pady=1)
        btn_numbers[i]["command"] = lambda x=numbers[i]: calculator.number_display(x)
        i += 1

# -------------------------------------------------------------- ADD, SUBTRACT, MULITPLY

btn_add = Button(root_frame, text="+", width=5, height=2, font="Helvatica 16 bold", bd=4, bg="#b3e6ff",
                 activebackground="#cceeff", command=lambda x='+': calculator.operator_display(x))
btn_add.grid(row=2, column=3, pady=1)

btn_subtract = Button(root_frame, text="-", width=5, height=2, font="Helvatica 16 bold", bd=4, bg="#b3e6ff",
                      activebackground="#cceeff", command=lambda x='-': calculator.operator_display(x))
btn_subtract.grid(row=3, column=3, pady=1)

btn_multiply = Button(root_frame, text="*", width=5, height=2, font="Helvatica 16 bold", bd=4, bg="#b3e6ff",
                      activebackground="#cceeff", command=lambda x='*': calculator.operator_display(x))
btn_multiply.grid(row=4, column=3, pady=1)

# -------------------------------------------------------------- ROW 5

btn_dot = Button(root_frame, text=".", width=5, height=2, font="Helvatica 16 bold", bd=4, bg="#b3e6ff",
                 activebackground="#cceeff", command=lambda x='.': calculator.character_display(x))
btn_dot.grid(row=5, column=0, pady=1)

btn_zero = Button(root_frame, text="0", width=5, height=2, font="Helvatica 16 bold", bd=4, bg="#66ccff",
                  activebackground="#80d4ff", command=calculator.zero_display)
btn_zero.grid(row=5, column=1, pady=1)

btn_equals = Button(root_frame, text="=", width=5, height=2, font="Helvatica 16 bold", bd=4, bg="#4dff88",
                    activebackground="#ccffcc", command=calculator.result_display)
btn_equals.grid(row=5, column=2, pady=1)
root.bind('<Return>', calculator.result_display)

btn_divide = Button(root_frame, text="/", width=5, height=2, font="Helvatica 16 bold", bd=4, bg="#b3e6ff",
                    activebackground="#cceeff", command=lambda x='/': calculator.operator_display(x))
btn_divide.grid(row=5, column=3, pady=1)


# ============================================================== SCIENTIFIC VIEW

# -------------------------------------------------------------- LABEL

scientific_label = Label(root_frame, text="Scientific Calculator", font="Calibri 20 bold", justify=CENTER, bg="#b3e6ff",
                         borderwidth=10, relief="ridge")
scientific_label.grid(row=0, column=4, columnspan=4, sticky="news")

# -------------------------------------------------------------- ROW 1

btn_sqrt = Button(root_frame, text="√", width=5, height=2, font="Helvatica 16 bold", bd=4, bg="#b3e6ff",
                  activebackground="#cceeff", command=calculator.sqrt)
btn_sqrt.grid(row=1, column=4, pady=1)

btn_1byx = Button(root_frame, text="1/x", width=5, height=2, font="Helvatica 16 bold", bd=4, bg="#b3e6ff",
                  activebackground="#cceeff", command=calculator.one_by_x)
btn_1byx.grid(row=1, column=5, pady=1)

btn_fact = Button(root_frame, text="x!", width=5, height=2, font="Helvatica 16 bold", bd=4, bg="#b3e6ff",
                  activebackground="#cceeff", command=calculator.factorial)
btn_fact.grid(row=1, column=6, pady=1)

btn_pi = Button(root_frame, text="π", width=5, height=2, font="Helvatica 16 bold", bd=4, bg="#b3e6ff",
                activebackground="#cceeff", command=lambda x=round(math.pi, 10): calculator.number_display(x))
btn_pi.grid(row=1, column=7, pady=1)

# -------------------------------------------------------------- ROW 2

btn_square = Button(root_frame, text="x\u00B2", width=5, height=2, font="Helvatica 16 bold", bd=4, bg="#b3e6ff",
                    activebackground="#cceeff", command=calculator.square)
btn_square.grid(row=2, column=4, pady=1)

btn_power = Button(root_frame, text="x\u207F", width=5, height=2, font="Helvatica 16 bold", bd=4, bg="#b3e6ff",
                   activebackground="#cceeff", command=lambda x='**': calculator.operator_display(x))
btn_power.grid(row=2, column=5, pady=1)

btn_abs = Button(root_frame, text="|x|", width=5, height=2, font="Helvatica 16 bold", bd=4, bg="#b3e6ff",
                 activebackground="#cceeff", command=calculator.absolute)
btn_abs.grid(row=2, column=6, pady=1)

btn_e = Button(root_frame, text="e", width=5, height=2, font="Helvatica 16 bold", bd=4, bg="#b3e6ff",
               activebackground="#cceeff", command=lambda x=round(math.e, 10): calculator.number_display(x))
btn_e.grid(row=2, column=7, pady=1)

# -------------------------------------------------------------- ROW 3

btn_sin = Button(root_frame, text="sin", width=5, height=2, font="Helvatica 16 bold", bd=4, bg="#b3e6ff",
                 activebackground="#cceeff", command=calculator.sin)
btn_sin.grid(row=3, column=4, pady=1)

btn_cos = Button(root_frame, text="cos", width=5, height=2, font="Helvatica 16 bold", bd=4, bg="#b3e6ff",
                 activebackground="#cceeff", command=calculator.cos)
btn_cos.grid(row=3, column=5, pady=1)

btn_tan = Button(root_frame, text="tan", width=5, height=2, font="Helvatica 16 bold", bd=4, bg="#b3e6ff",
                 activebackground="#cceeff", command=calculator.tan)
btn_tan.grid(row=3, column=6, pady=1)

btn_e_power = Button(root_frame, text="e\u207F", width=5, height=2, font="Helvatica 16 bold", bd=4, bg="#b3e6ff",
                     activebackground="#cceeff", command=calculator.e_power)
btn_e_power.grid(row=3, column=7, pady=1)

# -------------------------------------------------------------- ROW 4

btn_sin_inverse = Button(root_frame, text="sin\u207B\u00B9", width=5, height=2, font="Helvatica 16 bold", bd=4,
                         bg="#b3e6ff", activebackground="#cceeff", command=calculator.sin_inverse)
btn_sin_inverse.grid(row=4, column=4, pady=1)

btn_cos_inverse = Button(root_frame, text="cos\u207B\u00B9", width=5, height=2, font="Helvatica 16 bold", bd=4,
                         bg="#b3e6ff", activebackground="#cceeff", command=calculator.cos_inverse)
btn_cos_inverse.grid(row=4, column=5, pady=1)

btn_tan_inverse = Button(root_frame, text="tan\u207B\u00B9", width=5, height=2, font="Helvatica 16 bold", bd=4,
                         bg="#b3e6ff", activebackground="#cceeff", command=calculator.tan_inverse)
btn_tan_inverse.grid(row=4, column=6, pady=1)

btn_log = Button(root_frame, text="log", width=5, height=2, font="Helvatica 16 bold", bd=4, bg="#b3e6ff",
                 activebackground="#cceeff", command=calculator.log)
btn_log.grid(row=4, column=7, pady=1)

# -------------------------------------------------------------- ROW 5

btn_sinh = Button(root_frame, text="sinh", width=5, height=2, font="Helvatica 16 bold", bd=4, bg="#b3e6ff",
                  activebackground="#cceeff", command=calculator.sinh)
btn_sinh.grid(row=5, column=4, pady=1)

btn_cosh = Button(root_frame, text="cosh", width=5, height=2, font="Helvatica 16 bold", bd=4, bg="#b3e6ff",
                  activebackground="#cceeff", command=calculator.cosh)
btn_cosh.grid(row=5, column=5, pady=1)

btn_tanh = Button(root_frame, text="tanh", width=5, height=2, font="Helvatica 16 bold", bd=4, bg="#b3e6ff",
                  activebackground="#cceeff", command=calculator.tanh)
btn_tanh.grid(row=5, column=6, pady=1)

btn_ln = Button(root_frame, text="ln", width=5, height=2, font="Helvatica 16 bold", bd=4, bg="#b3e6ff",
                activebackground="#cceeff", command=calculator.ln)
btn_ln.grid(row=5, column=7, pady=1)

root.mainloop()
