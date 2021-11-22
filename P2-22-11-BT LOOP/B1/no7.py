'''Bài 7: Viết chương trình tính tổng của các chữ số của môt số nguyên n. Số nguyên dương n được
nhập từ bàn phím. Ví dụ: n = 1234, tổng các chữ số: 1 + 2 + 3 + 4 = 10'''
n = input('số nguyên n: ')
count = 1
sum = 0
while count <= len(n):
    if(count<len(n)):
        print(n[count-1]+' + ',end='')
    elif(count==len(n)):
        print(n[count-1]+' = ',end='')
    sum += int(n[count-1])
    count+=1
print(sum)
