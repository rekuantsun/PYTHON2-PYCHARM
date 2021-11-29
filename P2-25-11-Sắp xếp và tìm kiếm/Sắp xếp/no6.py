'''Bài 6: Viết chương trình thực hiện các yêu cầu sau:
- Xây dựng hàm sinh_ngau_nhien_danh_sach_so_nguyen( ), thực hiện các thao tác sau:
o Sinh ngẫu nhiên 1 danh sách số nguyên gồm n phần tử;
o Trong đó, n được nhập vào từ bàn phím và số nguyên sinh ra nằm trong khoảng từ
0 đến max_value;
o Giá trị max_value được nhập vào từ bàn phím;
o Hàm này trả về danh sách các số nguyên được sinh ngẫu nhiên ở trên.
- Xây dựng hàm sap_xep_giam_dan(x), trong đó:
o Tham số đầu vào x là một danh sách các số nguyên;
o Hàm này trả về một danh sách các số nguyên được sắp xếp theo chiều giảm dần.
- Xây dựng hàm sap_xep_tang_dan(x), trong đó:
o Tham số đầu vào x là một danh sách các số nguyên;
o Hàm này trả về một danh sách các số nguyên được sắp xếp theo chiều tăng dần.
- Chương trình chính (__main__) gọi thực hiện các hàm trên và in kết quả ra màn hình.'''
import random
def sinh_ngau_nhien_danh_sach_so_nguyen(n,max_value):
    l1 = []
    for i in range(n):
        l1.append(random.randint(0, max_value))
    return l1
def sap_xep_giam_dan(x):
    for i in range(len(x)):
        for j in range(i + 1, len(x)):
            if x[i] < x[j]:
                x[i], x[j] = x[j], x[i]
    return x
def sap_xep_tang_dan(x):
    for i in range(len(x)):
        for j in range(i + 1, len(x)):
            if x[i] > x[j]:
                x[i], x[j] = x[j], x[i]
    return x
def main():
    n=int(input('số phần tử của danh sách: '))
    max_value=int(input('giới hạn random: '))
    x=sinh_ngau_nhien_danh_sach_so_nguyen(n,max_value)
    print('danh sách sau khi sắp xếp tăng dần:',sap_xep_tang_dan(x))
    print('danh sách sau khi sắp xếp giảm dần:', sap_xep_giam_dan(x))
if __name__=='__main__':
    main()