# import mod.some
# import mod.some
from mod import some

a=int(input("Please input a first value: "))
operation=input("Please what operation do you want: ")
b=int(input("Please input a second value: "))
if operation=="+":
    some.sum(a,b)
elif operation=="-":
    some.difference(a,b)
elif operation=="*":
    some.multiplication(a,b)
elif operation=="/":
    some.division(a,b)


