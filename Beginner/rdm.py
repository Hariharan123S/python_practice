import random
Districts_of_TN = ["Trichy", "Madurai", "Chennai", "Salem", "Tirunelveli"]
States_of_India = ["TamilNadu", "Kerala", "Telangana", "Rajasthan", "Karnataka", "Gujarat"]
rty = random.randint(0, 4)
print(Districts_of_TN[rty])
print(len(Districts_of_TN))
# Districts_of_TN[-1] = "Kanyakumari"
print(Districts_of_TN)
print(Districts_of_TN[0])
abc = [Districts_of_TN, States_of_India]
print(abc[0])
print(abc[1][2])

