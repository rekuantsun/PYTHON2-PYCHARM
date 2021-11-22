n = int(input('tổng số số fibonacci đầu tiên: '))
l1=[]
lim = int(input())
count2= 1
count = 1
n1 = 0
n2 = 1
if n == 1:
    print(n1)
else:
    while count <= n:
        if(n1 > 2):
            l1.append(n1)
            nt = n1 + n2
            n1 = n2
            n2 = nt
            count += 1
        else:
            nt = n1 + n2
            n1 = n2
            n2 = nt
            count += 1
print('các số vừa là số fibonacci vừa là số nguyên tố:')
for i in range(len(l1)):
    for j in range(2,l1[i]):
        if l1[i] % j == 0:
            break
    else:
        if count2 == lim:
            print(l1[i],end=' ')
            break
        else:
            print(l1[i], end=' ')