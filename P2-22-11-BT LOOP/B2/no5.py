'''Bài 5: Viết chương trình thực hiện các yêu cầu sau:
- Nhập vào 1 danh sách các số nguyên từ bàn phím (Quá trình nhập dừng khi người dùng
nhập vào 1 kí tự từ a đến z)
- Hiển thị danh sách đó ra màn hình
- Yêu cầu người dùng nhập vào một số nguyên N từ bàn phím'''
l=[]
while True:
    n = input('số nguyên nhập vào: ')
    if (n.isalpha()==True):
        break
    else:
        l.append(int(n))
print(l)
