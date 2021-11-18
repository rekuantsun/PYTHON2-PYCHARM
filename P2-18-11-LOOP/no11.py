#Exercise 11: Display Fibonacci series up to 10 terms
lim=int(input('Số số fibonacci mong muốn: '))
n1 = 0
n2 = 1
count = 0
while lim <= 0:
    print('Mời nhập số dương')
    lim = int(input('Số số fibonacci mong muốn: '))
if lim == 1:
    print(n1)
else:
    print('Dãy fibonacci cần tìm:')
    while count < lim:
        print(n1,end=' ')
        ntb = n1 + n2
        n1 = n2
        n2 = ntb
        count+=1

