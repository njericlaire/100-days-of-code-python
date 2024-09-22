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


def format_data(account):
    A_name=account['name']
    A_desc=account['description']
    A_location=account['country']
    return f" {A_name}, a {A_desc} from {A_location}"
score=0
continue_playing=True
B = random.choice(data)


while continue_playing:
    
    print(logo)

    #get random data from the  data
    A=B
    B=random.choice(data)
    if A==B:
        B=random.choice(data)
    print(f"Compare A:{format_data(A)}")
    print(vs)
    print(f"Against  B:{format_data(B)}")
   
    choice=(input("Who has more followers. Type 'A' or 'B' ")).lower()
    A_follower=A["follower_count"]
    B_follower=B["follower_count"]
    result=compare(choice,A,B)
    if result:
        score+=1
        print(f"You're right! Current score {score}")
        
    else:
        print(f"Sorry, that's wrong. Final score: {score}.")
        continue_playing=False