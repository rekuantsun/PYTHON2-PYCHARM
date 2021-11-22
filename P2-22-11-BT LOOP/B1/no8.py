#Bài 8: Viết chương trình liệt kê các số Fibonacci nhỏ hơn n là số nguyên tố. N là số nguyên dương
#được nhập từ bàn phím.
import math
lim = int(input("Nhập giới hạn: "))
list1 = []
list2 = []

while (lim < 0):
  print("Nhập sai, xin nhập lại!(> 0)")
  lim = int(input("Nhập giới hạn: "))

count, fi, se = 0, 0, 1
while (count < lim):
  if(count <= 1):
    th = count
  else:
    th = fi + se
    fi = se
    se = th
  list1.append(th)
  count += 1

count = 0
count1 = 0
while (count < len(list1)):
    flag = 0
    tmp = 2
    while (tmp <= math.sqrt(list1[count])):
        if ((list1[count] % tmp) == 0):
            flag = 1
        tmp = tmp + 1
    if (flag == 0 and list1[count] != 1 and list1[count] < lim):
        count1 += 1
        list2.append(list1[count])
    count += 1

print("Các số Fibonacci đồng thời là số nguyên tố nhỏ hơn", lim, "là: ", list2)