'''Bài 4: Hãy viết chương trình thực hiện các yêu cầu sau:
- Xây dựng hàm giải phương trình bậc 1 (ax + b = 0), với hệ số a & b được truyền vào qua
thông số của hàm.
- Chương trình chính nhận các thông số a, b từ bàn phím
- Chương trình chính gọi hàm giải phương trình bậc 1 nêu trên'''
def bacnhat(a,b):
    if a == 0:
        if b == 0:
            print('vô số nghiệm')
        else:
            print('vô nghiệm')
    else:
        print('có một nghiệm x =',b/a)

def main():
    a=float(input('a = '))
    b=float(input('b = '))
    bacnhat(a,b)
if __name__ == '__main__':
    main()