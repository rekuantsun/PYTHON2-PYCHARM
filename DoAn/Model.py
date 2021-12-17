class Person:
    name: str
    sex: str
    phone: str
    email: str

    def __init__(self,name,sex,phone,email) -> None:
        super().__init__()
        self.name = name
        self.sex = sex
        self.phone = phone
        self.email = email

    def displayPer(self) -> str:
        result='name: '+ self.name +'\tsex: '+ self.sex + '\tphone: ' + self.phone + '\temail: ' + self.email
        return result

class Score:
    gpa: float
    test: float
    industrious: str

    def __init__(self,gpa,test,industrious) -> None:
        super().__init__()
        self.gpa = gpa
        self.test = test
        self.industrious = industrious

    def setgpa(self,gpa: float) -> None:
        self.gpa = gpa
    def settest(self,test: float) -> None:
        self.test = test
    def setindustrious(self,industrious: str) -> None:
        self.industrious = industrious
    def getgpa(self) -> float:
        return self.gpa
    def gettest(self) -> float:
        return self.test
    def getindustrious(self) -> str:
        return self.industrious

    def displayScore(self) -> str:
        display= 'Average mark: ' + str(self.gpa) + '\nTest mark: ' + str(self.test) +\
                 '\nIndustrious point: ' + self.industrious
        return display

class Faculty:
    name: str
    number: int

    def __init__(self,name: str, number: int) -> None:
        super().__init__()
        self.name=name
        self.number=number

    def setnamefac(self,name: str) -> None:
        self.name=name
    def setnumber(self,number: int) -> None:
        self.number=number
    def getnamefac(self) -> str:
        return self.name
    def getnumber(self) -> int:
        return self.number

    def displayFac(self) -> str:
        display='Faculty: ' + self.name + ';\tNumber: ' + str(self.number)
        return display

class Professor(Person):
    qualification: str
    faculty: Faculty
    salary: int

    def __init__(self, name, sex, phone, email, qualification, salary) -> None:
        Person.__init__(self, name, sex, phone, email)
        self.qualification=qualification
        self.salary=salary

    def setqualification(self,qualification: str) -> None:
        self.qualification=qualification
    def setfaculty(self,faculty: Faculty) -> None:
        self.faculty=faculty
    def setsalary(self,salary: int) -> None:
        self.salary=salary
    def getqualification(self) -> str:
        return self.qualification
    def getfaculty(self) -> Faculty:
        return self.faculty
    def getsalary(self) -> int:
        return self.salary

    def displayPro(self) -> str:
        display=self.displayPer() + '\nQualification: ' + self.qualification+\
                ';\tFaculty: ' + self.faculty.displayFac() + ';\tSalary: '+str(self.salary)
        return display

class Subject:
    name: str
    credit: int
    marker: Professor
    scoreboard: list[Score]

    def __init__(self,name: str, credit: int, marker: Professor) -> None:
        super().__init__()
        self.name = name
        self.credit = credit
        self.marker = marker
        self.scoreboard = []

    def setnamesub(self,name: str) -> None:
        self.name=name
    def setcredit(self,credit: int) -> None:
        self.credit=credit
    def setmarker(self,marker: Professor) -> None:
        self.marker=marker
    def setscoreboard(self,scoreboard: list[Score]) -> None:
        self.scoreboard=scoreboard
    def addscore(self,score: Score) -> None:
        self.scoreboard.append(score)
    def getnamesub(self) -> str:
        return self.name
    def getcredit(self) -> int:
        return self.credit
    def getmarker(self) -> Professor:
        return self.marker
    def getscoreboard(self) -> list[Score]:
        return self.scoreboard

    def displaySub(self) -> str:
        display= 'Subject: ' + self.name +';\tCredits: ' + str(self.credit) +\
                 ';\nMarker\n' + self.marker.displayPro() + '\n'
        for i in self.scoreboard:
            display += (i.displayScore() + '\t')
        return display

class Student(Person):
    faculty: Faculty
    id: str
    listSub: list[Subject]
    scoreboard: list[Score]

    def __init__(self, name, sex, phone, email, id) -> None:
        Person.__init__(self, name, sex, phone, email)
        self.id=id
        self.listSub=[]
        self.scoreboard=[]

    def setfaculty(self,faculty: Faculty) -> None:
        self.faculty=faculty
    def setid(self,id: str) -> None:
        self.id=id
    def setlistsub(self,listSub: list[Subject]) -> None:
        self.listSub=listSub
    def addsubject(self, subject: Subject) -> None:
        self.listSub.append(subject)
    def setscoreboard(self,scoreboard: list[Score]) -> None:
        self.scoreboard=scoreboard
    def addscore(self,score: Score) -> None:
        self.scoreboard.append(score)
    def getfaculty(self) -> Faculty:
        return self.faculty
    def getid(self) -> str:
        return self.id
    def getlistsub(self) -> list[Subject]:
        return self.listSub
    def getscoreboard(self) -> list[Score]:
        return self.scoreboard

    def displayStu(self) -> str:
        display= self.displayPer() + '\nFaculty: ' + self.faculty.displayFac() + ';\tID: ' + self.id +  '\n'
        for i in self.listSub:
            display += (i.displaySub() + '\t')
        return display







