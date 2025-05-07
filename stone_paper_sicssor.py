def game():
    
    while True:
        your_choice = input("Enter rock (r), paper(p), or scissor(s) : ").lower()
        print(f"you choose {your_choice}\ncomputer choose {computer_choice}")
        if your_choice == computer_choice:
            print ("it's a tie ")
        elif your_choice == "r" and computer_choice == "p":
            print ("you loose")
        elif your_choice == "r" and computer_choice == "s":
            print ("you win")
        elif your_choice == "s" and computer_choice == "p":
            print ("you win")    
        elif your_choice == "s" and computer_choice == "r":
            print ("you loose") 
        elif your_choice == "p" and computer_choice == "r":
            print ("you win") 
        elif your_choice == "p" and computer_choice == "s":
            print ("you loose")
        else :
            print ("invalid input ! please try again .") 
        
def try_again():
    
    while True :
        con = input ("you want to continue(ct) or not (n) : ")
    
        if con == "n":
            print ("thanks for playing with me >>>>")
            quit()
        elif con == "ct ":
            break 
        else :
            print ("invalid error ! ")
        
import random 
choices = ["r" , "p" , "s"]
computer_choice = random.choice(choices)
dic = { "r" : "rock", "p" : "paper", "s" : "sicssor" }

game()
try_again()
                    

