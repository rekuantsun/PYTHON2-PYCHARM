from Member import Person,Student,Professor
def enter_Person():
    person=[]
    count = 1
    while count <=10:
        person.append(Person(input('Name: '),int(input('Phone Number: ')),input('Email Address: ')).outputPerson())
        count+=1
    return person
def enter_Student():
    student=[]
    count = 1
    while count <= 10:
        student.append(Student(input('Name: '), int(input('Phone Number: ')), input('Email Address: '),input('Student Number: '),float(input('Average Mark: '))).outputStudent())
        count += 1
    return student
def enter_Professor():
    professor=[]
    count = 1
    while count <= 10:
        professor.append(Professor(input('Name: '), int(input('Phone Number: ')), input('Email Address: '), int(input('Salary: '))).outputProfessor())
        count += 1
    return professor

def main():
    print(enter_Person())
    print(enter_Student())
    print(enter_Professor())

if __name__=='__main()__':
    main()