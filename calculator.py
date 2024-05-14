import tkinter as tk
import math

class Calculator:
    def __init__(self, root):
        self.root = root
        self.root.title("Calculator")
        self.root.configure(bg="pink")

        self.display = tk.Entry(root, width=35, font=("Arial", 14), bd=5, justify="right", relief="sunken", insertbackground="black")
        self.display.grid(row=0, column=0, columnspan=4, padx=15, pady=15, ipady=15)

        buttons = [
            ('1', 1, 0), ('2', 1, 1), ('3', 1, 2), ('C', 1, 3),
            ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('+', 2, 3),
            ('7', 3, 0), ('8', 3, 1), ('9', 3, 2), ('-', 3, 3),
            ('.', 4, 0), ('0', 4, 1), ('=', 4, 2), ('/', 4, 3),
            ('(', 5, 0), (')', 5, 1), ('^', 5, 2), ('*', 5, 3),
            ('Quit', 6, 3)
        ]

        for (text, row, col) in buttons:
            button = tk.Button(root, text=text, font=("Arial", 12), width=5, height=2, command=lambda t=text: self.on_button_click(t))
            button.grid(row=row, column=col, padx=5, pady=5)

    def on_button_click(self, value):
        if value == '=':
            try:
                expression = self.display.get()
                expression = expression.replace('^', '**')
                result = eval(expression)
                self.display.delete(0, tk.END)
                self.display.insert(tk.END, result)
            except Exception as e:
                self.display.delete(0, tk.END)
                self.display.insert(tk.END, "Error")

        elif value == 'C':
            self.display.delete(0, tk.END)

        elif value == 'Quit':
            self.root.destroy()

        else:
            self.display.insert(tk.END, value)

def main():
    root = tk.Tk()
    app = Calculator(root)
    root.mainloop()

if __name__ == "__main__":
    main()
