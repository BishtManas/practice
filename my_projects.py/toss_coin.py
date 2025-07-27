import random
print()

def coin_toss():
    options = ['Heads', 'Tails']
    score = 0
    while True:
        user_guess = input("Guess Heads or Tails (or type 'exit' to quit): ").capitalize()
        
        if user_guess == 'Exit':
            print("Thanks for playing! Goodbye.")
            print(f"Here is your score {score}")
            break
        
        if user_guess not in options:
            print("Invalid input. Please type Heads or Tails.")
            continue

        result = random.choice(options)
        print(f"The coin landed on: {result}")
        
        if user_guess == result:
            print("✅ You guessed it right!\n")
            score += 10 
            print(f"Now, your scored is increased by +10 points\nHere is your score {score}")
        else:
            print("❌ Wrong guess!\n")
            if score == 0 :
                print("if you loose any game then the score is reduced by -5\nBut you have already zero score.")
            else:  
                score -= 5   
                print(f"Now your score is reduced by -5. Here is your final score {score}")       

# Run the game
coin_toss()
