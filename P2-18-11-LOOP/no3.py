#Exercise 3: Calculate the sum of all numbers from 1 to a given number
num = int(input('number: '))
sum = 0
for i in range(num+1):
    sum += i
print('sum =',sum)