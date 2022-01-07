from Model import Student,Person,Score,Professor,Subject,Faculty

class EnterInformation:

    def Student(self) -> Student:
        name = input('Name Student: ')
        sex = input('Sex: ')
        phone = input('Phone: ')
        email = input('Email: ')
        id = input('ID: ')
        student = Student(name,sex,phone,email,id)
        return student

    def Subject(self) -> Subject:
        name = input('Tên môn học: ')
        credit = int(input('Số tín chỉ: '))
        subject = Subject(name,credit)
        return subject

    def Score(self) -> Score:
        gpa=float(input('điểm trung bình: '))
        test=float(input('điểm thi: '))
        industrious=input('điểm chuyên cần: ')
        score=Score(gpa,test,industrious)
        return score