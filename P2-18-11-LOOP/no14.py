#Exercise 14: Use a loop to display elements from a given list present at odd index positions
L=[1,2,3,4,5,'a','v','c','b']
for i in range(len(L)):
    if i % 2 == 1:
        print(L[i],end=' ')