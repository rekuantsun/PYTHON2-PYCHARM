#Bài 8: Viết chương trình liệt kê các số Fibonacci nhỏ hơn n là số nguyên tố. N là số nguyên dương
#được nhập từ bàn phím.
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