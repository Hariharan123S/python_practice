#with open('weather_data.csv') as data:
#    datas = data.readlines()
#    for values in datas:
#        list_values = values.strip()
#        print(list_values)

import csv

#with open('weather_data.csv') as data:
#    datas = csv.reader(data)
#    temperature = []
#    for rows in datas:
#        if rows[1] != 'temp':
#            temperature.append(int(rows[1]))
#    print(temperature)

import pandas
data = pandas.read_csv('weather_data.csv')
print(data)

print(data.day)

print(data["temp"].max())


print(data[data.temp == data.temp.max()])

monday = data[data.day == 'Monday']
value = monday.temp
C_to_F = (value * 1.8) + 32
print(f"{C_to_F}F")

#creating data frame

data_Dict = {
    "students": ['Amy', 'Jack', 'Hari'],
    "marks": [70, 80, 90]
}
datas = pandas.DataFrame(data_Dict)
print(datas)
datas.to_csv("new_data.csv")



