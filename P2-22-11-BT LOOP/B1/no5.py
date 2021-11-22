'''Bài 5: Viết chương trình liệt kê n số nguyên tố đầu tiên. Số nguyên dương n được nhập từ bàn
phím.'''
n = int(input('tổng số số nguyên tố : '))
lim = int(input('giới hạn: '))
count = 1
print('các số nguyên tố nhỏ hơn n là: ')
for i in range(2, n + 1):
    for j in range(2, i):
        if (i % j == 0):
            break
    else:
        if(count<lim):
            print(i, end=' ')
            count+=1
        elif (count == lim):
            print(i)
            break



