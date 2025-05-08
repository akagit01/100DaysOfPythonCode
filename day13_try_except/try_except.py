
''' In the below code if user passes string instead of number, it will throw value error'''
#age=int(input("enter age: "))
#if age>18:
#    print('you can apply for license')


'''so to deal with above scenario where user might enter string instead of number, we use try catch'''

try:
    age=int(input("enter age: "))
except ValueError:
    print("you have typed an invalid input. Please enter a number")
    age = int(input("enter age: "))
    if age>18:
        print('you can apply for license')