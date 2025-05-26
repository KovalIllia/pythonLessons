class Converter():

    def __init__(self,kg,cm):
        self.kg=kg
        self.cm=cm

    def kg_to_lbs(self):
        return self.kg*2.20462

    def cm_to_inches(self):
        return self.cm/2.54
