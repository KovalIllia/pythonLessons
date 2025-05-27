class Person():
    """Human model"""

    def __init__(self, name, age):
        """Init human atributes - name,age"""
        self.name = name
        self.age = age
        print("Human was created")

    def sing(self):
        """We ask person to sing"""
        print(f"{self.name} can sing")

    def dance(self):
        """We ask person to dance"""
        print(f"{self.name} can dance")


man = Person("Tom", 30)
woman = Person("Elza", 30)

man.sing()
man.dance()

woman.sing()
