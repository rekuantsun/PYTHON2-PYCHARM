from Member import Person,Student,Professor

def enter_Person():
    l=[]
    l.append(input('Name: '))
    l.append(input('Phone: '))
    l.append(input('Email: '))
    return l

def enter_Student():
    l1=[]
    l1.append(input('Name: '))
    l1.append(input('Phone: '))
    l1.append(input('Email: '))
    l1.append(input('ID: '))
    l1.append((float(input('AVG Mark: '))))
    return l1

def enter_Professor():
    l2=[]
    l2.append(input('Name: '))
    l2.append(input('Phone: '))
    l2.append(input('Email: '))
    l2.append(int(input('Salary: ')))
    return l2

def list_Student():
    L1=[]
    for i in range(10):
        L1.append(enter_Student())
    return L1

def list_Person(L):
    L=[]
    for i in range(10):
        L.append(enter_Person())
    return L

def list_Professor():
    L2=[]
    for i in range(10):
        L2.append(enter_Professor())
    return L2

def output_Person(L):
    for i in L:
        a,b,c= tuple(i)
        print(Person(a,b,c).outputPerson())

def output_Student():
    for i in list_Student():
        a,b,c,d,e= tuple(i)
        print(Student(a,b,c,d,e).outputStudent())

def output_Professor():
    for i in list_Professor():
        a,b,c,d= tuple(i)
        print(Professor(a,b,c,d).outputProfessor())

def main():
    L=[]

    #list person
    list_Person(L)
    output_Person(L)

    #list student
    list_Student()
    output_Student()

    #list professor
    list_Professor()
    output_Professor()

if __name__=='__main__':
    main()