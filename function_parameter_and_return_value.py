"""
program: function_parameter_and_return_value.py
author: Angel Castro
date: 3/3/2021
description:
    Function that when called, repeats a string the number of times specified in the parameter.
"""


def multiply_string(favorite_class, repeat_number):
    for i in range(0, repeat_number):
        print('Your favorite class is ', favorite_class)


if __name__ == '__main__':
    try:
        className = input('What is your favorite class?: ')
        number = int(input('How many times should we print your favorite class?'))
    except ValueError:
        print('Value error! Number of times to print must be a number, try again later.')
    else:
        multiply_string(className, number)
