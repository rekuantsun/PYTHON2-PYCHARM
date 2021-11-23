'''Bài 3: Hãy viết chương trình thực hiện các yêu cầu sau:
- Nhập một số nguyên dương n từ bàn phím (kiểm tra nếu không đạt yêu cầu thì bắt nhập
lại)
- Nhập một thông điệp từ bàn phím
- Gọi thực hiện hàm ở Bài 2 n lần với thông điệp được truyền làm tham số đầu vào của hàm.'''
def nhapn():
    n=int(input('Nhập số nguyên dương n: '))
    if(n<0):
        nhapn()
    return n
def inrachuoi(chuoi):
    print(chuoi)
def main():
    m=nhapn()
    for i in range(1,m+1):
        inrachuoi('Chúc mọi người một ngày tốt lành')
if __name__ == '__main__':
    main()
