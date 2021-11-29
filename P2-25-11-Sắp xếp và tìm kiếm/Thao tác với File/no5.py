'''Bài 5: Viết chương trình thực các yêu cầu sau:
- Sinh ngẫu nhiên 1 danh sách gồm 1000 số nguyên trong khoảng từ [-1000, 1000]
- Nhập tên tập tin từ bàn phím
- Ghi danh sách trên vào tập tin theo quy tắc:
o 10 số trên một hàng
o Các số phân tách nhau bởi dấu phẩy (,)
- Đọc nội dung tập tin ở trên và in ra màn hình theo quy tắc:
o 10 số trên một hàng
o Các số phan tách nhau bởi dấu tab.'''

def danhsach():
    import random
    l=[]
    for i in range(1000):
        l.append(random.randint(-1000,1000))
    return l

def ghids(ttt):
    write open(ttt,'a+') as f:



