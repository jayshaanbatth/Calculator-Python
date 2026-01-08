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

while stop != True:
    while '=' not in inputs and stop == False:
        inputs.append(input('Please enter a number or a operator symbol: '))
        if 'stop' in inputs:
            stop = True
    if stop == True:
        print("Have a great day!")
    elif len(inputs) < 4:
        print('That is not a full equation, try again!')
        inputs.clear()
    else:
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

        print(inputs[0])
        inputs.clear()

import FreeSimpleGUI as sg

display = [
    [sg.Text("0", key="-DISPLAY-", size=(39, 4), justification="right")]
]

buttons = [
    [sg.Button("7", key="-7-", size=(4, 2), pad=(5, 5)), sg.Button("8", key="-8-", size=(4, 2), pad=(5, 5)), sg.Button("9", key="-9-", size=(4, 2), pad=(5, 5))],
    [sg.Button("4", key="-4-", size=(4, 2), pad=(5, 5)), sg.Button("5", key="-5-", size=(4, 2), pad=(5, 5)), sg.Button("6", key="-6-", size=(4, 2), pad=(5, 5))],
    [sg.Button("1", key="-1-", size=(4, 2), pad=(5, 5)), sg.Button("2", key="-2-", size=(4, 2), pad=(5, 5)), sg.Button("3", key="-3-", size=(4, 2), pad=(5, 5))],
    [sg.Button("0", key="-0-", size=(4, 2), pad=(5, 5)), sg.Button("AC", key="-AC-", size=(4, 2), pad=(5, 5)), sg.Button("=", key="-=-", size=(4, 2), pad=(5, 5))]
]

layout = [
    [sg.Frame("Display", display)],
    [sg.Frame("Keypad", buttons)]
]

window = sg.Window("Test Window", layout, margins=(200,300))

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == "OK":
        break

window.close()

