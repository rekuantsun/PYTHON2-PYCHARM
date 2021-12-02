import pickle
import Call
import Member
def output_Person(L):
    for i in L:
        a,b,c= tuple(i)
        f=open('Person.obj','wb')
        pickle.dump(Member.Person(a,b,c).outputPerson(),f)
        f.close()

def output_Student():
    for i in Call.list_Student():
        a,b,c,d,e= tuple(i)
        f=open('Student.obj','wb')
        pickle.dump(Member.Student(a,b,c,d,e).outputStudent(),f)
        f.close()

def output_Professor():
    for i in Call.list_Professor():
        a,b,c,d= tuple(i)
        f=open('Professor.obj','wb')
        pickle.dump(Member.Professor(a,b,c,d).outputProfessor(),f)
        f.close()

def load_stu():
    f = open('Student.obj','rb+')
    r = pickle.load(f)
    f.close()
    return r

def load_per():
    f = open('Person.obj', 'rb+')
    r = pickle.load(f)
    f.close()
    return r
def load_pro():
    f = open('Professor.obj', 'rb+')
    r = pickle.load(f)
    f.close()
    return r

def main():
    output_Professor()
    print(load_pro())

    output_Student()
    print(load_stu())

    output_Person(Call.L)
    print(load_per())

if __name__=='__main__':
    main()