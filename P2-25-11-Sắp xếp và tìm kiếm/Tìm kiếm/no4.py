'''Bài 4: Viết chương trình thực hiện các yêu cầu sau:
- Bước 1: Sinh ngẫu nhiên 1 danh sách n số nguyên trong đoạn [a, b], với các thông số n, a
và b được nhập vào từ bàn phím;
- Bước 2: Nhập vào 1 số x từ bàn phím có giá trị trong đoạn [a, b];

- Bước 3: Sắp xếp danh sách trên theo chiều tăng dần
- Bước 4: Tìm kiếm x có xuất hiện trong danh sách trên hay không theo yêu cầu sau:
o Nếu có thì trả về tất cả các vị trí xuất hiện trong danh sách và thông báo số bước
lặp đã thực hiện để tìm được các phần tử này.
o Ngược lại, thông báo không tìm thấy.'''
import random

n=int(input('số phần tử của danh sách: '))
a=int(input('random start: '))
b=int(input('random end: '))
l=[]
for i in range(n):
    l.append(random.randint(a,b))
print('danh sách đã tạo:',l)
x = int(input('giá trị cần tìm x là: '))
for i in range(len(l)):
    for j in range(i + 1, len(l)):
        if l[i] > l[j]:
            l[i], l[j] = l[j], l[i]
print('danh sách sau khi sắp xếp theo chiều tăng dần:',l)
count = 0
for i in range(len(l)):
    if l[i] == x:
        print('vị trí xuất hiện của x là:',i)
    count += 1
    print('số lần lặp là:', count)
else:
    print('không tìm thấy giá trị x')
