class Student:
    def __init__(self, name, age, course):
        self.name = name
        self.age = age
        self.course = course
    def introduce(self):
        print(f"Hello, my name is {self.name}, I am {self.age} years old and I am studying {self.course}.")

student1 = Student("VANESSA", 22, "CRIMINOLOGY")
student2 = Student("RUBIN", 21, "INFORMATION TECHNOLOGY")
student3 = Student("GWEN", 19, "NURSING")

student1.introduce()
student2.introduce()
student3.introduce()