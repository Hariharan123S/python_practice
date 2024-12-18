import random

Rock = '''Rock
   _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___) '''
Paper = '''Paper
    _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)'''
Scissor = '''Scissor
   _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)'''
ans = int(input("What do you choose? Type 0 for Rock, 1 for Paper, 2 for Scissor.\n"))
if ans == 0:
    print(Rock)
elif ans == 1:
    print(Paper)
elif ans == 2:
    print(Scissor)

rty = [Rock, Paper, Scissor]
elements = random.randint(0, 2)
print(rty[elements])

if ans == 1 and elements == 0:
    print("You Win!")
if ans == 0 and elements == 1:
    print("Computer Wins!")
elif ans == 2 and elements == 0:
    print("Computer Wins!")
elif ans == 0 and elements == 2:
    print("You Win!")
elif ans == 1 and elements == 2:
    print("Computer Win!")
elif ans == 2  and elements ==1:
    print("You Win")
else:
    print("Match Draw")
