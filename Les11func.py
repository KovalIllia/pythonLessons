#example 1
def sum(num_1, num_2):
    result = num_1 + num_2
    print(result)


sum(10, 20)
sum(30, 40)

#example 2
def hi(name):
    print(f"Hello {name}")

hi("Alex")

#example 3
def hi(name="Kaleb"):
    print(f"Hello {name}")

hi()

#example 4
name="Boris"
def hi(name):
    print(f"Hello {name}")

hi(name)

#example 5
name="Ben"#input()
#age=32
def hi(name,age):
    print(f"Hello! My name is {name}, I`m {age} old")

hi(name,32)


#example 6
name="Tom"
age="33"
def hi(name,age):
    result=name+" "+age
    return result

h=hi(name,age)
print(h)
# print(hi(name,age))