from UML import Person,Student,Professor
import pickle

def main():

    # Enter Information
    n=3
    per = []
    stu = []
    pro = []
    count = 1
    while count <= n:
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
    count1=0
    while count1 < n:
        print('Person',count1+1)
        print(per[count1].outputPerson())

        print('Student',count1+1)
        print(stu[count1].outputStudent())

        print('Professor',count1+1)
        print(pro[count1].outputProfessor())
        count1+=1

 #Sort lists
    for i in range(n):
        for j in range(i+1,n):
            if per[i].name < per[j].name:
                per[i],per[j]=per[j],per[i]

            if stu[i].averagemark < stu[j].averagemark:
                stu[i],stu[j] = stu[j],stu[i]

            if pro[i].salary > pro[j].salary:
                pro[i],pro[j] = pro[j],pro[i]

  #Dump lists into file
    f = open('per.txt', 'wb')
    for i in per:
        pickle.dump(i.outputPerson(), f)
    f.close()

    f = open('stu.txt', 'wb')
    for i in stu:
        pickle.dump(i.outputStudent(), f)
    f.close()

    f = open('pro.txt', 'wb')
    for i in pro:
        pickle.dump(i.outputProfessor(), f)
    f.close()

    #Load lists from file
    f = open('per.txt', 'rb')
    for i in per:
        a = pickle.load(f)
        print(a)
    f.close()

    f = open('stu.txt', 'rb')
    for i in stu:
        b = pickle.load(f)
        print(b)
    f.close()

    f = open('pro.txt', 'rb')
    for i in pro:
        c = pickle.load(f)
        print(c)
    f.close()

if __name__=='__main__':
    main()