#Exercise 12: Find the factorial of a given number
n=int(input('Giai thừa số: '))
fac=1
print('Giai thừa số',n,'là:',end=' ')
while n >= 1:
    fac *= n
    n-=1
print(fac)