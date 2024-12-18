'''print("Welcome to the tip calculator!")
bill = float(input("What was the total bill? $"))
tip = int(input("How much tip would you like to give? 10%, 12%, or 15%? (just type the number) "))
people = int(input("How many people to split the bill? "))
amt = ((tip/100) * bill) + bill
fi = amt / people
print("Each person should pay: $" + str(round(fi, 2)))'''

'''weight = float(input("What is your weight? "))
height = float(input("What is your height? "))
bmi = weight / (height**2)
if bmi < 18.5:
    print("Underweight")
    if bmi < 25 and bmi >= 18.5:
        print("Normal weight")
else:
    print("Overweight")'''

print("Welcome to the pizza Delivery!")
size = input("What size of pizza do you want? S, M, or L: ")
pepperoni = input("Do you want to add pepperoni to your pizza? type 'X' for Yes and 'Y' for No: ")
extra_cheese = input("Do you want to add extra cheese? Y or N: ")
bill = 0
if size == "S":
    bill += 150
elif size == "M":
    bill += 200
elif size == "L":
    bill += 250
else:
    print("Try again")
if pepperoni == "X":
    if size == "S":
        bill += 15
    else:
        bill += 25
if extra_cheese == "Y":
    bill += 30

print("Your final bill is Rs." + str(bill))








