def add(*args):
    total=0
    for n in args:
        total+=n
    return total

tot=add(11,10,20,30)
print(tot)

def calculate(n,**kwargs):
    n += kwargs["add"]
    n *= kwargs["multiply"]

    print(n)

calculate(2,add=2,multiply=5)


