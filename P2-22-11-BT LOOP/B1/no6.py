#Bài 6: Viết chương trình liệt kê tất cả số nguyên tố có 5 chữ số.
print('Số nguyên tố có 5 chữ số: ')
for i in range(10000,100000):
    for j in range(2,i):
        if i%j==0:
            break
    else:
        print(i)