import random



class School:
    def __init__(self,name,address):
        self.name = name
        self.address = address
        self.teachers = {}
        self.classrooms = {}
    
    def add_classroom(self):
        pass
    def add_teacher(self):
        pass
    def student_admission(self):
        pass
    def calculate_grade(self, marks):
        pass
    def grade_to_value(self,grade):
        pass
    def value_to_grade(self,value):
        pass
    def __repr__(self):
        pass

class ClassRoom:
    def __init__(self,name):
        self.name = name
        self.students = []
        self.subjects = []
        
    def add_student(self,student):
        pass
    def add_subject(self,subject):
        pass
    def take_semester_final(self):
        pass
    def get_top_students(self):
        pass
    
class Person:
    def __init__(self, name):
        self.name = name

class Teacher(Person):
    def __init__(self, name):
        super().__init__(name)
        
    def teach(self):
        pass
    
    def evaluate_exam(self,max_marks):
        return random.randint(0,max_marks)

class Student(Person):
    def __init__(self, name, enr_cls):
        super().__init__(name)
        self.enr_cls = enr_cls
        self.marks = {}
        self.grades = {}
        self.final_grade = None
    
    