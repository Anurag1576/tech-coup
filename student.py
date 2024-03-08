from person import Person
class student1(Person):
    def __init__(self, name=None, age=None,roll=None,marks=None):
        super().__init__(name, age)
        self._roll = roll 
        self._marks = marks
    def input(self):
        super().input()
        self._roll = input("Roll : ") 
        self._marks = float(input("Marks : "))
    def show(self):
        super().show()
        print("Roll : " , self._roll)
        print("Marks : " , self._marks) 
    def giveExam(self):
        print("Exam Given !")         