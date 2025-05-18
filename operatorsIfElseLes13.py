# #example №1
# age=int(input())
# if age>=18:
#     print(f"I`m {age} old. You have access")
# elif age<=18:
#     print(f"I`m {age} old. Access denied")
# else:
#     print("invalid character")
#
# # example №2
# name=input()
# if 'a' in name:
#     print(f"Hello Master")
# else:
#     print("invalid user")



# example №3
pin=1234
print("Input you password")
user_input=int(input())
if user_input==pin:
    print("What summ do you want?")
else:
    print("Error! Invalid password. You have 2 attempts")
    user_input = int(input())
    if user_input == pin:
        print("What summ do you want?")
    else:
        print("Error! Invalid password. You have 1 attempts")
        user_input = int(input())
        if user_input == pin:
            print("What summ do you want?")
        else:
            print("You card is blocked. Call you manager")