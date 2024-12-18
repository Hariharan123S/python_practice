import random
pictures = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''',  '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  |   |
  O   |
  |   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''

  +---+
  |   |
      |
      |
      |
      |
=========
  +---+''']
print("*****Welcome to Hangman game!*****")
print('''
 _                                             
| |                                            
| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
| '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
| | | | (_| | | | | (_| | | | | | | (_| | | | |
|_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                    __/ |                      
                   |___/       ''')
name_list = ["lion", "tiger", "cheetah"]
choice = random.choice(name_list)
print(choice)
ans = ""
dash = len(choice)
for j in range(dash):
    ans += "_ "
print(ans)
# name = input("Guess a letter: ").lower()
display = ""
a = False
crt_lt = []
lives = 6
while not a:
    print(f"**********Your remaining lives: {lives}/6 **********")
    name = input("Guess a letter: ").lower()
    display = ""
    for i in choice:
        if i == name:
            display += i
            crt_lt.append(name)
        elif i in crt_lt:
            display += i
        else:
            display += "_"
    print(display)
    print(pictures[lives])
    if name not in choice:
        lives -= 1
        print(f"**********Your remaining lives: {lives}/6 **********")
        print(pictures[lives])
        if lives == 0:
            a = True
            print("**********GAME OVER**********\n**********You Loose**********")
    if "_" not in display:
        a = True
        print("**********You Win!**********")





