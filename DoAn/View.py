from Model import Student,Person,Score,Professor,Subject,Faculty
from Control import InfoStudent

class EnterInfomationStudent:

    def infoStudent(self) -> Student:
        name = input('Name Student: ')
        sex = input('Sex: ')
        phone = input('Phone: ')
        email = input('Email: ')
        id = input('ID: ')
        student = Student(name,sex,phone,email,id)
        return student

