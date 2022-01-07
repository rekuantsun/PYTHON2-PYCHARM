from Model import Person, Student, Professor, Score, Subject, Faculty
import pickle

class StudentManager:
    listStu: list[Student]

    def __init__(self) -> None:
        super().__init__()
        self.listStu=[]

    def addStu(self, student: Student) -> None:
        self.listStu.append(student)

    def getlistStu(self) -> list[Student]:
        return self.listStu






