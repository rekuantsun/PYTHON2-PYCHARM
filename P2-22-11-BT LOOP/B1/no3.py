'''Bài 3: Dãy số Fibonacci được định nghĩa như sau: F0 = 0, F1 = 1, F2 = 1, Fn = F(n-1) + F(n-2)
với n >= 2. Ví dụ: 0, 1, 1, 2, 3, 5, 8, ... Hãy viết chương trình tìm n số Fibonacci đầu tiên với n
nhập vào từ bàn phím.'''
n = int(input('tổng số số fibonacci đầu tiên: '))
count = 1
n1 = 0
n2 = 1
if n == 1:
    print(n1)
else:
    print(n,'số fibonacci đầu tiên là:',end=' ')
    while count <= n:
        print(n1,end=' ')
        nt = n1 + n2
        n1 = n2
        n2 = nt
        count += 1
