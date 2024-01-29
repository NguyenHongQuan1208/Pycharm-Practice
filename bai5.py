import pandas as pd

def thong_ke_ho(file_path):
    try:
        # Đọc dữ liệu từ file CSV và tạo DataFrame
        df = pd.read_csv(file_path)

        # Chuyển họ về dạng chuỗi chuẩn để đếm
        df['lname'] = df['lname'].str.strip().str.capitalize()

        # Thống kê số lần xuất hiện của mỗi họ
        thong_ke_ho = df['lname'].value_counts()

        # In thống kê
        print("Thống kê số lần xuất hiện của mỗi họ:")
        print(thong_ke_ho)

    except FileNotFoundError:
        print("Không tìm thấy file.")

# Thực hiện thống kê từ file CSV trong thư mục con "csv"
thong_ke_ho('csv/gradedata.csv')
