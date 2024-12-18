'''def great():
    print("Hello")
    print("Good Morning")
    print("Have a nice day")

great()'''


# FUNCTIONS WITH INPUTS
def greet_with_name(name, location):
    print(f"Hello {name}!")
    print(f"Good Morning {name}")
    print(f"Are you going to {location} tomorrow?")


greet_with_name("Hari", "Chennai")

# functions with multiple inputs,
# positional arguments
# keyword arguments

greet_with_name(location="trichy", name="Hari")


def calculate_love_score(name1, name2):
    combined_names = name1 + name2
    b = combined_names.lower()
    t = b.count('t')
    r = b.count('r')
    u = b.count('u')
    e = b.count('e')
    score1 = t + r + u + e
    l = b.count('l')
    o = b.count('o')
    v = b.count('v')
    e = b.count('e')
    score2 = l + o + v + e
    love_score = score1 + score2
    print(love_score)


calculate_love_score("Hariharan", "Nayanthara")
b = "boy"
b >> 2
