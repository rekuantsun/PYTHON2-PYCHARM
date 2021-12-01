class Person:
    name: str
    phonenumber: int
    emailaddress: str

    def __init__(self,Name,PhoneNumber,EmailAddress) -> None:
        super().__init__()
        self.name = Name
        self.phonenumber = PhoneNumber
        self.emailaddress = EmailAddress

    def outputPerson(self) -> str:
        ans = 'Name: '+self.name+'; Phone number: '+str(self.phonenumber)+'; Email address: '+self.emailaddress+'\n'
        return ans

class Student(Person):
    studentnumber: int
    averagemark: float

    def __init__(self, Name, PhoneNumber, EmailAddress,StudentNumber,AverageMark) -> None:
        Person.__init__(Name, PhoneNumber, EmailAddress)
        self.studentnumber = StudentNumber
        self.averagemark = AverageMark

    def outputStudent(self) -> str:
        ans = self.outputPerson() + 'Student Number: '+str(self.studentnumber)+'; Average Mark: '+str(self.averagemark)+'\n'
        return ans

class Professor(Person):
    salary: int

    def __init__(self, Name, PhoneNumber, EmailAddress,Salary) -> None:
        Person.__init__(Name, PhoneNumber, EmailAddress)
        self.salary = Salary

    def outputProfessor(self) -> str:
        ans = self.outputPerson() + 'Salary: '+str(self.salary)
        return ans

