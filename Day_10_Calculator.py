import art
print(art.logo_cal)
def add(n1, n2):
    return n1 + n2


def subtract(n1, n2):
    return n1 - n2


def multiply(n1, n2):
    return n1 * n2


def divide(n1, n2):
    return n1 / n2





maths_dictionaries = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}


def calculator():
    maths = True
    num1 = int(input("Type the first number: "))

    while maths:
        for symbol in maths_dictionaries:
            print(symbol)
        operation = input("Type a mathematical operator: ")
        num2 = int(input("Type the second number: "))
        result = maths_dictionaries[operation](num1, num2)
        print(f"{num1} {operation} {num2} = {result}")
        continue_cal: str = input(f"Type 'y' if wants to continue the calculation with {result} or "
                                  f"'n' to start new calculation: ").lower()
        if continue_cal == "y":
            num1 = result
        if continue_cal == "n":
            maths = False
            print("\n" * 100)
            calculator()


calculator()
