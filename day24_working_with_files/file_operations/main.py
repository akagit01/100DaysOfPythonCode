"""

#one way of accessing file but you will always have to close it with this method
file = open("my_file.txt")
contents=file.read()
print(contents)
file.close()
"""

#another way where you don't need to mention close to close the file is using "with"
with open("my_file.txt",mode='a') as file:
    file.write("\n I will not lose")
    #new_content=file.read()
    #print(new_content)

with open("my_file.txt") as file:
    contents=file.read()
    print(contents)

with open("new_file.txt",mode='w') as file2:
    file2.write("this is a new file, created directly from code")

with open("new_file.txt") as file2:
    new_file_contents=file2.read()
    print(new_file_contents)