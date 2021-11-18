#Exercise 10: Write a program to display all prime numbers within a range
start = int(input('start: '))
end = int(input('end: '))
for i in range (start, end):
    if i > 1:
        for j in range (2,i):
            if i % j == 0:
                break
        else:
            print(i,end=' ')