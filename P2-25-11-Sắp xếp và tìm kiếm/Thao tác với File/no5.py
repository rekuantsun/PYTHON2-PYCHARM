'''Bài 5: Viết chương trình thực các yêu cầu sau:
- Sinh ngẫu nhiên 1 danh sách gồm 1000 số nguyên trong khoảng từ [-1000, 1000]
- Nhập tên tập tin từ bàn phím
- Ghi danh sách trên vào tập tin theo quy tắc:
o 10 số trên một hàng
o Các số phân tách nhau bởi dấu phẩy (,)
- Đọc nội dung tập tin ở trên và in ra màn hình theo quy tắc:
o 10 số trên một hàng
o Các số phan tách nhau bởi dấu tab.'''

import random
danhsach = []
count = 0
for i in range(1000):
    danhsach.append(random.randint(-1000, 1000))
filename = input("Tên tập tin: ") +'.txt'
for i in danhsach:
    if count < 9:
        f = open(filename, 'a')
        cktu = str(i)+','
        f.write(cktu)
        f.close()
        count +=1
    else:
        f = open(filename, 'a')
        f.write(str(i)+"\n")
        f.close()
        count = 0
f = open(filename, 'r')
a = f.readlines()
for i in a:
    print(i.replace(",", " "))
f.close()



