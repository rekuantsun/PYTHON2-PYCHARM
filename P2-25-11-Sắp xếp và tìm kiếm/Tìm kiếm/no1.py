'''Bài 1: Viết chương trình thực hiện các yêu cầu sau:
- Sinh ngẫu nhiên 1 danh sách n số nguyên trong đoạn [a, b], với các thông số n, a và b được
nhập vào từ bàn phím;
- Nhập vào 1 số x từ bàn phím có giá trị trong đoạn [a, b];
- Tìm kiếm x có xuất hiện trong danh sách trên hay không. Nếu có thì trả về vị trí xuất hiện
đầu tiên trong danh sách. Ngược lại, thông báo không tìm thấy.'''
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
    if l[i] == x:
        print('vị trí đầu tiên của x là:',i)
        break
else:
    print('không tìm thấy giá trị x')