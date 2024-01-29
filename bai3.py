import random

def sinh_so_ngau_nhien():
    return random.randint(1, 6)

def nhap_so_tu_1_den_6():
    while True:
        try:
            so_nguoi_dung = int(input("Nhập một số từ 1 đến 6: "))
            if 1 <= so_nguoi_dung <= 6:
                return so_nguoi_dung
            else:
                print("Vui lòng nhập số trong khoảng từ 1 đến 6. Thử lại.")
        except ValueError:
            print("Vui lòng nhập vào một giá trị số nguyên. Thử lại.")

def so_sanh_so_ngau_nhien_va_so_nguoi_dung(so_ngau_nhien, so_nguoi_dung):
    return so_ngau_nhien == so_nguoi_dung

def main():
    so_lan_doan_dung = 0

    for i in range(3):  # Cho phép người dùng đoán 3 lần
        so_ngau_nhien = sinh_so_ngau_nhien()
        so_nguoi_dung = nhap_so_tu_1_den_6()

        if so_sanh_so_ngau_nhien_va_so_nguoi_dung(so_ngau_nhien, so_nguoi_dung):
            print("Bạn đã đoán đúng!")
            so_lan_doan_dung += 1
        else:
            print(f"Bạn đã đoán sai. Số ngẫu nhiên là: {so_ngau_nhien}")

    print(f"Số lần đoán đúng của bạn là: {so_lan_doan_dung}")

if __name__ == "__main__":
    main()
