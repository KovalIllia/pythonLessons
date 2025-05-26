"""Задача 1: Математичні обчислення
Мета: Працювати з вбудованим модулем math.

📌 Завдання:
Імпортуй модуль math.
Обчисли квадратний корінь з 625.
Обчисли косинус числа π.
Виведи округлене значення логарифму по основі 10 від числа 1000."""

# import math
# import random
# from math import pi
#
# print(math.pi)
# print(math.sqrt(625))
# print(math.cos(math.pi))
#
# num = 1000
# base = 10
# log_value = math.log(num, base)
# rounded_log = round(log_value)
# print(f"Округлене значення логарифму: {rounded_log}")
# print()

""""Задача 2: Створення власного модуля
Мета: Створити модуль і імпортувати його в інший файл.

📌 Завдання:

Створи файл converter.py, в якому реалізуй функції:

kg_to_lbs(kg)

cm_to_inches(cm)

У файлі main.py імпортуй функції з converter і протестуй їх з різними значеннями."""

from Les26Import_p4Homework2 import Converter

value_1=Converter(100,2000)
print(f"value kg_to_lbs: {value_1.kg_to_lbs()}")
value_2=Converter(50,55)
print(f"value kg_to_lbs: {value_2.cm_to_inches()}")








"""Задача 3: Використання псевдонімів та імпорт частинами
Мета: Практика з import ... as та from ... import ...

📌 Завдання:

Імпортуй модуль datetime з псевдонімом dt.

Виведи поточну дату і час.

Імпортуй лише клас date з datetime.

Створи об'єкт дати свого народження.

"""

# from datetime import datetime as dt
# from datetime import date
# print(dt.now())
# print(date.today())
# print()


"""Задача 4: Випадкові числа
Мета: Практика з модулем random.

📌 Завдання:

Імпортуй модуль random.

Згенеруй випадкове ціле число від 1 до 100.

Створи список із 5 випадкових чисел.

Вибери випадковий елемент зі списку фруктів: ["apple", "banana", "cherry", "date"]."""

# import random
# value_1=random.randrange(1,100)
# value_2=random.randrange(1,100)
# value_3=random.randrange(1,100)
# value_4=random.randrange(1,100)
# value_5=random.randrange(1,100)
# result=[value_1,value_2,value_3,value_4,value_5]
# result_2=[random.randrange(1,100),random.randrange(1,100),random.randrange(1,100),random.randrange(1,100),random.randrange(1,100)]
# print(result)
# print(result_2)
# random_list=["apple", "banana", "cherry", "date"]
# print(random.choice(random_list))