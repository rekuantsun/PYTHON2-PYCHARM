'''Bài 4: Viết chương trình liệt kê tất cả các số nguyên tố nhỏ hơn n. Số nguyên dương n được nhập
từ bàn phím.'''
n = int(input('Giới hạn: '))
while n < 0:
    print('mời nhập lại')
    n = int(input('Giới hạn: '))
print('các số nguyên tố nhỏ hơn n là: ')
for i in range(2,n+1):
    for j in range (2,i):
        if (i%j==0):
            break
    else:
        print(i,end=' ')
