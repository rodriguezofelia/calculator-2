"""CLI application for a prefix-notation calculator."""

from arithmetic import (add, subtract, multiply, divide, square, cube,
                        power, mod, )

def calculate ():
    """ Prints out an answer for the given equation """

    while True:

        input_string = input('Enter your equation > ')
        tokens = input_string.split(' ')

        if input_string == 'q':
            print('You will exit.')
            break
        
        elif tokens[0] == '+':
            print(f'{add(float(tokens[1]), float(tokens[2]))}')

        elif tokens[0] == '-':
            print(f'{subtract(float(tokens[1]), float(tokens[2]))}')

        elif tokens[0] == '*':
            print(f'{multiply(float(tokens[1]), float(tokens[2]))}')
        
        elif tokens[0] == '/':
            print(f'{divide(float(tokens[1]), float(tokens[2]))}')

        elif tokens[0] == 'square':
            print(f'{square(float(tokens[1]))}')
        
        elif tokens[0] == 'cube':
            print(f'{cube(float(tokens[1]))}')
        
        elif tokens[0] == 'pow':
            print(f'{power(float(tokens[1]), float(tokens[2]))}')

        elif tokens[0] == 'mod':
            print(f'{mod(float(tokens[1]), float(tokens[2]))}')
        
calculate()

