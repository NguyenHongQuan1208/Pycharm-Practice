import re
def nhap_email():
    email_hop_le = False
    while not email_hop_le:
        email = input("Nhập địa chỉ email: ")

        pattern = re.compile(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$')
        if pattern.match(email):
            email_hop_le = True  # Đặt cờ thành True để kết thúc vòng lặp
        else:
            print("Địa chỉ email không hợp lệ. Vui lòng thử lại.")
    return email

email_hop_le = nhap_email()
print("Địa chỉ email đã nhập là:", email_hop_le)
