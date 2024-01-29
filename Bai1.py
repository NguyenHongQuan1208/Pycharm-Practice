def enterPositiveNumber():
    while True:
        try:
            number = float(input("Nhập vào một số dương: "))
            if number >= 0:
                return number
            else:
                print("Vui lòng nhập vào một số dương. Thử lại.")
        except ValueError:
            print("Vui lòng nhập vào một giá trị số. Thử lại.")

so_duong = enterPositiveNumber()

# In ra số dương đã nhập
print("Số dương đã nhập là:", so_duong)
