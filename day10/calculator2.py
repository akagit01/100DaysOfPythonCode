def add(n1,n2):
    return n1+n2

def sub(n1,n2):
    return n1-n2

def mul(n1,n2):
    return n1*n2

def div(n1,n2):
    return n1/n2

operations={'+':add,
          '-':sub,
          '*':mul,
          '/':div}


def calculator():
    continue_calculating=True

    n1=float(input("what's the first no: "))

    while continue_calculating:
        for symbol in operations:
            print(symbol)
        op = input("Pick an operation :")
        n2 = float(input("what's the second no: "))
        res = operations[op](n1, n2)
        print(f"{n1}{op}{n2}={res}")
        con = input("would you like to continue with previous result? Type Y/N.Or E for exit:").lower()
        if con == 'y':
            n1=res
        elif con=='n':
            continue_calculating=False
            calculator()
        else:
            print("thanks for using calculator")
            exit()


calculator()