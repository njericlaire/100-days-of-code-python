import random
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
logo = """
.------.            _     _            _    _            _    
|A_  _ |.          | |   | |          | |  (_)          | |   
|( \/ ).-----.     | |__ | | __ _  ___| | ___  __ _  ___| | __
| \  /|K /\  |     | '_ \| |/ _` |/ __| |/ / |/ _` |/ __| |/ /
|  \/ | /  \ |     | |_) | | (_| | (__|   <| | (_| | (__|   < 
`-----| \  / |     |_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\\
      |  \/ K|                            _/ |                
      `------'                           |__/           
"""
def calculate_score(cards):
    """Take a list of cards and return the score calculated from the cards"""
    if sum(cards) == 21 and len(cards) == 2:
        return 0

    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)

    return sum(cards)

def compare(u_score, c_score):
    """Compares the user score u_score against the computer score c_score."""
    if u_score == c_score:
        return "Draw 🙃"
    elif c_score == 0:
        return "Lose, opponent has Blackjack 😱"
    elif u_score == 0:
        return "Win with a Blackjack 😎"
    elif u_score > 21:
        return "You went over. You lose 😭"
    elif c_score > 21:
        return "Opponent went over. You win 😁"
    elif u_score > c_score:
        return "You win 😃"
    else:
        return "You lose 😤"

print(logo)
def blackjack():
    choice=input("Do you want to play blackjack? Type 'y' for yes and 'n' for no? ")
    if choice=="y":
        your_card=[]
        computer_card=[]
        for i in range(2):
            your_card.append(random.choice(cards))
            computer_card.append(random.choice(cards))


        continue_playing=True
        while continue_playing:
            your_sum=calculate_score(your_card)
            computer_sum=calculate_score(computer_card)
            print(f"Your card: {your_card} current score:{your_sum} ")
            print(f"Computers first card: {computer_card[0]}")
           

            if your_sum == 0 or computer_sum == 0 or your_sum > 21:
                continue_playing = False
            else:
                next = input("Type 'y' to get another card, type 'n' to pass: ")


                if next=="y":
                    your_card.append(random.choice(cards))
                elif next=="n":
                    continue_playing=False
        while computer_sum != 0 and computer_sum < 17:
            computer_card.append(random.choice(cards))
            computer_sum = calculate_score(computer_card)
        print(f"Your final card: {your_card} Total: {your_sum}")
        print(f"Computer final card: {computer_card} Total: {computer_sum}")
        print(compare(your_sum, computer_sum))
        blackjack()
blackjack()