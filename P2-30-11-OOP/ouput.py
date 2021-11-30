from Person import Person,Student,Lecturer
def main():
    LQT=Student('Lê Quang Trung',1,'0898167571',13,1)
    DTNM=Student('Đặng Thái Nhật Minh',1,'09901238',23,1)
    PTLN=Lecturer('Phạm Thị Lê Na',2,"071231223",10,3)
    print(LQT.outputStudent())
    print(DTNM.outputStudent())
    print(PTLN.outputLecturer())
if __name__=='__main__':
    main()
