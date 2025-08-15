import math as m
import os

# ANSI color codes
RED = '\033[31m'
GREEN = '\033[32m'
YELLOW = '\033[33m'
CYAN = '\033[36m'
MAGENTA = '\033[35m'
BLUE = '\033[34m'
RESET = '\033[0m'

# Display basic menu

# Take user input
def mainh():
    print()
    print(f"{CYAN}📘 Basic Information:{RESET}")
    print()

    print(f"{YELLOW}You can perform the following operations:{RESET}\n")# use of reset is just sure to remove the color like you edit a color and you want to add a new color then you must use of 'reset'.
    print(f"{GREEN}1) Square root of a number        ➜ (Type: sqrt){RESET}")
    print(f"{GREEN}2) Trigonometric functions        ➜ (Type: trigo){RESET}")
    print(f"{GREEN}3) Factorial of a number          ➜ (Type: fact!){RESET}")
    print(f"{GREEN}4) Value of π (pi)                ➜ (Type: pi){RESET}")
    print(f"{GREEN}5) Value of e (Euler's Number)    ➜ (Type: expo){RESET}")
    print(f"{GREEN}6) Square of a number             ➜ (Type: sqr){RESET}")
    print()
    user_input_preference = input(f"{MAGENTA}👉 What do you want to do? {RESET}").lower().strip()
    print()

    # Function for square root
    def sqrt():
        user_input = int(input(f"{BLUE}Enter a number: {RESET}"))
        print(f"\n{GREEN}✅ Square root of {user_input} is {m.sqrt(user_input)}{RESET}\n")

    # Function for factorial
    def fact():
        user_input = int(input(f"{BLUE}Enter a number: {RESET}"))
        print(f"\n{GREEN}✅ Factorial of {user_input} is {m.factorial(user_input)}{RESET}\n")

    # Function to display value of pi
    def pi():
        print(f"\n{GREEN}π (pi) = {m.pi}{RESET}\n")

    # Function to display value of e
    def expo():
        print(f"\n{GREEN}Euler's number (e) = {m.e}{RESET}\n")

    # Function to calculate square
    def sqr():
        user_input = int(input(f"{BLUE}Enter a number: {RESET}"))
        print(f"\n{GREEN}✅ Square of {user_input} is {user_input**2}{RESET}\n")

    # Function for basic trigonometric values
    def trigo():
        angle = float(input(f"{BLUE}Enter the angle in degrees: {RESET}"))
        rad = m.radians(angle)
        print()
        print(f"{GREEN}sin({angle}°)  = {round(m.sin(rad), 4)}{RESET}")
        print(f"{GREEN}cos({angle}°)  = {round(m.cos(rad), 4)}{RESET}")
        print(f"{GREEN}tan({angle}°)  = {round(m.tan(rad), 4)}{RESET}")
        print()

    # Decision making
    if user_input_preference == "sqrt":
        sqrt()
    elif user_input_preference == "trigo":
        trigo()
    elif user_input_preference == "fact!":
        fact()
    elif user_input_preference == "pi":
        pi()
    elif user_input_preference == "expo":
        expo()
    elif user_input_preference == "sqr":
        sqr()
    else:
        print(f"{RED}❌ Invalid input! Please try again with a valid option.{RESET}")


if __name__ == "__main__":
    mainh()