# 🧩 Задача 1: Клас Book
# Створи клас Book, який представляє книгу.
#
# Властивості:
# title (назва)
# author (автор)
# year (рік видання)
#
# Методи:
# display_info() — виводить інформацію про книгу у форматі:
# Назва: ..., Автор: ..., Рік: ...
#
#🔧Завдання:
#Створи 2 об'єкти книги.
#Виклич метод display_info() для кожного.
from itertools import count


class Book():

    def __init__(self,tittle,author,year):
        self.tittle=tittle
        self.author=author
        self.year=year

    def display_info(self):
        print(f"Tittle: {self.tittle}, Author: {self.author}, Year: {self.year}")

fantastic=Book("Duna","Frank Herbert",1963)
detective=Book("Sherlok Holmes","Sir Arthur Ignatius Conan Doyle",1900)

fantastic.display_info()
detective.display_info()


# 🧩 Задача 2: Клас Rectangle
# Створи клас Rectangle, який представляє прямокутник.
#
# Властивості:
# width
# height
#
# Методи:
# area() — повертає площу
# perimeter() — повертає периметр
#
# 🔧 Завдання:
# Створи об'єкт з шириною 5 і висотою 10.
# Виведи площу та периметр.


class Rectangle():

    def __init__(self,width,height):
        self.width=width
        self.height=height

    def area(self):
        result=int(self.height*self.width)
        print(f"Area of figure is: {result}")

    def perimeter(self):
        result=int(2*(self.width+self.height))
        print(f"Perimeter of figure is: {result}")

object_1=Rectangle(5,10)
object_1.area()
object_1.perimeter()



# 🧩 Задача 3: Клас Student
# Створи клас Student.
#
# Властивості:
# name
# grades — список оцінок
#
# Методи:
# add_grade(grade) — додає оцінку
# average_grade() — повертає середнє значення оцінок
#
# 🔧 Завдання:
# Створи об'єкт студента.
# Додай кілька оцінок.
# Виведи середню оцінку.

class Student():

    def __init__(self,name,grades):
        self.name=name
        self.grades=grades

    def add_grade(self):
        new_grade=self.grades.append(1)
        print(f"Added grade:{self.grades}")

    def average_grade(self):
        result_1= len(self.grades)
        result_2=sum(self.grades)
        result_3= float(result_2/result_1)
        print(f"average: {result_3}")

first_student=Student("Alex",[5,2,3,4])
first_student.average_grade()

