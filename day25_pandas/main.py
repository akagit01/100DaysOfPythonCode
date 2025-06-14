import pandas

data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data_20250605.csv")
#total_count=data

#(data[data.day=="Monday"])

#gray=data[data["Primary Fur Color"=="Gray"]]
gray = data[data["Primary Fur Color"] == "Gray"]
#print(type(gray))
#print((data["Primary Fur Color"]=="Black").count())
cinnamon=data[data["Primary Fur Color"]=="Cinnamon"]
black=data[data["Primary Fur Color"]=="Black"]
print(f"no of gray squirrels: {len(gray)}")
print(f"no of gray squirrels: {len(cinnamon)}")
print(f"no of gray squirrels: {len(black)}")
g_squir=len(gray)
b_squir=len(black)
c_squir=len(cinnamon)

dict1={"squirrel":["gray","black","cinnamon"],
       "Number":[g_squir,b_squir,c_squir]}

data2=pandas.DataFrame(dict1)
data2.to_csv("squirrels_count_per_color.csv")

print(pandas.read_csv("squirrels_count_per_color.csv"))

"""
gray_count=gray.count()
cinnamon=(data["Primary Fur Color"]=="Cinnamon")
cn_count=cinnamon.count()
black=(data["Primary Fur Color"]=="Black")
b_count=black.count()
#=="Gray".count())
#fur_color_g=data[data["Primary Fur Color"]=="Gray"].count()
print(gray_count)
print(cn_count)
print(b_count)
"""