# Задача 1: Клас User
# Створи клас User з атрибутами:
# name
# role (за замовчуванням "guest")
# is_active (за замовчуванням True)
#
# Методи:
# deactivate() — ставить is_active = False
# display_info() — виводить ім’я, роль та статус активності

class User:

    def __init__(self, name,role="guest",is_active=True):
        self.name=name
        self.role="guest"
        self.is_active=True

    def deactive(self):
        self.is_active=False

    def display_info(self):
        print(f"Name:{self.name}, role:{self.role}, is_active:{self.is_active}")

first_user=User("Mick")
admin=User("Tom",role="admin")

first_user.display_info()
admin.display_info()


# Задача 2: Клас PizzaOrder
# Створи клас PizzaOrder з атрибутами:
# size (за замовчуванням "medium")
# toppings (за замовчуванням порожній список)
# extra_cheese (за замовчуванням False)
#
# Методи:
# add_topping(topping)
# summary() — виводить розмір піци, список топінгів і чи додано сир
#
# 📌 Порада: пам’ятай, що не варто ставити [] як дефолтне значення напряму в __init__,
# краще None і ініціалізувати вручну (тут перевіряється це знання 😉).

class PizzaOrder():

    def __init__(self):
        self.size="medium"
        self.toppings=[]
        self.extra_cheese=False

    def add_topping(self,toppings):
        # return self.toppings.append("chilli") # var_1
         self.toppings.append(toppings)# var_2


    def summary(self):
        print(f"size:{self.size}, toppings:{self.toppings}, extra_cheese:{self.extra_cheese}")

first_order=PizzaOrder()
# first_order.add_topping()# var_1
first_order.add_topping("mushrooms")# var_2
first_order.summary()


#  Задача 3: Клас TodoItem
# Створи клас TodoItem з атрибутами:
# task
# done (за замовчуванням False)
# priority (за замовчуванням "normal")
#
# Методи:
# mark_done() — змінює done на True
# display() — показує статус завдання (включаючи пріоритет)

class TodoItem():

    def __init__(self,task,priority="normal"):
        self.task=task
        self.done=False
        self.priority="normal"

    def mark_done(self):
        self.done=True

    def display(self):
        print(f"All information: {self.task}, status: {self.done}, priority: {self.priority}")

task_1=TodoItem("washing")
task_1.display()
task_1.mark_done()
task_1.display()