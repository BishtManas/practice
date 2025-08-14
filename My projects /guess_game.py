import random

# This is for guessing a number.
computer_choice0 = random.randint(1,1000)
computer_choice1 = random.randint(1,500)
computer_choice2 = random.randint(1,100)
computer_choice3 = random.randint(1,10)

# This is for a guessing a word.

cartoon_names = [
    "Tom and Jerry",
    "SpongeBob SquarePants",
    "Doraemon",
    "Chhota Bheem",
    "Ben 10",
    "Phineas and Ferb",
    "Oggy and the Cockroaches",
    "Looney Tunes",
    "The Powerpuff Girls",
    "Scooby-Doo"
]
anime_names = [
    "Naruto",
    "One Piece",
    "Attack on Titan",
    "Death Note",
    "Demon Slayer",
    "Dragon Ball Z",
    "Tokyo Ghoul",
    "My Hero Academia",
    "Jujutsu Kaisen",
    "Fullmetal Alchemist"
]
human_names = [
    "Alex",
    "Priya",
    "John",
    "Aarav",
    "Sophia",
    "Rahul",
    "Emily",
    "Karan",
    "Olivia",
    "Rohan"
]
song_names = [
    "Shape of You",
    "Believer",
    "Blinding Lights",
    "Levitating",
    "Perfect",
    "Senorita",
    "Kesariya",
    "Apna Bana Le",
    "Taki Taki",
    "Calm Down"
]
Random_Anime = random.choice(anime_names).lower()
Random_Name = random.choice(human_names).lower()
Random_Song = random.choice(song_names).lower()

class games:
    def __init__(self):
        self.score = 0
    def guess_the_word(self):

        print("Games names in word:--")
        print("Guess cartoon names >> gcn")
        print("Guess anime names >> gan")
        print("Guess humans names >> ghn")
        print("Guess song name >> gsn")

        ask = input("What game you want to play : ")

        def guess_cartoon():
            print("Welcome to guess the cartoon name game ")
            while True:
                Random_Cartoon = random.choice(cartoon_names).lower()
                print("choose a word:")
                print(cartoon_names)
                you = input("choose your word : ").lower().strip()
                if you == Random_Cartoon:
                    print("correct")
                    self.score +=1
                elif you =="":
                    print(f"thank you ! your current score is {self.score}")
                    exit()
                else:
                    print(f"the word is {Random_Cartoon}")
                    print("wrong! try again")
                    print("if you want to end this game just press enter")
        

        def guess_anime():
            print("this is a anime game.")

        def guess_humans():
            print("this is a humans game.")

        def guess_song():
            print("this is a song game")

        if ask == "gcn":
            guess_cartoon()

        elif ask == "gan":
            guess_anime()

        elif ask == "ghn":
            guess_humans()

        elif ask == "gsn":
            guess_song()

        else:
            print("invalid input.")

    def guess_the_number(self):

        def oneto1000(self):
            print("this is a number between 1 to 1000")

        def oneto500(self):
            print("this is a number between  1 to 500")

        def oneto100(self):
            print("this is a number between 1 to 100")

        def oneto10(self):
            print("this is a number between 1 to 10")

        print 
        ask = input ("what game you want to play ")
        # if 
info = games()# create an object for all function so that i use this to everyone.!
while True:

    print("Choice in games:-")
    print("Word guessing game >> wgg")
    print("Number guessing game >> ngg")
    print("What you want to play : ")

    choice = input().lower().strip()

    if choice == "wgg":
        info.guess_the_word()

    elif choice == "ngg":
        info.guess_the_number()

    else:
        print("Invalid input.")
        continue

    while True:

        print("You want to play again :")
        print("Enter to continue")
        print("Space + Enter to exit this game.")

        ask = input()

        if ask == "":
            break

        elif ask == " ":
            print("Thanks for playing")
            exit()

        else:
            print("This is not a valid input try again!")