def addition(a , b ):
    
    print (f"here is your answer {a} + {b} = {a + b}")
    
def multiplication (a , b ):
   
    print (f"here is your answer {a} x {b} = {a * b}")
    
def division (a , b ):
    if a == 0 or b ==0 :
        print ("not divisible by 0")
    else :
        print (f"here is your answer {a} / {b} = {a / b}")
    
def subtraction (a , b ):
    
    print (f"here is your answer {a} - {b} = {a - b}")

while True:
    
    a = int (input ("what is your first number : "))
    b = int (input ("what is your second number : "))
    s = input ("what you want to do (* ,/ ,- ,+) : ")
    
    if s == "+":
        addition(a , b )
    elif s == "*":
        multiplication (a , b )
    elif s == "/":
        division (a , b )
    elif s == "-":
        subtraction (a , b )
    else :
        print ("Invalid input ! please try again .")
        
    want = input ("you want to continue (c) or not(n) : ")
    while True:
        want = input("Do you want to continue? (c) or not (n): ")
        if want == "n":
            print("Thank you for using us!")
            exit()
        elif want == "c":
            break   # break this small loop and go back to the main loop
        else:
            print("Invalid input! Please enter only 'c' or 'n'.")
