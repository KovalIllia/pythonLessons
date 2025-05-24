# ✅ Задача 1: Транспортний засіб
# Батьківський клас: Vehicle
# Атрибути: brand, model, year
# Метод: display_info() — виводить інформацію про транспорт.
#
# Клас-нащадок: Car
# Додатковий атрибут: doors (кількість дверей)
# Новий метод: is_family_friendly() — якщо дверей ≥ 4, виводить "Good for family".

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

mini=Car("BMW","Counrtyman",2008,2)
mini.display_info()
mini.is_family_friendly()


# ✅ Задача 2: Працівники
# Батьківський клас: Employee
# Атрибути: name, position, salary
# Метод: display_info() — виводить усі атрибути.
#
# Клас-нащадок: Manager
# Додатковий атрибут: team_size
# Новий метод: has_big_team() — якщо team_size > 10, виводить "Big team".