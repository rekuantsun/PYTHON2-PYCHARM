'''Bài 3: Viết chương trình nhập vào từ bàn phím một danh sách các số thực, theo các yeu cầu sau:
- Sau khi nhập mỗi số thực từ bàn phím, chương trình hỏi người dùng có muốn tiếp tục nhập
không. Nếu người dùng gõ ký tự n hoặc N thì kết thúc quá trình nhập;
- Sắp xếp danh sách các số thực tren theo chiều giảm dần;
- In kết quả ra màn hình.'''
def nhapdanhsach():
    l1=[]
    while True:
        n=float(input('phần tử của danh sách: '))
        l1.append(n)
        print('Nhập Y để tiếp tục hoặc N để kết thúc:')
        choice = input().upper()
        if(choice == 'N'):
            return l1
            return False
def sapxepdanhsach(l1):
    for i in range(len(l1)):
        for j in range(i + 1, len(l1)):
            if l1[i] < l1[j]:
                l1[i], l1[j] = l1[j], l1[i]
    return l1
def main():
    l1 = nhapdanhsach()
    print('danh sách trước khi sắp xếp:',l1)
    print('danh sách sau khi sắp xếp (giảm dần):',sapxepdanhsach(l1))
if __name__=="__main__":
    main()