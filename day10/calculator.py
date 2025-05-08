def calc(a,op,b):
    if op=='+':
        return a+b
    elif op=='-':
        return a-b
    elif op=='*':
        return a*b
    elif op=='/':
        return float(a/b)
    else:
        print("Invalid input")
        return




res=calc(float(input("what's the first no: ")),
    input("+\n -\n *\n /\n Pick an operation :"),
    float(input("what's the second no: ")))
print(res)