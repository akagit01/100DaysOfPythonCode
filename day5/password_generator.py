import random
from random import *
letters_list=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z',
         'A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
numbers_list=[0,1,2,3,4,5,6,7,8,9]
symbols_list=['!','@','#','$','%']

print("Welcome to the pyPassword generator")
letter=int(input('how many letters do you want in pwd?: '))
symb=int(input('how many symbols?: '))
num=int(input('how many no?: '))

pwd=[]
for i in range(letter+1):
    pwd.append(choice(letters_list))

for i in range(symb+1):
    pwd.append(choice(symbols_list))

for i in range(num+1):
    random_no=str(choice(numbers_list))
    pwd.append(random_no)
print(pwd)
print(''.join(pwd))
shuffle(pwd)
shuffled_pwd=''.join(pwd)
print(f'your password is {shuffled_pwd}')
