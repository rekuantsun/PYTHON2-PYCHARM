'''Bài 7: Viết chương trình thực hiện các yêu cầu sau:
- Thực hiện yêu cầu như bài 6
- Sau khi thực hiện xong cho người dùng lựa chọn tiếp tục thực hiện lại hay kết thúc chương
trình'''
def bacnhat(b,c):
    if b == 0:
        if c == 0:
            print('vô số nghiệm')
        else:
            print('vô nghiệm')
    else:
        print('có một nghiệm x =',c/b)
def bachai(a,b,c):
    import math
    denta = b**2 - 4*a*b
    if denta>0:
        x1=(-b - math.sqrt(denta)) / (2*a)
        x2=(-b + math.sqrt(denta)) / (2*a)
        print('Phương trình có 2 nghiệm')
        print('x1 =',round(x1,3))
        print('x2 =',round(x2,3))
    if denta == 0:
        x = (-b) / (2*a)
        print('Phương tình có một nghiệm duy nhất')
        print('x1 = x2 =',x)
    if denta < 0:
        print('Phương trình vô nghiệm')
def tieptuc():
    print('Bạn có muốn tiếp tục tính toán')
    print('Nhập Yes để tiếp tục\nNhập No để dừng lại')
    YoN= input('Yes or No').upper()
    if YoN == 'YES':
        main()
    else:
        pass
def main():
    print('Chương trình giải phương trình bậc 1 hoặc bậc 2')
    print('Nhấn (1) để giải pt bậc nhất\nNhấn (2) để giải pt bậc hai')
    choice = int(input('Lựa chọn của bạn: '))
    if choice == 1:
        b=float(input('b = '))
        c=float(input('c = '))
        bacnhat(b,c)
    if choice == 2:
        a=float(input('a = '))
        b=float(input('b = '))
        c=float(input('c = '))
        if a != 0:
            bachai(a,b,c)
        else:
            bacnhat(b,c)
    tieptuc()
if __name__ == '__main__':
    main()
