#1
L=[1,2,3,4,5,6]
print('sum all the items in a list:',sum(L))

#2
import math
L1=[29,11,2]
print('multiply all the items in a list:',math.prod(L1))

#3
print('the largest number from a list:',max(L1))

#4
print('the smallest number from a list:',min(L1))

#5
L.sort(reverse=True)
print('sort a list in descending order: ',L)

#6
L1.sort()
print('sort a list in ascending order:',L1)

#7
print('get the size of a list:',len(L))

#8
import random
print('get random element(s) of a list:',random.choice(L))

#9
print('join two different lists into one:',L+L1)