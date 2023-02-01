class Book:
    def __init__(self, title, author, price):
        self.title = title
        self.author = author
        self.price = price

    
class Student:
    ID = 0
    def __init__(self, name, surname, age) -> None:
        Student.ID += 1
        self.id = Student.ID
        self.name = name
        self.surname = surname
        self.email = self.name + self.surname + str(self.id) + 'gmail.com'
        
    def register(self, library: 'Library'):
        return library.add_student(self)

  
class Library:
    def __init__(self, budget = 100000) -> None:
        self.books = []
        self.students = []
        self.budget = budget
        
    def add_student(self, student: 'Student'):
        if student.id in self.students:
            print("This student is already registered.")
        else:
            self.students.append(student.id)
            
            
            


student1 = Student('Mane', 'Mkrtchyan', 19)
student2 = Student('Mariam', 'Stepanyan', 20)
student3 = Student('Arina', 'Kostanyan', 20)

library = Library()

student1.register(library)
print(library.students)