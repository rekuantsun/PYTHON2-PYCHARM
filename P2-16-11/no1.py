# Tạo một biến x kiểu List rỗng
x=[]

# Thêm giá trị 18 vào x
x.append(18)

#Thêm giá trị "Huế" vào x
x.append('Huế')

#Tạo 1 List y = [12, 45, -1, -0.56, "abc"]
y = [12, 45, -1, -0.56, "abc"]

#Thêm y vào x
x.extend(y)

#Xuất giá trị của x ra màn hình
print(x)

#In ra màn hình giá trị của phần tử cuối cùng và phần tử đầu tiên của x
print('phần tử đầu tiên:',x[0])
print('phần tử cuối cùng:',x[-1])

#In ra màn hình giá trị của phần tử đầu tiên đến phần tử thứ 5 của x
print('phần tử đầu tiên đến phần tử thứ 5:',x[:5])

#In ra màn hình giá trị của phần từ thứ 3 đến cuối cùng của x
print('phần tử thứ 3 đến phần tử cuối cùng:',x[2:])