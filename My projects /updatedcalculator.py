import math_module

# Define operations
def addition(a, b):
    print(f"Result : {a} + {b} = {a + b}")

def subtraction(a, b):
    print(f"Result : {a} - {b} = {a - b}")

def multiplication(a, b):
    print(f"Result : {a} x {b} = {a * b}")

def division(a, b):
    if b == 0:
        print("Error: Cannot divide by zero!")
    else:
        print(f"Result : {a} / {b} = {a / b}")

# Dictionary for operations
operations = {
    "+": addition,
    "-": subtraction,
    "*": multiplication,
    "/": division
}

# Calculator function
def simple_calculator():
    try:
        a = float(input('Enter First Number : '))
        b = float(input('Enter Second Number : '))
        user_input = input('Enter Operation (+,-,*,/) : ').strip()
        
        if user_input in operations:
            operations[user_input](a, b)
        else:
            print('Invalid input! Enter a valid operation.')
    except ValueError:
        print("Error: Please enter numeric values only.")

if __name__ == "__main__":
    user_choice = input('calculator / maths : ').lower().strip()
    if user_choice == 'calculator':
        simple_calculator()
    elif user_choice == 'maths':
        math_module.mainh()
