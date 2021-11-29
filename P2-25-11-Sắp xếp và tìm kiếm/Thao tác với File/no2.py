'''Bài 2: Viết chương trình thực hiện các yêu cầu sau:
- Nhập tên tập tin từ bàn phím
- Đọc nội dung tập tin và in ra màn hình'''
ttt=input('Tên tập tin: ')+'.txt'
with open(ttt,'r') as f:
    nd=f.read()
print(nd)