'''Bài 4: Viết chương trình thực hiện các yêu cầu sau:
- Đọc tập tin ở bài 3 và ghi kết quả ra màn hình'''
with open('P2-file.txt') as f:
    rf=f.read()
print(rf)