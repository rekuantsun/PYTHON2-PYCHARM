'''Bài 1: Viết chương trình thực hiện các yêu cầu sau:
- Nhập một chuỗi kí tự từ bàn phím
- Nhập tên tập tin từ bàn phím
- Lưu chuỗi ký tự ở trên vào tập tin.'''
cktu = input("Nhập 1 chuỗi: ")
ttt = input("Nhập tên tệp: ") + ".txt"
f=open(ttt,'w')
f.write(cktu)
f.close()