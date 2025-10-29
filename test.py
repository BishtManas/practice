import random

print("🎯 Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")
print("Can you guess it?")

# Random number between 1 to 100
secret_number = random.randint(1, 100)
attempts = 0

while True:
    try:
        guess = int(input("👉 Enter your guess: "))
        attempts += 1

        if guess < 1 or guess > 100:
            print("⚠️ Please guess a number between 1 and 100.")
            continue

        if guess < secret_number:
            print("Too low! Try again ⬆️")
        elif guess > secret_number:
            print("Too high! Try again ⬇️")
        else:
            print(f"🎉 Correct! The number was {secret_number}.")
            print(f"You guessed it in {attempts} attempts!")
            break
    except ValueError:
        print("❌ Invalid input! Please enter a number.")
