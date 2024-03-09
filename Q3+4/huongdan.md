# Endpoints:

/: chuyển về /about
/about: hiển thị trang giới thiệu
/delis: hiển thị tất cả các deli, chia làm 2 phần Cold Deli và Hot Deli
/login: hiển thị trang đăng nhập, kiểm tra thông tin đăng nhập
/logout: thực hiện thao tác đăng xuất
/register: hiển thị trang đăng kí, thực hiện đăng kí tài khoản
/orderdeliset: hiển thị trang tạo Deli Set
/createorderdeliset: thực hiện tạo Deli Set mới theo người dùng
/vieworders: hiển thị các order do người dùng hiện tại đặt
/upload: tạo nhiều tài khoản, deli, deli set theo file .txt trong thư mục upload

# Các công thức dùng trong dự án:

## Deli
Calories = fat * 9 + carbonhydrate * 4 + protein * 4

## Deliset
Price = tổng price các deli trong deliList của deliset
Calories = tổng Calories các deli trong deliList của deliset
Consume in = min của các expiryhours trong deliList của deliset

## Order
Price = tổng price các deli trong deliList của order
Calories = tổng Calories các deli trong deliList của order
Fat = tổng Fat các deli trong deliList của order
Delivery fee = 0.0 nếu tài khoản là tài khoản Handicapped
Consume in = min của các expiryhours trong deliList của order
Total_price = Price + Delivery fee


