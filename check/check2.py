class Person():
    name: str
    phonenumber: str
    emailadd: int

    def __init__(self, ten, sdt, mail) -> None:
        self.name = ten
        self.phonenumber = sdt
        self.emailadd = mail

    def outputPerson(self) -> str:
        result = "name: " + self.name + "; phonenumber: " + self.phonenumber + "; emailadd: " + str(self.emailadd)
        return result

class Student(Person):
    studentnumber: int
    avgmark: str

    def __init__(self, ten, sdt, mail, maHS, diemTB) -> None:
        Person.__init__(self, ten, sdt, mail)
        self.studentnumber = maHS
        self.avgmark = diemTB

    def outputStudent(self) -> str:
        result = self.outputPerson() + "; studentnumbe" + str(self.studentnumber) + "; avgmark" + self.avgmark
        return result

class Professor(Person):
    salary: str

    def __init__(self, ten, sdt, mail, luong) -> None:
        Person.__init__(self, ten, sdt, mail)
        self.salary = luong

    def outputProfessor(self) -> str:
        result = self.outputPerson() + "; salary" + self.salary
        return result

import pickle

def main():
    nguoi_list = []
    hocsinh_list = []
    thay_list = []
    n = 2
    #Nhập đối tượng
    for i in range(n):
        nguoi = Person(input("Tên:"), input("SĐT:"), input("Mail:"))
        nguoi_list.append(nguoi)
        hocsinh = Student(input("Tên:"), input("SĐT:"), input("Mail:"), input("Mã HS:"), input("Điểm TB:"))
        thay = Professor(input("Tên:"), input("SĐT:"), input("Mail:"), input("Lương:"))
        hocsinh_list.append(hocsinh)
        thay_list.append(thay)
    #Xuất người
    for i in range(n):
        print(nguoi_list[i].outputPerson())
    #Xuất sinh viên
    for i in range(n):
        print(hocsinh_list[i].outputStudent())
    #Xuất giảng viên
    for i in range(n):
        print(thay_list[i].outputProfessor())
    #sắp xếp
    for i in range(n):
        for j in range(i + 1, n):
            if (nguoi_list[i].name > nguoi_list[j].name):
                nguoi_list[i], nguoi_list[j] = nguoi_list[j], nguoi_list[i]
            if (hocsinh_list[i].avgmark < hocsinh_list[j].avgmark):
                hocsinh_list[i], hocsinh_list[j] = hocsinh_list[j], hocsinh_list[i]
            if (thay_list[i].salary < thay_list[j].salary):
                thay_list[i], thay_list[j] = thay_list[j], thay_list[i]
    #Xuất người
    for i in range(n):
        print(nguoi_list[i].outputPerson())
    #Xuất sinh viên
    for i in range(n):
        print(hocsinh_list[i].outputStudent())
    #Xuất giảng viên
    for i in range(n):
        print(thay_list[i].outputProfessor())
    #Chuyển đối tượng thành str
    for i in range(n):
        str(hocsinh_list[i].avgmark)
        str(thay_list[i].salyri)
    #Ghi đối tượng người vào file
    f1 = open('nguoi.txt', "wb")
    for i in nguoi_list:
      pickle.dump(i.outputPerson(), f1)
    f1.close()
    #Ghi đối tượng sinh viên vào file
    f2 = open('hocsinh.txt', "wb")
    for i in hocsinh_list:
      pickle.dump(i.outputStudent(), f2)
    f2.close()
    #Ghi đối tượng giảng viên vào file
    f3 = open('thay.txt', "wb")
    for i in thay_list:
      pickle.dump(i.outputProfessor(), f3)
    f3.close()
    #Đọc file đối tượng người
    f1 = open('nguoi.txt', 'rb')
    for i in range (n):
        x = pickle.load(f1)
        print(x)
    f1.close()
    #Đọc file đối tượng sinh viên
    f2 = open('hocsinh.txt', 'rb')
    for i in range(n):
        y = pickle.load(f2)
        print(y)
    f2.close()
    #Đọc file đối tượng giảng viên
    f3 = open('thay.txt', 'rb')
    for i in range(n):
        z = pickle.load(f3)
        print(z)
    f3.close()

if __name__ == "__main__":
   main()