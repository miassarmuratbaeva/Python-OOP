class Student:
    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade
student1 = Student("Miyasar Muratbaeva", 16, "9-sinf")
student2 = Student("Azimov Shaxzod", 17, "10-sinf")
student3 = Student("usmanova SArvinoz", 15, "8-sinf")
print(student1.name, student1.age, student1.grade)
print(student2.name, student2.age, student2.grade)
print(student3.name, student3.age, student3.grade)