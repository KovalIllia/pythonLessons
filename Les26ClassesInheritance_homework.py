"""✅ Задача 1: Транспортний засіб
Батьківський клас: Vehicle
Атрибути: brand, model, year
Метод: display_info() — виводить інформацію про транспорт.

Клас-нащадок: Car
Додатковий атрибут: doors (кількість дверей)
Новий метод: is_family_friendly() — якщо дверей ≥ 4, виводить "Good for family"."""

class Vehicle():

    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year

    def display_info(self):
        print(f"All information: brand={self.brand}, model={self.model}, year={self.year}")


class Car(Vehicle):

    def __init__(self, brand, model, year, doors):
        super().__init__(brand, model, year)
        self.doors = int(doors)

    def is_family_friendly(self):
        if self.doors >= 4:
            print(f"Good for family")
        else:
            print(f"Good for free people")

# mini=Car("BMW","Counrtyman",2008,2)
# mini.display_info()
# mini.is_family_friendly()


"""✅ Задача 2: Працівники
Батьківський клас: Employee
Атрибути: name, position, salary
Метод: display_info() — виводить усі атрибути.

Клас-нащадок: Manager
Додатковий атрибут: team_size
Новий метод: has_big_team() — якщо team_size > 10, виводить "Big team"."""


class Employee():

    def __init__(self,name,position,salary):
        self.name=name
        self.position=position
        self.salary=salary

    def display_info(self):
        return self.name,self.position,self.salary

class Manager(Employee):

    def __init__(self,name,position,salary,team_size):
        super().__init__(name,position,salary)
        self.team_size=team_size

    def has_big_team(self):
        if self.team_size>10:
            print("Big team")
        else:
            print("Standart")


# team_1=Manager("Alex","cleaner",20000,11)
# team_1.has_big_team()




"""# ✅ Задача 3: Домашні тварини
# Батьківський клас: Pet
# Атрибути: name, species
# Метод: make_sound() — виводить "Some generic sound".

# Клас-нащадок: Dog
# Перевизначити метод: make_sound() — замість стандартного звуку виводить "Woof!"
# Додатковий метод: fetch() — виводить "Dog is fetching the ball"."""

class Pet():

    def __init__(self,name,species):
        self.name=name
        self.species=species

    def make_sound(self):
        print(f"Some generic sound: {self.name}={self.species}")

class Dog(Pet):

    def __init__(self,name,species='hamster'):
        super().__init__(name,species)#or species="ayff!" or "ayff!" -- it`s default from class Pet

    def make_sound_new(self):
        print("Woof!")

    def fetch(self):
        print("Dog is fetching the ball")

# """exemple №1"""
# colli=Dog("Alexa",'aff!')
# colli.make_sound()
# """exemple №2"""
# colli=Dog("Alexa")
# colli.make_sound()
# """exemple №3"""
# colli=Dog("Alexa")
# colli.make_sound_new()



"""🔹 Задача 4: Птахи
Створи базовий клас Bird з такими атрибутами:
name – ім'я птаха
can_fly – за замовчуванням True

Методи:
make_sound() — виводить "Chirp!"
description() — виводить інформацію про птаха

Створи клас Penguin, який наслідується від Bird, але встановлює can_fly у False.
Додай метод swim(), який виводить "Penguin swims well!".

✅ Мета: продемонструвати зміну дефолтних атрибутів у нащадку."""

class Bird():
    def __init__(self,name,can_fly=True):
        self.name=name
        self.can_fly=can_fly

    def make_sound(self):
        print("Chirp!")

    def description(self):
        print(f"all information about this bird: name={self.name}, can_fly={self.can_fly}")

class Penguin(Bird):
    def __init__(self,name,can_fly=False):
        super().__init__(name,can_fly)

    def swim(self):
        print("Penguin swims well!")

new_bird=Penguin("Tomas")
new_bird.description()



"""🔹 Задача 5: Музичні інструменти
Створи базовий клас Instrument:
Атрибути: name, type (тип інструменту, напр. "перкусія", "струнний")
Метод: play() — виводить "Playing sound from {name}"

Створи клас Guitar:
Успадковується від Instrument
За замовчуванням тип — "струнний"
Додай метод tune() — виводить "Guitar is tuned!"

✅ Мета: потренувати дефолтні значення в ініціалізації класу-нащадка + додати власні методи."""

class Instrument():

    def __init__(self,name,type="percussion"):
        self.name=name
        self.type=type

    def play(self):
        print(f"Playing sound from {self.name}")

class Guitar(Instrument):
    def __init__(self,name,type="stringed"):
        super().__init__(name,type)

    def tune(self):
        print("Guitar is tuned!")

instrument_1=Instrument("viola")
instrument_2=Guitar("electro_guitar")
instrument_1.play()
instrument_2.tune()