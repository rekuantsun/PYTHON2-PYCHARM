'''Bài 1: Viết chương trình nhập vào từ bàn phím một danh sách gồm 10 số nguyên và thực hiện các
yêu cầu sau:
- Sắp xếp danh sách trên theo chiều tăng dần
- In kết quả ra màn hình'''
a = [2,-1,1,9,-20,13,-18,65,11,-3]
for i in range(len(a)):
    for j in range(i+1,len(a)):
        if a[i]>a[j]:
            a[i], a[j] = a[j], a[i]
print(a)