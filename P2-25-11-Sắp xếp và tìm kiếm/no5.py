'''Bài 5: Viết chương trình thực hiện các yêu cầu sau:
- Sinh ngẫu nhiên 1 danh sách số nguyên gồm n phần tử. Trong đó, n được nhập vào từ bàn
phím và số nguyên sinh ra nằm trong khoảng từ 0 đến max_value. Giá trị max_value được
nhập vào từ bàn phím;
- Hỏi người dùng lựa chọn sắp xếp danh sách trên theo chiều tăng dần hay giảm dần và sắp
xếp danh sách theo lựa chọn của người dùng;
- In kết quả sắp xếp ra màn hình.'''
import random

max_value = int(input('giới hạn random: '))
n = int(input('số phần tử của danh sách: '))
l1 = []
for i in range (n):
    l1.append(random.randint(0,max_value))
print('danh sách trước khi sắp xếp',l1)
print('nhập (1) để sắp xếp danh sách tăng dần')
print('nhập (2) để sắp xếp danh sách giảm dần')
choice = int(input('lựa chọn của bạn: '))
if choice == 1:
    for i in range(len(l1)):
        for j in range(i + 1, len(l1)):
            if l1[i] > l1[j]:
                l1[i], l1[j] = l1[j], l1[i]
    print('danh sách sau sắp xếp tăng dần:',l1)
if choice == 2:
    for i in range(len(l1)):
        for j in range(i + 1, len(l1)):
            if l1[i] < l1[j]:
                l1[i], l1[j] = l1[j], l1[i]
    print('danh sách sau sắp xếp giảm dần:',l1)


