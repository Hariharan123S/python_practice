import pandas

data = pandas.read_csv('2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv')
color = data['Primary Fur Color']

count = []
gray = 0
red = 0
black = 0
for gray_col in color:
    if gray_col == 'Gray':
        gray += 1
    if gray_col == 'Cinnamon':
        red += 1
    if gray_col == 'Black':
        black += 1
count.append(gray)
count.append(red)
count.append(black)

park_dict = {"Fur Color": ["gray", "red", "black"],
             "Count": count
             }
park = pandas.DataFrame(park_dict)
print(park)
park.to_csv("squirrel_count")
