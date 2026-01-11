"""
Created by: Jayshaan Batth
Supplement to: calculator program (python)
Date: 12/31/25
Description: This is the main file that determines user input and conditionals

This is the start of the calcuator program
1. Setup POOP
2. Write Code
3. Test GUI code
4. connect code to gui
"""
# import the Calculator class here
from calculator import Calculator

inputs = []
stop = False

def Calculate(inputs):
    del inputs[len(inputs)-1]
    while len(inputs) > 1:
        if 'x' in inputs:
            index = inputs.index('x')
            temp_num = Calculator.multiply(int(inputs[index-1]), int(inputs[index+1]))
            inputs[index-1] = str(temp_num)
            del inputs[index]
            del inputs[index]

        elif '/' in inputs:
            index = inputs.index('/')
            temp_num = Calculator.divide(int(inputs[index-1]), int(inputs[index+1]))
            inputs[index-1] = str(temp_num)
            del inputs[index]
            del inputs[index]
        elif '+' in inputs:
            index = inputs.index('+')
            temp_num = Calculator.add(int(inputs[index-1]), int(inputs[index+1]))
            inputs[index-1] = str(temp_num)
            del inputs[index]
            del inputs[index]
        elif '-' in inputs:
            index = inputs.index('-')
            temp_num = Calculator.subtract(int(inputs[index-1]), int(inputs[index+1]))
            inputs[index-1] = str(temp_num)
            del inputs[index+1]
            del inputs[index]
    return inputs[0]


import FreeSimpleGUI as sg

display = [
    [sg.Text("0", key="-DISPLAY-", size=(39, 4), justification="right")]
]

buttons = [
    [sg.Button("7", key="-7-", size=(4, 2), pad=(5, 5)), sg.Button("8", key="-8-", size=(4, 2), pad=(5, 5)), sg.Button("9", key="-9-", size=(4, 2), pad=(5, 5))],
    [sg.Button("4", key="-4-", size=(4, 2), pad=(5, 5)), sg.Button("5", key="-5-", size=(4, 2), pad=(5, 5)), sg.Button("6", key="-6-", size=(4, 2), pad=(5, 5))],
    [sg.Button("1", key="-1-", size=(4, 2), pad=(5, 5)), sg.Button("2", key="-2-", size=(4, 2), pad=(5, 5)), sg.Button("3", key="-3-", size=(4, 2), pad=(5, 5))],
    [sg.Button("0", key="-0-", size=(4, 2), pad=(5, 5)), sg.Button("+", key="-+-", size=(4, 2), pad=(5, 5)), sg.Button("-", key="---", size=(4, 2), pad=(5, 5))],
    [sg.Button("x", key="-x-", size=(4, 2), pad=(5, 5)), sg.Button("/", key="-/-", size=(4, 2), pad=(5, 5)), sg.Button("=", key="-=-", size=(4, 2), pad=(5, 5))],
    [sg.Button("AC", key="-AC-", size=(4, 2), pad=(5, 5))]

]

layout = [
    [sg.Frame("Display", display)],
    [sg.Frame("Keypad", buttons)]
]

window = sg.Window("Calculator", layout, margins=(200,300))

while True:
    while '=' not in inputs:
        temp_input = []
        while True:
            event, values = window.read()
            if event == "-0-":
                temp_input.append("0")
                window["-DISPLAY-"].update("".join(temp_input), text_color="white")
            elif event == "-1-":
                temp_input.append("1")
                window["-DISPLAY-"].update("".join(temp_input), text_color="white")
            elif event == "-2-":
                temp_input.append("2")
                window["-DISPLAY-"].update("".join(temp_input), text_color="white")
            elif event == "-3-":
                temp_input.append("3")
                window["-DISPLAY-"].update("".join(temp_input), text_color="white")
            elif event == "-4-":
                temp_input.append("4")
                window["-DISPLAY-"].update("".join(temp_input), text_color="white")
            elif event == "-5-":
                temp_input.append("5")
                window["-DISPLAY-"].update("".join(temp_input), text_color="white")
            elif event == "-6-":
                temp_input.append("6")
                window["-DISPLAY-"].update("".join(temp_input), text_color="white")
            elif event == "-7-":
                temp_input.append("7")
                window["-DISPLAY-"].update("".join(temp_input), text_color="white")
            elif event == "-8-":
                temp_input.append("8")
                window["-DISPLAY-"].update("".join(temp_input), text_color="white")
            elif event == "-9-":
                temp_input.append("9")
                window["-DISPLAY-"].update("".join(temp_input), text_color="white")
            elif event == "-+-":
                inputs.append("".join(temp_input))
                inputs.append("+")
                temp_input.clear()
                break
            elif event == "---":
                inputs.append("".join(temp_input))
                inputs.append("-")
                temp_input.clear()
                break
            elif event == "-x-":
                inputs.append("".join(temp_input))
                inputs.append("x")
                temp_input.clear()
                break
            elif event == "-/-":
                inputs.append("".join(temp_input))
                inputs.append("/")
                temp_input.clear()
                break
            elif event == "-=-":
                inputs.append("".join(temp_input))
                inputs.append("=")
                temp_input.clear()
                break
            elif event == "-AC-":
                temp_input.clear()
                inputs.clear()
                window["-DISPLAY-"].update("0", text_color="white")
            elif event == sg.WIN_CLOSED:
                break # EXIT once
        if event == sg.WIN_CLOSED:
            break # EXIT twice
    if event == sg.WIN_CLOSED:
        break # EXIT thrice
    elif len(inputs) < 4:
        window["-DISPLAY-"].update("Error", text_color="red")
        inputs.clear()
    else:
        #NEED TO FIX ALL BRACKETS
        window["-DISPLAY-"].update(Calculate(inputs), text_color="white")
        inputs.clear()
        

window.close()

