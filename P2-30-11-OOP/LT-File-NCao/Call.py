from Member import Person,Student,Professor
def enter_Person():
    Name = input('Name: ')
    PhoneNumber = int(input('Phone Number: '))
    EmailAddress = input('Email Address: ')
    count = 1
    while count <=10:
        print(Person(Name,PhoneNumber,EmailAddress).outputPerson())
        count+=1

def enter_Student():
    Name = input('Name: ')
    PhoneNumber = int(input('Phone Number: '))
    EmailAddress = input('Email Address: ')
    StudentNumber = input('Student Number: ')
    AverageMark = float(input('Average Mark: '))
    count = 1
    while count <= 10:
        print(Student(Name, PhoneNumber, EmailAddress,StudentNumber,AverageMark).outputStudent())
        count += 1

def enter_Professor():
    Name = input('Name: ')
    PhoneNumber = int(input('Phone Number: '))
    EmailAddress = input('Email Address: ')
    Salary = int(input('Salary: '))
    count = 1
    while count <= 10:
        print(Professor(Name, PhoneNumber, EmailAddress, Salary).outputProfessor())
        count += 1

def main():
    enter_Person()
    enter_Student()
    enter_Professor()

if __name__=='__main()__':
    main()