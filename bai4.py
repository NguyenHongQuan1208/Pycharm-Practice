class TaiKhoan:
    def __init__(self, so_tai_khoan, so_du=0):
        self.so_tai_khoan = so_tai_khoan
        self.so_du = so_du
        self.lich_su_giao_dich = []

    def gui_tien(self, so_tien):
        self.so_du += so_tien
        self.lich_su_giao_dich.append(f'Gửi tiền: +{so_tien}')

    def rut_tien(self, so_tien):
        if so_tien <= self.so_du:
            self.so_du -= so_tien
            self.lich_su_giao_dich.append(f'Rút tiền: -{so_tien}')
        else:
            print("Số dư không đủ.")

    def xem_so_du(self):
        print(f"Số dư trong tài khoản {self.so_tai_khoan}: {self.so_du}")

    def xem_lich_su_giao_dich(self):
        print(f"Lịch sử giao dịch của tài khoản {self.so_tai_khoan}:")
        for giao_dich in self.lich_su_giao_dich:
            print(giao_dich)

def main():
    so_tai_khoan = input("Nhập số tài khoản của bạn: ")
    tai_khoan = TaiKhoan(so_tai_khoan)

    while True:
        print("\n====== MENU CHÍNH ======")
        print("a. Rút tiền")
        print("b. Gửi tiền")
        print("c. Xem số dư")
        print("d. Xem lịch sử giao dịch")
        print("e. Quay về")

        lua_chon_chinh = input("Nhập lựa chọn của bạn: ")

        if lua_chon_chinh == 'a':
            so_tien_rut = float(input("Nhập số tiền bạn muốn rút: "))
            tai_khoan.rut_tien(so_tien_rut)
        elif lua_chon_chinh == 'b':
            so_tien_gui = float(input("Nhập số tiền bạn muốn gửi: "))
            tai_khoan.gui_tien(so_tien_gui)
        elif lua_chon_chinh == 'c':
            tai_khoan.xem_so_du()
        elif lua_chon_chinh == 'd':
            tai_khoan.xem_lich_su_giao_dich()
        elif lua_chon_chinh == 'e':
            print("Cảm ơn bạn đã sử dụng dịch vụ ATM. Tạm biệt!")
            break
        else:
            print("Lựa chọn không hợp lệ. Vui lòng thử lại.")

if __name__ == "__main__":
    main()
