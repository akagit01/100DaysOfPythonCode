import pandas

#df1=pandas.DataFrame("file1.txt").to_csv("file1.csv")
#df2=pandas.DataFrame("file2.txt").to_csv("file2.csv")
#print(df1)


with open("file1.txt") as file:
    file1_content=[line.strip() for line in file]


with open("file2.txt") as file:
    file2_content=[line.strip() for line in file]

result=[n for n in file1_content if n in file2_content]

print(result)



