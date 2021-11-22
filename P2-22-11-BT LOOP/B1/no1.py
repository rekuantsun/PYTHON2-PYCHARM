'''Bài 1: Viết chương trình tìm tất cả các số chia hết cho 7 nhưng không phải bội số của 5, nằm trong
đoạn 10 và 200 (tính cả 10 và 200). Các số thu được sẽ được in ra màn hình.'''
count = 10
print('những số chia hết cho 7 và không là bội của 5:',end = ' ')
while count <= 200:
    if (count % 7 == 0) and (count % 5 != 0):
        print(count, end =' ')
        count += 1
    else:
        count += 1