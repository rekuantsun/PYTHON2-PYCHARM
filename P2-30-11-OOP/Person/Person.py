class Person:
    name: str
    gender: int
    phone: str

    def __init__(self,name,gender,phone) -> None:
        super().__init__()
        self.name = name
        self.gender = gender
        self.phone = phone

    def outputPerson(self) -> str:
        ans = 'name: '+self.name+'; gender: '+str(self.gender)+'; phone: '+self.phone+'\n'
        return ans

class Student(Person):
    studentID: int
    studentClass: int

    def __init__(self, name, gender, phone, ID,stuclass) -> None:
        Person.__init__(self,name, gender, phone)
        self.studentID = ID
        self.studentClass = stuclass

    def outputStudent(self) -> str:
        ans = self.outputPerson() + 'ID: '+str(self.studentID)+'; Class: '+str(self.studentClass)+'\n'
        return ans

class Lecturer(Person):
    lecturerID: int
    yearOfExperience: int

    def __init__(self, name, gender, phone, ID,YOE) -> None:
        Person.__init__(self,name, gender, phone)
        self.lecturerID = ID
        self.yearOfExperience = YOE

    def outputLecturer(self) -> str:
        ans = self.outputPerson() + 'ID: '+str(self.lecturerID)+'; YearOfExperience: '+str(self.yearOfExperience)+'\n'
        return ans

