def maths(a, b):
    if b == 0:
        print("Can't divide by zero. Please try another number.")
    elif a % b == 0:
        print(f"{a} is divisible by {b}")
    else:
        print(f"{a} is not divisible by {b}")

print("Welcome to our calculator!")

while True:
    try:
        a = int(input("What's the value of the first number: "))
        b = int(input("What's the value of the second number: "))
    except ValueError:
        print("Invalid input! Please enter integers only.")
        continue

    maths(a, b)

    while True:
        h = input("Press 'Enter' to continue or 'n' to exit: ").strip().lower()
        if h == "n":
            print("Thank you for using our calculator :)")
            exit()
        elif h == "":
            break
        else:
            print("Invalid input! Please try again.")
