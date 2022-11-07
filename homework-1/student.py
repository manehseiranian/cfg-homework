from statistics import mean
import random
"""

TASK 2

Write a base class to represent a student. Below is a starter code.
Feel free to add any more new features to your class.
As a minimum a student has a name and age and a unique ID.

Create a new subclass from student to represent a concrete student doing a specialization, for example:
Software Student and Data Science student.

"""


class Student:

    def __init__(self, name, surname, age, student_id):
        self.name = name
        self.surname = surname
        self.age = age
        self.student_id = student_id
        self.subjects = dict()


# class CFGStudent(<should inherit from Student>)
#     create new method that manages student's subjects (add/remove new subject and its grade to the dict)
#     create a method to view all subjects taken by a student
#     create a method  (and a new variable) to get student's overall mark (use average)


class CFGStudent(Student):
    def __init__(self, name, surname, age, student_id, specialisation):
        super().__init__(name, surname, age, student_id)
        self.specialisation = specialisation

    def add_subject(self, subject, mark):
        self.subjects[subject] = mark
        return self.subjects

    def remove_subject(self, subject):
        self.subjects.pop(subject)
        return self.subjects

    def view_subjects_taken(self):
        print(f"{self.name} {self.surname} took the following classes:")
        for subject in self.subjects:
            print(subject)

    def calculate_average_mark(self):
        average_mark = round(mean(list(self.subjects.values())))
        print(f"{self.name} {self.surname}'s average grade to date is {average_mark}%")



# EXAMPLE code run:

# Defining example students:
anna = CFGStudent(name="Anna", surname="Jones", age=21, student_id="1234", specialisation="Software")
sofie = CFGStudent(name="Sofie", surname="Kardashian", age=26, student_id="1235", specialisation="Software")
michelle = CFGStudent(name="Michelle", surname="Heer", age=23, student_id="1236", specialisation="Data")

# Adding example subjects and marks to students:

subjects_software = ["SQL", "Python", "Testing", "OOP"]
subjects_data = ["SQL", "Python", "Algorithms", "Big Data"]

for i in range(0, len(subjects_software)):
    anna.add_subject(subjects_software[i], random.randint(0, 100))
    sofie.add_subject(subjects_software[i], random.randint(0, 100))

for i in range(0, len(subjects_data)):
    michelle.add_subject(subjects_data[i], random.randint(0, 100))

# Removing example subjects from students

michelle.remove_subject("Big Data")


# Viewing the subjects taken by students

anna.view_subjects_taken()
sofie.view_subjects_taken()
michelle.view_subjects_taken()


# Viewing the overall grades of students:
anna.calculate_average_mark()
sofie.calculate_average_mark()
michelle.calculate_average_mark()
