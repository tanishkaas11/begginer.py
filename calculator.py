# tkinter is Python's built-in library to create GUI (Graphical User Interface)
# It helps us create windows, buttons, text boxes like real apps

import tkinter as tk
# ================= CLASS DEFINITION =================

# We are creating a CLASS because:
# - It groups data (buttons, screen)
# - And behavior (what happens when button is clicked)
# This is called Object Oriented Programming (OOP)

class CalculatorApp:

    # ================= CONSTRUCTOR =================
    # __init__ runs automatically when object is created
    # It builds the entire calculator interface

    def __init__(self, root):
        # root is the main window passed from outside
        
        self.root = root

        # Set title of calculator window
        self.root.title("Simple Calculator")
        # Set window size (width x height)
        self.root.geometry("330x370")
        # Prevent window resizing (fixed calculator size)
        self.root.resizable(False, False)


        # ================= SCREEN (DISPLAY) =================

        # Entry widget = single line text box
        # This acts like calculator screen
        self.screen = tk.Entry(
            root,               # parent window
            font=("Arial", 20), # text style and size
            borderwidth=5,      # border thickness
            relief=tk.RIDGE     # border style
        )


        # Place screen on top with padding
        self.screen.grid(row=0, column=0, columnspan=4, padx=10, pady=10)


        # ================= INTERNAL STATE =================

        # This variable stores the full expression like "5+3"
        self.expression = ""



        # ================= BUTTONS =================

        # We create buttons like a calculator keypad

        # Each button calls a function when clicked:
        # - number buttons → add number
        # - operator buttons → add + - * /
        # - equals → calculate result
        # - clear → reset screen


        # Row 1 buttons
        self.create_button("7", 1, 0)
        self.create_button("8", 1, 1)
        self.create_button("9", 1, 2)
        self.create_button("/", 1, 3)


        # Row 2 buttons
        self.create_button("4", 2, 0)
        self.create_button("5", 2, 1)
        self.create_button("6", 2, 2)
        self.create_button("*", 2, 3)

        # Row 3 buttons
        self.create_button("1", 3, 0)
        self.create_button("2", 3, 1)
        self.create_button("3", 3, 2)
        self.create_button("-", 3, 3)

        # Row 4 buttons
        self.create_button("0", 4, 0)
        self.create_button("C", 4, 1)   # Clear button
        self.create_button("=", 4, 2)   # Result button
        self.create_button("+", 4, 3)


    # ================= BUTTON CREATION FUNCTION =================

    # This function creates buttons dynamically
    # So we don't repeat code again and again

    def create_button(self, text, row, col):

        button = tk.Button(

            self.root,            # parent window

            text=text,            # text shown on button

            width=5,              # button width

            height=2,             # button height

            font=("Arial", 14),   # font style

            # command = function called when button is clicked
            # lambda allows passing button text into function
            command=lambda: self.on_button_click(text)
        )

        # Place button in grid layout
        button.grid(row=row, column=col, padx=5, pady=5)


    # ================= BUTTON CLICK HANDLER =================

    def on_button_click(self, char):

        # If user clicks "C"
        if char == "C":
            self.expression = ""              # reset expression
            self.update_screen("")            # clear screen

        # If user clicks "="
        elif char == "=":
            self.calculate_result()           # compute result

        # If number or operator clicked
        else:
            self.expression += str(char)      # add to expression
            self.update_screen(self.expression)


    # ================= CALCULATION FUNCTION =================

    def calculate_result(self):

        try:
            # eval() converts string math into real calculation
            # Example: "5+3" → 8
            result = eval(self.expression)

            # show result on screen
            self.update_screen(result)

            # store result as new expression
            self.expression = str(result)

        except:

            # If invalid input (like 5++3), show error
            self.update_screen("Error")

            self.expression = ""


    # ================= SCREEN UPDATE FUNCTION =================

    def update_screen(self, value):

        # delete everything currently on screen
        self.screen.delete(0, tk.END)

        # insert new value into screen
        self.screen.insert(0, value)



# ================= MAIN PROGRAM =================

# This runs only when file is executed directly

if __name__ == "__main__":

    # Create main window
    root = tk.Tk()

    # Create calculator object (constructor runs here)
    app = CalculatorApp(root)

    # Start GUI loop (keeps window open and listens to clicks)
    root.mainloop()