def sum(a,b):
    result=int(a+b)
    print(f"Sum of this values: {result}")

def difference(a,b):
    result=int(a-b)
    print(f"Difference of this values: {result}")

def multiplication(a,b):
    result=int(a*b)
    print(f"Result of multiplication of this values: {result}")

def division(a,b):
    try:
        result=int(a/b)
    except ZeroDivisionError:
        result = 0
        print("Invalid operation!")
    print((f"result of division of this values: {result}"))

