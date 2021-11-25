'''Bài 2: Viết chương trình thực hiện các yêu cầu sau:
- Xây dựng hàm có tên nhap_danh_sach_so_nguyen(n), trong đó:
o Tham số đầu vào n là số phần tử của danh sách;
o Hàm này trả về một danh sách gồm n số nguyên được nhập vào từ bàn phím
- Xây dựng hàm có tên sap_xep_danh_sach(x), trong đó:
o Tham số đầu vào x là một danh sách các số nguyên
o Hàm này trả về một danh sách các số nguyên được sắp xếp theo chiều tăng dần
- Chương trình chính (__main__) gọi thực thi 2 hàm nêu trên và in kết quả sắp xếp ra màn
hình.'''
def nhap_danh_sach_so_nguyen(n):
    l1 = []
    for i in range(n):
        l1.append(int(input('phần tử: ')))
    return l1
def sap_xep_danh_sach(x):
    for i in range(len(x)):
        for j in range(i+1,len(x)):
            if x[i] > x[j]:
                x[i], x[j] = x[j], x[i]
    return(x)
def main():
    n = int(input('số phần tử của danh sách: '))
    x = nhap_danh_sach_so_nguyen(n)
    print('danh sách trước khi sắp xếp:', x)
    print('danh sách sau khi sắp xếp (tăng dần):',sap_xep_danh_sach(x))
if __name__ =='__main__':
    main()
