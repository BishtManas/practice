def maths ():
    if a % b == 0 :
        print (f"{a} is divisivble by {b}")
    else :
        print (f"{a} is not divisivble by {b}")

print ("welcome to our calculator ! " )
while True :
    a = int (input ("whats the value of first number :  "))
    b = int (input ("what is the value of second number : "))
    maths()
    
    h = input ("you want to continue(c) or not (n)")
    if h == "n":
        print ("thankyou for using aor calculator ")
        break 
    
    