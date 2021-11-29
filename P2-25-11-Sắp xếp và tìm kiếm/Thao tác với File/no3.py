'''Bài 3: Viết chương trình thực hiện các yêu cầu sau:
- Nhập tên tập tin từ bàn phím
- Nhập một chuỗi kí tự vào từ bàn phím
- Ghi chuỗi kí tự này vào cuối tập tin ở trên'''
ttt=input("Tên tập tin: ")+'.txt'
cktu=input("Chuỗi ký tự: ")
f = open(ttt, 'a',)
f.write(cktu)
f.close()
