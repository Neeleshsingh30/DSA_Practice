# squared = []

# for i in range(10):
#     squared.append( i * i)
# print(squared)

# print("----------------------------------------------")

# sqaure = [i * i for i in range(6)]
# print(sqaure)

# print("----------------------------------------------")

# even = [ i * i for i in range(10) if i % 2 == 0]
# print(even)
# print("----------------------------------------------")

# def student(**kwargs):
#     print(kwargs)

# student(name="Neelesh", age=22)
# print("----------------------------------------------")

class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def study(self):
        print("Student is studying")

        
student1 = Student("Neelesh", 22)
student2 = Student("Rahul", 21)