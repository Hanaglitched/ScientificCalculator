import tkinter as tk

from classes.Calculator import Calculator


class CalculatorGUI:
    """
    GUI of the calculator
    """
    def __init__(self, master):
        """
        Create a new CalculatorGUI object
        :param master: The main window
        """
        self.master = master
        self.display = tk.Entry(self.master, width=25)
        self.display.grid(row=0, column=0, columnspan=4)

        # create buttons
        buttons = [
            "C", "CE", "MC", "MR",
            "7", "8", "9", "/",
            "4", "5", "6", "*",
            "1", "2", "3", "-",
            "0", ".", "pi", "+",
            "sin", "cos", "tan", "log",
            "sqrt", "exp",
            "Ans", "=", "x^y"
        ]
        r = 1
        c = 0
        for button in buttons:
            cmd = lambda x=button: self.button_click(x)
            if button == "0":
                tk.Button(self.master, text=button, width=12, command=cmd).grid(row=r, column=c, columnspan=2)
                c += 2
            else:
                tk.Button(self.master, text=button, width=5, command=cmd).grid(row=r, column=c)
                c += 1
            if c > 3:
                c = 0
                r += 1

        self.calc = Calculator()

    def button_click(self, button):
        """
        Handle button clicks
        :param button: The button that was clicked
        :return:
        """
        if button in ["sin", "cos", "tan", "log", "sqrt", "exp"]:
            self.calc.current_value = float(self.display.get())
            if button == "sin":
                self.calc.operation = "sin"
            elif button == "cos":
                self.calc.operation = "cos"
            elif button == "tan":
                self.calc.operation = "tan"
            elif button == "log":
                self.calc.operation = "log"
            elif button == "sqrt":
                self.calc.operation = "sqrt"
            elif button == "exp":
                self.calc.operation = "exp"
            self.calc.evaluate()
            self.display.delete(0, tk.END)
            self.display.insert(0, self.calc.current_value)
        elif button in ["+", "-", "*", "/", "^"]:
            self.calc.current_value = float(self.display.get())
            self.calc.operation = button
            self.display.delete(0, tk.END)
        elif button == "C":
            self.display.delete(0, tk.END)
            self.calc.clear()
        elif button == "CE":
            self.display.delete(0, tk.END)
        elif button == "MC":
            self.calc.memory = 0
        elif button == "MR":
            self.display.delete(0, tk.END)
            self.display.insert(0, self.calc.memory)
        elif button == "pi":
            self.display.insert(tk.END, "3.14159265359")
        elif button == "x^y":
            self.calc.current_value = float(self.display.get())
            self.calc.operation = "^"
            self.display.delete(0, tk.END)
        elif button == "=":
            self.calc.second_value = float(self.display.get())
            self.calc.evaluate()
            self.display.delete(0, tk.END)
            self.display.insert(0, self.calc.current_value)
        else:
            self.display.insert(tk.END, button)

    def run(self):
        """
        Start the main event loop
        :return:
        """
        self.master.mainloop()
