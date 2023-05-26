print("Welcome to Python Pizza Deliveries! ")
size = input("Whats size pizza do you want? S, M or L? ")
bill = 0

if size == "S":
    bill += 15
    add_pepperoni = input("Do you want pepperoni? Yes or No? ")
    if add_pepperoni == "Yes":
        bill += 2
elif size == "M":
    bill += 20
    add_pepperoni = input("Do you want pepperoni? Yes or No? ")
    if add_pepperoni == "Yes":
        bill += 3
elif size == "L":
    bill += 25
    add_pepperoni = input("Do you want pepperoni? Yes or No? ")
    if add_pepperoni == "Yes":
        bill += 3

extra_cheese = input("Do you want extra cheese? Yes or No? ")
if extra_cheese == "Yes":
    bill += 1

tip_choice = input("Which type of tip do you want to give? 10%, 15%, 20%, or None? ")
if tip_choice == "10%":
    tip = 0.1
elif tip_choice == "15%":
    tip = 0.15
elif tip_choice == "20%":
    tip = 0.2
else:
    tip = 0

total_bill = bill + (bill * tip)
print(f"Your total is ${total_bill:.2f}")