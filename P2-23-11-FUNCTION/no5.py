'''Bài 5: Hãy viết chương trình thực hiện các yêu cầu sau:
- Xây dựng hàm giải phương trình bậc (ax2 + bx + c = 0), với hệ số a & b & c được truyền
vào qua thông số của hàm.
- Chương trình chính nhận các thông số a, b & c từ bàn phím
- Chương trình chính gọi hàm giải phương trình bậc 2 nêu trên'''
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
    denta = b^2 - 4*a*b
    if denta>0:
        x1=(-b - math.sqrt(denta)) / (2*a)
        x2=(-b + math.sqrt(denta)) / (2*a)
        print('Phương trình có 2 nghiệm')
        print('x1 =',x1)
        print('x2 =',x2)
    if denta == 0:
        x = (-b) / (2*a)
        print('Phương tình có một nghiệm duy nhất')
        print('x1 = x2 =',x)
    if denta < 0:
        print('Phương trình vô nghiệm')
def main():
    a = int(input('a = '))
    b = int(input('b = '))
    c = int(input('c = '))
    if (a != 0):
        bachai(a,b,c)
    else:
        bacnhat(b,c)
if __name__ == '__main__':
    main()