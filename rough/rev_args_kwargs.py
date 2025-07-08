def add(*args):
    tot=0
    for i in args:
        tot+=i
    return tot

no_sum=add(1,2,3,4,5,50)
print(no_sum)

def calculator(n,**kwargs):
    n+=kwargs['add']
    n*=kwargs['multiply']
    print(n)

calculator(2,add=3,multiply=2)

class Car():

    def __init__(self,**kwargs):
        self.make=kwargs["make"]
        self.model=kwargs.get("model")

my_car=Car(make="nissan")
print(my_car.make)
print(my_car.model) #.get in class attribute ensures None is returned if not initialised while creating object
