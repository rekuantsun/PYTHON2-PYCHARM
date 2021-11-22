'''Bài 2: Viết một chương trình tính giai thừa của một số nguyên dương n. Với n được nhập từ bàn
phím. Ví dụ, n = 8 thì kết quả đầu ra phải là 1*2*3*4*5*6*7*8 = 40320.'''
print('Giai thừa số:')
i = int(input())
gt = 1
count = 1
l1 = ''
while i > 0:
    gt *= i
    i -= 1
while count <= i:
    if (count < i):
        l1+=str(count)+'*'
    else:
        l1+=str(count)+'='
    count += 1
print(gt)
