a = input("Nhập vào số n:")

try:
    b = int(a)
    c = 10/b
    print(c)
except ValueError:
    print("lỗi không chuyển được sang int được")