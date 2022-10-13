"""

TASK 2

Write a base class to represent a student. Below is a starter code.
Feel free to add any more new features to your class.
As a minimum a student has a name and age and a unique ID.

Create a new subclass from student to represent a concrete student doing a specialization, for example:
Software Student and Data Science student.

"""


class Student:

    def __init__(self, name, surname, id):
        self.name = name
        self.surname = surname
        self.id = id
        self.subjects = dict()

class CFGStudent(Student):
    def __init__(self, name, surname, id, specialisation):
        super().__init__(name, surname, id)
        self.specialisation = specialisation #can be "Software"/"Data"/"Full Stack"


class ClassTopics(CFGStudent): #Please note in this example the CFGD is made up of class topics such as SQL, Python, Dev Concepts, OOP, etc.
    def __init__(self, name, surname, id, specialisation, topic):
        super().__init__(name, surname, id, specialisation)
        self.topic = topic


class Marks(ClassTopics):
    def __init__(self, name, surname, id, specialisation, topic, test_grade):
        super().__init__(name, surname, id, specialisation, topic)
        self.test_grade = test_grade

    def average_mark:


# class CFGStudent(<should inherit from Student>)
#     create new methods that manage student's subects (add/remove new subject and its graade to the dict)
#     create a method to view all subjects taken by a student
#     create a method  (and a new variable) to get student's overall mark (use average)
