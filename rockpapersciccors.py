import random
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
type = int(input("What do you choose? Type 0 for rock, 1 for paper and 2 for scissors"))
if type==0:
    print(rock)
elif type==1:
    print(paper)
else:
    print(scissors)

number = random.randint(0,2)
print("Computer choice")
if number==0:
    print(rock)
elif number==1:
    print(paper)
else:
    print(scissors)

if type>=3 or type<0:
     print("invalid choice")
elif type==0 and number==2:
    print("Your win")
elif number==0 and type==2:
    print("Your lose")
elif number>type:
    print("You Lose")
elif type>number:
    print("You win")
else :
    print("Draw")

   