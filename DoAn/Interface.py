import pickle

from Model import Student,Person,Score,Subject,Faculty,Professor
from Control import StudentManager
from View import EnterInformation


def interface():
    print('--- STUDENT MANAGER ---')
    print(' FACULTY: KHDL & TTNT')
    print('      2021-2022')
    print('-----------------------')
    print('* Danh sách thao tác: *')
    print('* 1. Thêm sinh viên.  *')
    print('-----------------------')
    print('\n')



def main():
    '''    #khởi tạo
    qlsv = StudentManager()
    ntt = EnterInformation()

    # khóa học
    khoa=Faculty('KHDL & TTNT',2)

    #thầy giáo
    levanhoa=Professor('Lê Văn Hòa','Nam','123','lvh@','Tiến sĩ',20000)
    nguyendinhhoacuong=Professor('Nguyễn Đình Hoa Cương','Nam','234','ndhc@','Tiến sĩ',20000)
    tranxuanmau=Professor('Trần Xuân Mậu','Nam','345','txm@','Tiến sĩ',20000)

    # giao diện hiển thị
    interface()
    choose=int(input('Lựa chọn của bạn: '))

    # thêm sinh viên
    if choose == 1:
        print('--- Thêm sinh viên ---')

        #thông tin sinh viên
        nstu = int(input('Số sinh viên muốn nhập: '))
        for i in range(nstu):
            print('sinh viên',i+1)
            stu = ntt.Student()
            qlsv.addStu(stu)
            #môn học sinh viên đăng ký
            nsub = int(input('Số môn học đã đăng ký: '))
            for j in range(nsub):
                print('môn học',j+1)
                sub = ntt.Subject()
                gvphutrach=input('marker: ')
                if gvphutrach == 'levanhoa':
                    levanhoa.setfaculty(khoa)
                    sub.setmarker(levanhoa)
                elif gvphutrach == 'nguyendinhhoacuong':
                    nguyendinhhoacuong.setfaculty(khoa)
                    sub.setmarker(nguyendinhhoacuong)
                else:
                    tranxuanmau.setfaculty(khoa)
                    sub.setmarker(tranxuanmau)
                stu.addsubject(sub)
                #bảng điểm
                score = ntt.Score()
                sub.addscore(score)

        #lưu sinh viên vào file
        dssv = qlsv.getlistStu()
        f=open('sinhvien.txt','wb')
        for student in dssv:
            pickle.dump(student.displayStu(khoa),f)
        f.close()

        #hiển thị danh sách
        f=open('sinhvien.txt','rb')
        for student in dssv:
            a=pickle.load(f)
            print(a)
        f.close()

    # tìm kiếm sinh viên
    if choose == 2:
        name=input()
'''

if __name__=='__main__':
    main()