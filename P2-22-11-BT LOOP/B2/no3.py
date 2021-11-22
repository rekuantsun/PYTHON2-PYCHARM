'''Bài 3: Viết chương trình thực hiện các yêu cầu sau:
- Nhập vào từ bàn phím một chuỗi các giá trị (có thể là số nguyên, số thực hay các ký tự)
cách nhau bởi dấu phẩy (“,”).
- Chuyển chuỗi được nhập từ bàn phím thành một tuple
- Hiển thị tuple đó ra màn hình.'''
l= 'a,b,c,2,3,4,5.4,6.1'
l=l.split(',')
t=tuple(l)
print(t)