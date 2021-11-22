'''Bài 1: Viết chương trình thực hiện các yêu cầu sau:
- Nhập vào 1 số nguyên dương N từ bàn phím
- Hãy xây dựng 1 dictionary với các phần tử chỉ mục và giá trị có dạng (i: log(i)) với I đi từ
0 tới N
- Hiển thị dictionary trên ra màn hình'''
import math
n = int(input('số nguyên dương N: '))
d = {0:'lỗi'}
for i in range(1,n+1):
    d.update({i:math.log(i)})
print(d)