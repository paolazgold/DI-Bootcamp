"""Here is a python code that generates a list of 20000 random numbers, called list_of_numbers, and a target number.

import random

list_of_numbers = [random.randint(0, 10000) for _ in range(20000)]

target_number   = 3728


Copy this code, and create a program that finds, within list_of_numbers all the pairs of number that sum to the target number

"""
import random

list_of_numbers = [random.randint(0, 10000) for _ in range(20000)]
target_number   = 3728

for x in range(len(list_of_numbers)):
    for y in range(x + 1, len(list_of_numbers)):
        if list_of_numbers[x] + list_of_numbers[y] == target_number:
            print(list_of_numbers[x], "+", list_of_numbers[y], "=", target_number)
