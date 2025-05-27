class Person():
    """Human model"""

    def __init__(self, name, age, height):
        """Init human atributes"""
        self.name = name
        self.age = age
        self.height=height
        self.weight=100


    def description_person(self):
        """Get description of created person"""
        description= f"Name: {self.name}, age:{int(self.age)}, height:{int(self.height)}, weight:{int(self.weight)}"
        print(description)

    def get_weight(self):
        """Get weight of created person"""
        print(f"weight of this person: {self.weight}")

    def update_weight(self,kg):
        """Update weight of created person"""
        self.weight=kg



man = Person("Tom", 30,180)
woman = Person("Alza", 33,200)
man.description_person()

# woman.weight=50
woman.update_weight(66)
woman.description_person()

