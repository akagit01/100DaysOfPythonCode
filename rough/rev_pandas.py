import pandas


data= pandas.read_csv("weather_data2.csv")
print(data)
print(data["temp"])
print(data[data["temp"]>20]["condition"])

data2=data.to_dict()
print(data2)

temp_list=data["temp"].to_list()
print(type(temp_list))

avg_temp=sum(temp_list)/len(temp_list)
print(round(avg_temp,2))

print(data["temp"].mean())
print(data["temp"].max())

print(data[data.day == 'Monday'])
print(data[data["temp"] == data["temp"].max()])

monday_temp=data[data.day == "Monday"].temp
mon_temp_farenheit=monday_temp*(9/5)+32
print(mon_temp_farenheit)

#create a dataframe from scratch
data_dict2={
    "student":['A','B','C'],
    "scores":[11,22,33]
}

new_data=pandas.DataFrame(data_dict2)
new_data.to_csv("new_data.csv")

squirrel_data=pandas.read_csv("2018__Squirrel_Data.csv")
gray_squirrel=squirrel_data[squirrel_data["Primary Fur Color"]=="Gray"]
gray_squirrel_count=len((gray_squirrel))
black_squirrel=squirrel_data[squirrel_data["Primary Fur Color"]=='Black']
black_squirrel_count=len(black_squirrel)
cinnamon_squirrel=squirrel_data[squirrel_data["Primary Fur Color"]=='Cinnamon']
innamon_squirrel_count=len(cinnamon_squirrel)
squirrel_dict3={
    "color":["Gray","Black","Cinnamon"],
    "count":[gray_squirrel_count,black_squirrel_count,innamon_squirrel_count]
}
print(squirrel_dict3)
squirrel_color_count_data=pandas.DataFrame(squirrel_dict3)
squirrel_color_count_data.to_csv("squirrel_count_based_on_color.csv")


