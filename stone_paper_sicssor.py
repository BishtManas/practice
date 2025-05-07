import random 
choices = ["r" , "p" , "s"]

dic = { "r" : "rock", "p" : "paper", "s" : "sicssor" }

def game():
    
    while True:
        your_choice = input("Enter rock (r), paper(p), or scissor(s) : ").lower()
        computer_choice = random.choice(choices)
        if your_choice in dic and computer_choice in dic:
            print(f"You choose {dic[your_choice]}\ncomputer choose {dic[computer_choice]}")
        
        
        if your_choice == computer_choice:
            print ("it's a tie ")
            try_again()
        elif (your_choice == "r" and computer_choice == "s") or (your_choice == "s" and computer_choice == "p") or (your_choice == "p" and computer_choice == "r"):
            print ("you win")
            try_again()
            
        elif (your_choice == "r" and computer_choice == "p") or (your_choice == "s" and computer_choice == "r") or (your_choice == "p" and computer_choice == "s") :
            print ("you loose")
            try_again()
        else :
            print ("invalid input ! please try again .") 
        
def try_again():
    while True :
        con = input ("you want to continue(ct) or not (n) : ")
    
        if con == "n":
            print ("thanks for playing with me >>>>")
            quit()
        elif con == "ct":
            game()
            break 
        else :
            print ("invalid error ! ")
        
game()

                    

