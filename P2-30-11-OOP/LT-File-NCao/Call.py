from Member import Person,Student,Professor

def enter_Person():
    l=[]
    l.append(input('Name: '))
    l.append(input('Phone: '))
    l.append(input('Email: '))
    return l

def enter_Student():
    l=[]
    l.append(input('Name: '))
    l.append(input('Phone: '))
    l.append(input('Email: '))
    l.append(input('ID: '))
    l.append((float(input('AVG Mark: '))))
    return l

def enter_Professor():
    l=[]
    l.append(input('Name: '))
    l.append(input('Phone: '))
    l.append(input('Email: '))
    l.append(int(input('Salary: ')))
    return l

def list_Student(L):
    for i in range(10):
        L.append(enter_Student())
    return L

def list_Person(L):
    for i in range(10):
        L.append(enter_Person())
    return L

def list_Professor(L):
    for i in range(10):
        L.append(enter_Professor())
    return L

def output_Person(L):
    for i in L:
        a,b,c= tuple(i)
        print(Person(a,b,c).outputPerson())

def output_Student(L):
    for i in L:
        a,b,c,d,e= tuple(i)
        print(Student(a,b,c,d,e).outputStudent())

def output_Professor(L):
    for i in L:
        a,b,c,d= tuple(i)
        print(Professor(a,b,c,d).outputProfessor())

def main():
    L=[]

    #list person
    list_Person(L)
    output_Person(L)

    #list student
    list_Student(L)
    output_Student(L)

    #list professor
    list_Professor(L)
    output_Professor(L)

if __name__=='__main__':
    main()