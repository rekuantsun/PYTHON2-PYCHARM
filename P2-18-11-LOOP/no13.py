#Exercise 13: Reverse a given integer number
n = input('number: ')
for i in range(len(n)-1,-1,-1):
    print(n[i],end='')