import tkinter as tk
from classes.Calculator import Calculator
from classes.CalculatorGUI import CalculatorGUI


def main():
    """
    Main function
    :return:
    """
    # Create the calculator object
    calc = Calculator()

    # Create the main window and GUI objects
    root = tk.Tk()
    root.title("Scientific Calculator")
    root.resizable(False, False)
    gui = CalculatorGUI(root)

    # Start the main event loop
    root.mainloop()


if __name__ == "__main__":
    main()
