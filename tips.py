print("Welcome to the tip calculator!")
bill = float(input("What was the total bill? $"))
tip = int(input("How much tip would you like to give?10, 12 or 15?"))
people = int(input("How many to split the bill?"))
pay= (bill + (tip/100*bill))/people
print(f"Each person will pay {pay}")