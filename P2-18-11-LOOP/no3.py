#Exercise 3: Calculate the sum of all numbers from 1 to a given number
num = int(input('number: '))
sum = 1
for i in range(num):
    sum += i
print('sum =',sum)