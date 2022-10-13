#Práctica 01 Almacenes de Datos
#Nahuatlato Neri Néstor Leonel
#from tkinter import ttk
from tkinter import ttk
import tkinter

#Auliary constants
WINDOW_NAME = "Calculator"
ROOT_DISPLAY_STATE = "readonly"

CLEAR_OPERATOR = "C"
ERASE_OPERATOR = "←"
ADD_OPERATOR = "+"
SUBTRACT_OPERATOR = "-"
MULTIPLICATION_OPERATOR = "×"
DIVISION_OPERATOR = "÷"
DOT = "."
RESULT_OPERATOR = "="
C_0 = "0"
C_1 = "1"
C_2 = "2"
C_3 = "3"
C_4 = "4"
C_5 = "5"
C_6 = "6"
C_7 = "7"
C_8 = "8"
C_9 = "9"

WIDTH_SIZE = 320
HEIGHT_SIZE = 150
COLUMN_1_POSITION = 0
COLUMN_2_POSITION = 80
COLUMN_3_POSITION = 160
COLUMN_4_POSITION = 240
ROW_1_POSITION = 30
ROW_2_POSITION = 60
ROW_3_POSITION = 90
ROW_4_POSITION = 120

EMPTY_STRING = ""
C2_0 = 0
C2_1 = 1
C__1 = -1

#Variables to use
accum = C2_0
flag = False
operator_to_use = EMPTY_STRING

def is_dot_last_char(string):
    aux_string = string.get()
    if aux_string.endswith(DOT):
        erase_last(string)
    
    return string

def add(number, string):
    global flag

    if flag:
        string.set(EMPTY_STRING)
        flag = False

    aux_string = string.get() + number
    result = aux_string.count(DOT) == C2_1

    if aux_string.isdecimal() or result:
        string.set(aux_string)

def erase_last(string):
    aux_string = string.get()
    aux_string_size = len(aux_string)

    if aux_string_size > C2_0:
        string.set(aux_string[:C__1])

def clear(string):
    string.set(EMPTY_STRING)

    global accum, flag, operator_to_use
    accum = C2_0
    flag = False
    operator_to_use = EMPTY_STRING


def operation(operator_received, string):
    global accum, operator_to_use

    if accum == C2_0:
        aux_string = is_dot_last_char(string)
        accum = float(aux_string.get())

    operator_to_use = operator_received

    string.set(EMPTY_STRING)

def show_result(string):
    global accum, flag

    if operator_to_use != EMPTY_STRING:
        aux_string = is_dot_last_char(string)
        value = float(aux_string.get())

        if operator_to_use == ADD_OPERATOR:
            result = accum + value
        elif operator_to_use == SUBTRACT_OPERATOR:
            result = accum - value
        elif operator_to_use == MULTIPLICATION_OPERATOR:
            result = accum * value
        elif operator_to_use == DIVISION_OPERATOR:
            result = accum / value

        string.set(result)
        flag = True
        accum = C2_0
    else:
        clear(string)

def main():
    #window setting
    root = tkinter.Tk()
    root.config(width=WIDTH_SIZE, height=HEIGHT_SIZE)
    root.title(WINDOW_NAME)
    root.resizable(C2_0, C2_0)

    #Display setting
    string = tkinter.StringVar()
    string.set(EMPTY_STRING)
    display = ttk.Entry(textvariable=string, state=ROOT_DISPLAY_STATE)
    display.place(x=C2_0, y=C2_0)

    #Numbers buttons settins
    button_7 = ttk.Button(root, text=C_7, command=lambda:add(C_7, string))
    button_7.place(x=COLUMN_1_POSITION, y=ROW_1_POSITION)

    button_4 = ttk.Button(root, text=C_4, command=lambda:add(C_4, string))
    button_4.place(x=COLUMN_1_POSITION, y=ROW_2_POSITION)

    button_1 = ttk.Button(root, text=C_1, command=lambda:add(C_1, string))
    button_1.place(x=COLUMN_1_POSITION, y=ROW_3_POSITION)

    button_0 = ttk.Button(root, text=C_0, command=lambda:add(C_0, string))
    button_0.place(x=COLUMN_1_POSITION, y=ROW_4_POSITION)

    button_8 = ttk.Button(root, text=C_8, command=lambda:add(C_8, string))
    button_8.place(x=COLUMN_2_POSITION, y=ROW_1_POSITION)

    button_5 = ttk.Button(root, text=C_5, command=lambda:add(C_5, string))
    button_5.place(x=COLUMN_2_POSITION, y=ROW_2_POSITION)

    button_2 = ttk.Button(root, text=C_2, command=lambda:add(C_2, string))
    button_2.place(x=COLUMN_2_POSITION, y=ROW_3_POSITION)

    button_dot = ttk.Button(root, text=DOT, command=lambda:add(DOT, string))
    button_dot.place(x=COLUMN_2_POSITION, y=ROW_4_POSITION)

    button_9 = ttk.Button(root, text=C_9, command=lambda:add(C_9, string))
    button_9.place(x=COLUMN_3_POSITION, y=ROW_1_POSITION)

    button_6 = ttk.Button(root, text=C_6, command=lambda:add(C_6, string))
    button_6.place(x=COLUMN_3_POSITION, y=ROW_2_POSITION)

    button_3 = ttk.Button(root, text=C_3, command=lambda:add(C_3, string))
    button_3.place(x=COLUMN_3_POSITION, y=ROW_3_POSITION)

    button_result = ttk.Button(root, text=RESULT_OPERATOR, command=lambda:show_result(string))
    button_result.place(x=COLUMN_3_POSITION, y=ROW_4_POSITION)

    #operator buttons settins
    add_button = ttk.Button(root, text=ADD_OPERATOR, command=lambda:operation(ADD_OPERATOR, string))
    add_button.place(x=COLUMN_4_POSITION, y=ROW_1_POSITION)

    subtract_button = ttk.Button(root, text=SUBTRACT_OPERATOR, command=lambda:operation(SUBTRACT_OPERATOR, string))
    subtract_button.place(x=COLUMN_4_POSITION, y=ROW_2_POSITION)

    multiplication_button = ttk.Button(root, text=MULTIPLICATION_OPERATOR, command=lambda:operation(MULTIPLICATION_OPERATOR, string))
    multiplication_button.place(x=COLUMN_4_POSITION, y=ROW_3_POSITION)

    division_button = ttk.Button(root, text=DIVISION_OPERATOR, command=lambda:operation(DIVISION_OPERATOR, string))
    division_button.place(x=COLUMN_4_POSITION, y=ROW_4_POSITION)

    clean_button = ttk.Button(root, text=CLEAR_OPERATOR, command=lambda:clear(string))
    clean_button.place(x=COLUMN_3_POSITION, y=C2_0)

    erase_button = ttk.Button(root, text=ERASE_OPERATOR, command=lambda:erase_last(string))
    erase_button.place(x=COLUMN_4_POSITION, y=C2_0)

    root.mainloop()

if __name__ == "__main__":
    main()