'''def my_function():
    for i in range(1, 20+1):
        if i == 20:
            print("You got it")

my_function()


year = int(input("What's you year of birth? "))
if year >= 1980 and year < 1994:
    print("You are a millennial")
elif year >= 1994:
    print("You are a Gen Z.")'''


def is_leap(year):
    if year % 400 == 0 and year % 100 == 0:
        print("True")
    elif year % 4 == 0 and year % 100 != 0:
        print("True")
    else:
        print("False")

is_leap(2020)

def fizz_buzz(target):
    for number in range(1, target + 1):
        if number % 3 == 0 and number % 5 == 0:
            print("FizzBuzz")
        elif number % 3 == 0:
            print("Fizz")
        elif number % 5 == 0:
            print("Buzz")
    else:
        print([number])

fizz_buzz(15)
