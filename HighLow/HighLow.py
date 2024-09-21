from art import logo,vs
from data import data
import random



    
def compare(guess,A,B):
    if guess=="A":
        if A['follower_count']>B['follower_count']:
            return True
        else:
            return False
    else:
         if A['follower_count']<B['follower_count']:
            return True
         else:
            return False



continue_playing=True
score=0
while continue_playing:
    
    print(logo)

    #get random data from the  data
    A=random.choice(data)
    print(f"Compare A: {A['name']}, a {A['description']} from {A['country']}")
    print(vs)
    B=random.choice(data)
    print(f"Against B: {B['name']}, a {B['description']} from {B['country']}")
   
    choice=input("Who has more followers. Type 'A' or 'B' ")
    result=compare(choice,A,B)
    if result:
        score+=1
        print(f"Your score is {score}")
        continue_playing=result
    else:
        print(f"Your score is {score}")
        continue_playing=result