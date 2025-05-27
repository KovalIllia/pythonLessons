# import mod.some
# import mod.some
from mod import some_variant2

def run_calculator():
    a=int(input("Please input a first value: "))
    operation=input("Please what operation do you want: ")
    b=int(input("Please input a second value: "))
    if operation=="+":
        some_variant2.sum(a,b)
    elif operation=="-":
        some_variant2.difference(a,b)
    elif operation=="*":
        some_variant2.multiplication(a,b)
    elif operation=="/":
        some_variant2.division(a,b)


if __name__ == "__main__":
    run_calculator()