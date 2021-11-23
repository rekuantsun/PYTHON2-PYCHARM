'''Bài 6: Hãy viết chương trình thực hiện các yêu cầu sau:

- Cho người dùng lựa chọn giải phương trình bậc 1 hay bậc 2 bằng cách nhập số (1 hay 2)
từ bàn phím
- Nếu người dùng chọn giải phương trình bậc 1, thì thực hiện các bước như Bài 4
- Nếu người dùng chọn giải phương trình bậc 2, thì thực hiện các bước như Bài 5'''
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
if __name__ == '__main__':
    main()