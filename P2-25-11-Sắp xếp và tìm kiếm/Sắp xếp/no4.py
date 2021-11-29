'''Bài 4: Viết chương trình thực hiện các yêu cầu sau:
- Xây dựng hàm nhap_danh_sach_so_thuc( ) thỏa mãn các yêu cầu sau:
o Sau khi nhập mỗi số thực từ bàn phím, chương trình hỏi người dùng có muốn tiếp
tục nhập không. Nếu người dùng gõ ký tự n hoặc N thì kết thúc quá trình nhập;
o Hàm trả về danh sách các số thực đã nhập.
- Xây dựng hàm sap_xep_danh_sach_so_thuc(x), với:
o Tham số đầu vào x là một danh sách các số thực;
o Hàm này trả về một danh sách các số thực được sắp xếp theo chiều giảm dần
- Chương trình chính (__main__) gọi thực thi 2 hàm nêu trên và in kết quả sắp xếp ra màn
hình.'''
def nhapdanhsach():
    l1 = []
    while True:
        n=float(input('phần tử của danh sách: '))
        l1.append(n)
        print('Nhập Y để tiếp tục hoặc N để kết thúc:')
        choice = input().upper()
        if(choice == 'N'):
            break
    return l1
def sapxepdanhsachsothuc(x):
    for i in range(len(x)):
        for j in range(i + 1, len(x)):
            if x[i] < x[j]:
                x[i], x[j] = x[j], x[i]
    return x
def main():
    x = nhapdanhsach()
    print('danh sách trước khi sắp xếp:',x)
    print('danh sách sau khi sắp xếp:',sapxepdanhsachsothuc(x))
if __name__=="__main__":
    main()