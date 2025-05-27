class Person():
    """Create Human model"""

    def __init__(self, name, age, height, weight=110):
        """Init human atributes"""
        self.name = name
        self.age = age
        self.height = height
        self.weight = weight

    def description_person(self):
        """Get description of created person"""
        description = f"Name: {self.name}, age:{int(self.age)}, height:{int(self.height)}, weight:{int(self.weight)}"
        print(description)

    def get_weight(self):
        """Get weight of created person"""
        print(f"weight of this person: {self.weight}")

    def update_weight(self, kg):
        """Update weight of created person"""
        self.weight = kg


class Warior(Person):
    """Create Warior model"""

    def __init__(self, name, age, height, weight=111):
        super().__init__(name, age, height, weight)
        self.rage=100 #default parametr only for this class Warior

    def get_rage(self):
        """Get rage of created warior"""
        print(f"rage of warior: {self.rage}")

    def description_person(self):
        """Get description of created warior"""
        description = f"Name: {self.name}, age:{int(self.age)}, height:{int(self.height)}, weight:{int(self.weight)}, rage:{self.rage}"
        # print(description)
        return description

# man=Person("Tom",32,180,92)
# man.description_person()