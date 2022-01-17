from Model import Student,Subject,Faculty,Professor,Score,Person

#khoa
fal=Faculty('KHDL & TTNT',2)
#danh sách giáo viên
import json
dsgiaovien={}
#Ngôn ngữ lập trình python - Nguyễn Đình Hoa Cương
nguyendinhhoacuong=Professor('Nguyễn Đình Hoa Cương','Nam','1234567890','ndhc@gmail.com','Tiến sĩ',10000)
dsgiaovien[nguyendinhhoacuong.name]=[]
dsgiaovien[nguyendinhhoacuong.name].append({
    "Name":nguyendinhhoacuong.name,
    "Sex":nguyendinhhoacuong.sex,
    "Phone":nguyendinhhoacuong.phone,
    "Email":nguyendinhhoacuong.email,
    "Qualification":nguyendinhhoacuong.qualification,
    "Salary":nguyendinhhoacuong.salary
})
#Nhập môn khoa học dữ liệu - Lê Văn Hòa
levanhoa=Professor('Lê Văn Hòa','Nam','1234567891','lvh@gmail.com','Tiến sĩ',10000)
dsgiaovien[levanhoa.name]=[]
dsgiaovien[levanhoa.name].append({
    "Name":levanhoa.name,
    "Sex":levanhoa.sex,
    "Phone":levanhoa.phone,
    "Email":levanhoa.email,
    "Qualification":levanhoa.qualification,
    "Salary":levanhoa.salary
})
#Tiếng anh chuyên ngành - Trần Xuân Mậu
tranxuanmau=Professor('Trần Xuân Mậu','Nam','1234567892','txm@gmail.com','Tiến sĩ',10000)
dsgiaovien[tranxuanmau.name]=[]
dsgiaovien[tranxuanmau.name].append({
    "Name":tranxuanmau.name,
    "Sex":tranxuanmau.sex,
    "Phone":tranxuanmau.phone,
    "Email":tranxuanmau.email,
    "Qualification":tranxuanmau.qualification,
    "Salary":tranxuanmau.salary
})
#Toán