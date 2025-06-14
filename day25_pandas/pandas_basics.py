
"""
with open("weather_data.csv") as file:
    data=file.readlines()
print(data)
"""

"""
import csv


temperature=[]
with open("weather_data.csv") as file:
    data= csv.reader(file)
    for row in data:
        if row[1] != 'temp':
            temperature.append(int(row[1]))

print(temperature)
"""

import pandas

data = pandas.read_csv("weather_data.csv")
#print(data["temp"])

print(type(data)) #dataframe
print(type(data["temp"])) #series

data_dict=data.to_dict()
print(data_dict)

temp_list=data["temp"].to_list()
print(temp_list)

avg_temp=sum(temp_list)/len(temp_list)
print(f"avg temp is {round(avg_temp,2)}")

avg_tmp2=data["temp"].mean()
print(round(avg_tmp2,2))

max_temp=data["temp"].max()
print(max_temp)

#you can also directly refer to column headers
print(data.temp)
print(data.condition)


#in order to get a particular row
print(data[data.day=="Monday"])
print(data[data.temp== data.temp.max()])

monday=data[data.day=="Monday"]
print(monday.condition)
monday_temp_f= monday.temp * (9/5) + 32
print(monday_temp_f)


#create a data frame from scratch

data_dict1={
    "students":["Amy","Anna","Michael"],
    "scores":[76,56,65]
}

data2=pandas.DataFrame(data_dict1)
print(data2)
data2.to_csv("new_data.csv")



