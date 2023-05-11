"""remove leading and trailing zeros
Task:
Create a function that takes a string input as a number and replaces leading and trailing zeros.

Hint:
re.sub("___(______)______", r"\1", given_string) # r"\1" returns us the group

Input/Output:
"0023.07623070"   -->   "23.0762307"  
"hello world"     -->   "hello world"  
"01230"           -->   "1230"  """

# Solution 1
import re

def remove_leading_trailing_zeros(number_string):
    updated_string = re.sub(r"^0+|0+$", "", number_string)
    return updated_string

# Testing the function
numbers = [
    "0023.07623070",
    "hello world",
    "01230",
    "0.000",
    "0000",
    "0",
]

for number in numbers:
    print(f"{number} --> {remove_leading_trailing_zeros(number)}")

print("_________________________________________________________")

# Solution 2
def remove_leading_trailing_zeros(number_string):
    # Remove leading zeros
    while number_string.startswith('0') and len(number_string) > 1:
        number_string = number_string[1:]

    # Remove trailing zeros
    while number_string.endswith('0') and '.' in number_string:
        number_string = number_string[:-1]

    return number_string

# Testing the function
numbers = [
    "0023.07623070",
    "hello world",
    "01230",
    "0.000",
    "0000",
    "0",
]

for number in numbers:
    print(f"{number} --> {remove_leading_trailing_zeros(number)}")
