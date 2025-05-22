# example 1
# a=int(input("Please input a first value: "))
# b=int(input("Please input a second value: "))
# result=int(a/b)
# print(f"result of operation: {result}")

# # example 2
# a=int(input("Please input a first value: "))
# b=int(input("Please input a second value: "))
# try:
#     result=int(a/b)
# except ZeroDivisionError:
#     print("Invalid operation!")
# print(f"result of operation: {result}")


# # example 3
# a=int(input("Please input a first value: "))
# b=int(input("Please input a second value: "))
# try:
#     result=int(a/b)
# except ZeroDivisionError:
#     result=0
#     print("Invalid operation!")
# print(f"result of operation: {result}")


# example 4
a=int(input("Please input a first value: "))
b=int(input("Please input a second value: "))
try:
    result=int(a/b)
except ZeroDivisionError:
    result=0
    print("Invalid operation!")
print(f"result of operation: {result}")

result_2=a+b
print(result_2)