class Person:
    name: str
    phonenumber: str
    emailaddress: str

    def __init__(self,Name,PhoneNumber,EmailAddress) -> None:
        super().__init__()
        self.name = Name
        self.phonenumber = PhoneNumber
        self.emailaddress = EmailAddress

    def outputPerson(self) -> str:
        ans = 'Name: '+self.name+'; Phone number: '+self.phonenumber+'; Email address: '+self.emailaddress+'\n'
        return ans

class Student(Person):
    studentnumber: str
    averagemark: str

    def __init__(self, Name, PhoneNumber, EmailAddress,StudentNumber,AverageMark) -> None:
        Person.__init__(self,Name, PhoneNumber, EmailAddress)
        self.studentnumber = StudentNumber
        self.averagemark = AverageMark

    def outputStudent(self) -> str:
        ans = self.outputPerson() + 'Student Number: '+self.studentnumber+'; Average Mark: '+self.averagemark+'\n'
        return ans

class Professor(Person):
    salary: int

    def __init__(self, Name, PhoneNumber, EmailAddress,Salary) -> None:
        Person.__init__(self,Name, PhoneNumber, EmailAddress)
        self.salary = Salary

    def outputProfessor(self) -> str:
        ans = self.outputPerson() + 'Salary: '+str(self.salary)+ '\n'
        return ans

