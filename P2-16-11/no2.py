'''#1
n = float(input('enter number: '))
if (n >= 0):
    print('positive number')
else:
    print('negative number')

#2
x1=float(input('x1: '))
x2=float(input('x2: '))
x3=float(input('x3: '))
num_max=x1
if(num_max < x2):
    num_max = x2
if(num_max < x3):
    num_max = x3
print('the greatest number:',num_max)

#3
num=float(input('enter number: '))
if (num == 0):
    print('zero')
elif (num > 0):
    pon = 'positive number'
else:
    pon = 'negative number'
if (abs(num) < 1):
    print('small '+pon)
elif(abs(num)>1000000):
    print('large '+pon)
else:
    print(pon)

#4
days = ['monday','tuesday','wednesday','thurday','friday','saturday','sunday']
nday = int(input('Day: '))
if (1 <= nday <= 7):
    print('Day',nday,'of the week is',days[nday-1])
else:
    nday = nday % 7
    print('Day',nday,'of the week is',days[nday-1])'''

#5
import math
a = float(input('a = '))
b = float(input('b = '))
if(math.floor(a*1000)==math.floor(b*1000)):
    print('they are same')
else:
    print('They are different')