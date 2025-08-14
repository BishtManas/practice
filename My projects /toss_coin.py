import random
import os
from colorama import Fore, Style, init

# Initialize colorama (Windows needs this)
init(autoreset=True)

def coin_toss():
    options = ['Heads', 'Tails']
    score = 0

    while True:
        os.system('cls' if os.name == 'nt' else 'clear')  # Clears the terminal screen

        print(Fore.CYAN + Style.BRIGHT + "🎲 Welcome to Coin Toss Game! 🎯")
        print(Fore.YELLOW + f"Current Score: {score}\n")

        user_guess = input(Fore.MAGENTA + "Guess Heads or Tails (or type 'exit' to quit): ").capitalize()
        
        if user_guess == 'Exit':
            print(Fore.CYAN + "Thanks for playing! Goodbye.")
            print(Fore.GREEN + f"🏁 Final Score: {score}")
            break
        
        if user_guess not in options:
            print(Fore.RED + "❌ Invalid input. Please type Heads or Tails.")
            input("Press Enter to continue...")
            continue

        result = random.choice(options)
        print(Fore.BLUE + f"The coin landed on: {result}")

        if user_guess == result:
            print(Fore.GREEN + "✅ You guessed it right!")
            score += 10 
            print(Fore.GREEN + f"+10 points! 🎉 New Score: {score}")
        else:
            print(Fore.RED + "❌ Wrong guess!")
            if score == 0:
                print(Fore.RED + "You have 0 score, can't subtract points.")
            else:  
                score -= 5   
                print(Fore.RED + f"-5 points. 😢 New Score: {score}")
        
        input(Fore.YELLOW + "\nPress Enter to toss again...")

# Run the game
coin_toss()# add some features like input the player name and ask from user he/she wants to play alone or multiplayer and give a chance to put the user_name for that.
