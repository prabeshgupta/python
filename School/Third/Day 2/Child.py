from Father import Father
from Mother import Mother

class Child(Father, Mother):
    def __init__(self, father_name, mother_name, child_name):
        Father.__init__(self, father_name)
        Mother.__init__(self, mother_name)
        self.child_name = child_name

    def display(self):
        print(f'Father name: {self.father_name}\nMother name: {self.mother_name}\nChild name: {self.child_name}')

child1 = Child("JP Gupta", "Sanu Gupta", "Prabesh Gupta")
child1.display()