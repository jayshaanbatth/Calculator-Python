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
