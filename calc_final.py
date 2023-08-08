import tkinter as tk
from tkinter import ttk

class CalculatorApp(tk.Tk):
    def __init__(self, title):
        super().__init__()
        self.title(title)
        self.geometry('300x450')
        self.resizable(False, False)
        self.config(bg='#0A0E16')

        ## GRID SETUP
        self.grid_columnconfigure((0,1,2,3), weight=1)
        self.grid_rowconfigure((0,1,2,3,4,5,6), weight=1)

        ## VARIABLES
        self.calc_text = tk.StringVar()
        self.result_text = tk.StringVar()

        self.mind = CalculatorMind()
        self.widgets = self.create_widgets()

        ## STYLE BUTTONS
        self.style = ttk.Style(self)
        self.style.theme_use('clam')
        self.style.configure('num.TButton', font=('Helvetica', 18), background='#161F31', foreground='#FFFFFF', borderwidth=0, width=1)
        self.style.configure('oper.TButton', font=('Helvetica', 15), background='#1992ff', foreground='#0A0E16', borderwidth=0, width=1)
        self.style.configure('del.TButton', font=('Helvetica', 15), background='#2D3545', foreground='#FFFFFF', borderwidth=0, width=1)
        self.style.map('num.TButton',foreground=[('pressed', '#1992ff')], background=[('pressed', '#444B5A')])
        self.style.map('oper.TButton',foreground=[('pressed', '#FFFFFF')], background=[('pressed', '#75BDFF')])
        self.style.map('del.TButton',foreground=[('pressed', '#1992ff')], background=[('pressed', '#81858F')])

    def create_widgets(self):

        ##  BUTTONS LOCATION
        self.button_grid = {0:{"row":6, "column":0},
                1:{'row':3, 'column':0},
                2:{'row':3, 'column':1},
                3:{'row':3, 'column':2},
                4:{'row':4, 'column':0},
                5:{'row':4, 'column':1},
                6:{'row':4, 'column':2},
                7:{'row':5, 'column':0},
                8:{'row':5, 'column':1},
                9:{'row':5, 'column':2},
                'C':{'row':2, 'column':2},
                '<':{'row':2, 'column':3},
                '=':{'row':6, 'column':1},
                '.':{'row':6, 'column':2},
                '/':{'row':3, 'column':3},
                '*':{'row':4, 'column':3},
                '-':{'row':5, 'column':3},
                '+':{'row':6, 'column':3}
                }

        ## NUMBERS BUTTONS
        for num in range(10):
            self.btn_num = ttk.Button(self, text=f'{num}', style='num.TButton')
            self.btn_num.bind('<Button-1>', self.button_press)
            self.btn_num.grid(row=self.button_grid[num]['row'], column=self.button_grid[num]['column'], sticky='nwse', pady=2, padx=2)

        ## OPERATIONS BUTTONS
        for char in ["+", "-", "*", "/", ".", "="]:
            self.btn_char = ttk.Button(self, text=f'{char}', style='oper.TButton')
            self.btn_char.bind('<Button-1>', self.button_press)
            self.btn_char.grid(row=self.button_grid[char]['row'], column=self.button_grid[char]['column'], sticky='nwse', pady=2, padx=2)

        ## C and DELETE BUTTONS
        for char in ["<", "C"]:
            self.btn_char = ttk.Button(self, text=f'{char}', style='del.TButton')
            self.btn_char.bind('<Button-1>', self.button_press)
            self.btn_char.grid(row=self.button_grid[char]['row'], column=self.button_grid[char]['column'], sticky='nwse', pady=2, padx=2)

        ## DISPLAY
        self.display = ttk.Label(self, textvariable=self.result_text, font=('Helvetica', 40), background='#0A0E16', foreground='#FFFFFF', anchor='e', justify='right')
        self.display.grid(row=0, column=0, columnspan=4, sticky='nwe', padx=10, pady=15)

        self.calculation = ttk.Label(self, textvariable=self.calc_text, font=('Helvetica', 15), background='#0A0E16', foreground='#6B758A', anchor='e', justify='right')
        self.calculation.grid(row=1, column=0, columnspan=4, sticky='nwse', padx=15, pady=15)

    def button_press(self, event):  # Action when the button is pressed.
        char = event.widget.cget('text')
        if char == 'C':
            self.mind.clear_display()
            self.calc_text.set(self.mind.calc_string)
            self.result_text.set(self.mind.calc_string)
        elif char == '<':
            self.mind.del_char()
            self.calc_text.set(self.mind.calc_string)
        elif char == '=':
            self.mind.result_calc_string()
            if len(self.mind.calc_string) > 9:
                self.mind.calc_string = self.mind.calc_string[:9]
            elif self.mind.calc_string[-2:] == '.0':
                self.mind.calc_string = self.mind.calc_string[:-2]
            self.result_text.set(self.mind.calc_string)
        else:
            self.mind.add_char(char)
            self.calc_text.set(self.mind.calc_string)

class CalculatorMind:
    """
    Class to create calculation string and calculate result.
    """
    def __init__(self):
        self.calc_string = ''

    def add_char(self, char):
        self.calc_string += str(char)

    def clear_display(self):
        self.calc_string = ''

    def del_char(self):
        self.calc_string = self.calc_string[:-1]

    def result_calc_string(self):
        try:
            result = str(eval(self.calc_string))
        except ZeroDivisionError:
            result = 'Nelze dělit nulou'
        except Exception:
            result = 'Chyba !!!'
        self.calc_string = str(result)

## RUN APP
app = CalculatorApp('Kalkulačka')
app.mainloop()
