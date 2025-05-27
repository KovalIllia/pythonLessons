a=int(input("Please input a first value: "))
operation=input("Please what operation do you want: ")
b=int(input("Please input a second value: "))
if operation=="+":
    result=int(a + b)
    print((f"result of operation '{operation}' = {result}"))
elif operation=="-":
    result=int(a / b)
    print((f"result of operation '{operation}' = {result}"))
elif operation=="*":
    result=int(a * b)
    print((f"result of operation '{operation}' = {result}"))
elif operation == "/":
    result = int(a / b)
    print((f"result of operation '{operation}' = {result}"))
try:
    result=int(a/b)
except ZeroDivisionError:
    result=0
    print("Invalid operation!")


