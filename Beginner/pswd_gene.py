import random

lt = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w",
      "x", "y", "z", "A", "B", "C" "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W",
      "X", "X", "Y", "Z"]
sy = ["!", "@", "#", "%", "^", "&", "*", "(", ")"]
nm = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

print("Welcome to the PyPassword Generator!")
letters = int(input("How many letters would you like in your password?\n"))
symbols = int(input("How many symbols would you like?\n"))
numbers = int(input("How many numbers would you like?\n"))
Password = ""
'''for alp in range(1, letters + 1):
    char = random.choice(lt)
    Password += char
for i in range(1, symbols + 1):
    symb = random.choice(sy)
    Password += symb
for j in range(1, numbers + 1):
    numerical = random.choice(nm)
    Password += numerical
print("Your Password: " + Password)'''

paswd = []
for char in range(1,letters + 1):
    t = random.choice(lt)
    paswd.append(t)
for i in range(1, symbols + 1):
    r = random.choice(sy)
    paswd.append(r)
for j in range(1, numbers + 1):
    s = random.choice(nm)
    paswd.append(s)
print(paswd)
random.shuffle(paswd)
print(paswd)
password = ""
for k in paswd:
    password += k
print("Your password: " + password)
