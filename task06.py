class Student:
    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade
    def info(self):
        print(f"{self.name}, {self.age} yoshda, {self.grade}-sinf oquvchisi.")
student1 = Student("Ali", 15, 9)
student2 = Student("Malika", 16, 10)
student1.info()
student2.info()