'''Bài 4: Viết chương trình thực hiện các yêu cầu sau:
- Đọc tập tin ở bài 3 và ghi kết quả ra màn hình'''
f = open('P2-file.txt', 'r')
a = f.read()
print(a)
f.close()