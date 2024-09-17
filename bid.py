logo = '''
                         ___________
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________\\
                       .-------------.
                      /_______________\\
'''
continue_bid=True
bid={}
def winner(bid):
    high=0
    bidder=""
    for key in bid:
        if high < bid[key]:
            high=bid[key]
            bidder=key
    print(f"The winner is {bidder} with a bid of {high}")


while continue_bid:
    print(logo)
    name=input("What is your name? ").lower()
    amount=int(input("What is your bid? $ "))
    bid[name]=amount
    next=input("Is there anyone else who want to bid?Yes or no? ").lower()
    if next=="no":
        continue_bid=False
        winner(bid)
    elif next=="yes":
        print("\n"*100)



# TODO-1: Ask the user for input
# TODO-2: Save data into dictionary {name: price}
# TODO-3: Whether if new bids need to be added
# TODO-4: Compare bids in dictionary