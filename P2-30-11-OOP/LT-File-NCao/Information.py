from UML import Person,Student,Professor
import pickle

def main():
    # Enter Information
    per = []
    stu = []
    pro = []
    count = 1
    while count <= 4:
        print('Person',count)
        per.append(Person(input('Name:'), input('Phone: '), input('Email: ')))

        print('Student',count)
        stu.append(Student(input('Name:'), input('Phone: '), input('Email: '),
                           input('ID: '), input('AVG Mark: ')))

        print('Professor',count)
        pro.append(Professor(input('Name:'), input('Phone: '), input('Email: '),
                             int(input('Salary: '))))
        count += 1

   #Display
    '''count1=0
    while count1 < 10:
        print(per[count1].outputPerson())
        print(stu[count1].getStudent())
        print(pro[count1].outputProfessor())
        count1+=1'''

    #Sort lists
    for i in range(4):
        for j in range(i+1,4):
            if per[i].name < per[j].name:
                per[i],per[j]=per[j],per[i]
            if stu[i].averagemark < stu[j].averagemark:
                stu[i],stu[j]=stu[j],stu[i]
            if pro[i].salary > pro[j].salary:
                pro[i],pro[j]=pro[j],pro[i]

    #Dump lists into file
    for i in per:
        f = open('per.txt', 'wb')
        pickle.dump(i.outputPerson(), f)
        f.close()

    for i in stu:
        f = open('stu.txt', 'wb')
        pickle.dump(i.getStudent(), f)
        f.close()

    for i in pro:
        f = open('pro.txt', 'wb')
        pickle.dump(i.outputProfessor(), f)
        f.close()

    #Load lists from file
    for i in range(4):
        f = open('per.txt', 'rb')
        a = pickle.load(f)
        f.close()
        print(a)

    for i in range(4):
        f = open('stu.txt', 'rb')
        b = pickle.load(f)
        f.close()
        print(b)

    for i in range(4):
        f = open('pro.txt', 'rb')
        c = pickle.load(f)
        f.close()
        print(c)

if __name__=='__main__':
    main()