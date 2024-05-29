def tim_ro_so(bang_chu_cai, chuoi):
    for i in range(len(bang_chu_cai)):
        if bang_chu_cai[i] == chuoi:
            return i
    return -1

def tim_ma_chu(bang_chu_cai, chuoi, k):
    ma_chu = []
    for char in chuoi:
        ma_so = tim_ro_so(bang_chu_cai, char)
        if ma_so != -1:
            temp = (ma_so + k) % 26
            ma_chu.append(bang_chu_cai[temp])
        else:
            ma_chu.append(char)
    return ''.join(ma_chu)

def tim_giai_ma(bang_chu_cai, chuoi, k):
    giai_ma = []
    for char in chuoi:
        ma_so = tim_ro_so(bang_chu_cai, char)
        if ma_so != -1:
            ma_so -= k
            if ma_so < 0:
                ma_so = 26 + ma_so
            giai_ma.append(bang_chu_cai[ma_so])
        else:
            giai_ma.append(char)
    return ''.join(giai_ma)

bang_chu_cai = "abcdefghijklmnopqrstuvwxyz"

while True:
    print("1. Lập mã.")
    print("2. Giải mã.")
    print("0. Thoát.")
    chon = int(input("Chọn: "))

    if chon == 0:
        print("Kết thúc chương trình.")
        break

    chuoi = input("Nhập chuỗi: ").lower()
    k = int(input("Nhập khoá: "))

    if chon == 1:
        print("Chuỗi đã mã hóa:", tim_ma_chu(bang_chu_cai, chuoi, k))
    elif chon == 2:
        print("Chuỗi đã giải mã:", tim_giai_ma(bang_chu_cai, chuoi, k))
    else:
        print("Lựa chọn không hợp lệ. Vui lòng chọn lại.")
