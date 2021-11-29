'''Bài 1: Viết chương trình nhập vào từ bàn phím một danh sách gồm 10 số nguyên và thực hiện các
yêu cầu sau:
- Sắp xếp danh sách trên theo chiều tăng dần
- In kết quả ra màn hình'''
a = []
while True:
    n=input('Nhập phần tử của danh sách: ').upper()
    if n == "N":
        break
    a.append(int(n))
print('Danh sách trước khi sắp xếp')
print(a)
print('Danh sách sau khi sắp xếp tăng dần')
for i in range(len(a)):
    for j in range(i+1,len(a)):
        if a[i]>a[j]:
            a[i], a[j] = a[j], a[i]
print(a)