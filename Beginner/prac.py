import random


def maths(n1, n2):
    return n1 + n2


def mutate(a_list):
    b_list = []
    item = 0
    for i in a_list:
        item = i * 2
        item += random.randint(1, 3)
        item = maths(item, i)
        b_list.append(item)
    print(b_list)


mutate([1, 2, 3, 5, 8, 13])

