import random
print("Welcome to the Number Guessing Game")
print("I am thinking of a number between 1 and 100.")
difficulty= input("Choose a difficulty. Type 'easy' or 'hard': ")
answer=random.randint(1,101)
print(answer)


def easy():
    print("You have 10 attempts remaining to guess the number")
    game=True
    i=9
    while game is True and i>=0:
        guess=int(input("Make a guess: "))
        if guess==answer:
            game=False
            return print(f"You got it the answer is {answer}")
            
        elif guess<answer:
            print("Too low")
            print(f"You have {i} attemps remaining")
        else:
            print("Too high")
            print(f"You have {i} attemps remaining")
        i-=1
    print("You run out of guesses you loss")

def hard():
    print("You have 5 attempts remaining to guess the number")
    game=True
    i=4
    while game is True and i>=0:
        guess=int(input("Make a guess: "))
        if guess==answer:
            game=False
            return print(f"You got it the answer is {answer}")
            
        elif guess<answer:
            print("Too low")
            print(f"You have {i} attemps remaining")
        else:
            print("Too high")
            print(f"You have {i} attemps remaining")
        i-=1
    print("You run out of guesses you loss")



if difficulty=="easy":
    easy()
elif difficulty=="hard":
    hard()