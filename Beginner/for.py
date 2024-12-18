'''Marks = [70, 77, 91, 82, 89, 95]
# print(max(Marks))
initial = 0
for i in Marks:
    if i > initial:
        initial = i
print(initial)'''
for i in range(1, 101):
    if i % 3 == 0:
        i = "Fizz"
    elif i % 5 == 0:
        i = "Buzz"
    elif i % 3 == 0 and i % 5 == 0:
        i = "FizzBuzz"
    print(i)
