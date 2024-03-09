Register, Login and Logout
Refer to Figure 2(c) (i) and (ii) for the user interfaces for Register and Login
respectively. For this question part, you will need to define the User class in Figure
Q2(b).SINGAPORE UNIVERSITY OF SOCIAL SCIENCES (SUSS) TMA – Page 9 of 19
Create the admin user (email: admin@abc.com, password 12345 and name Admin)
if the user collection is empty. You can create the admin user either via Compass
or through some application code. There is no need to include other details for
admin user such as ID dob, handicapped and deli sets.
Similar to the Staycation case study, a participant (non-admin user) needs to be
authenticated before he can use certain functions of the application. Therefore, he
must register for an account. Upon successful registration, he will be directed to a
login page with a flashed message displayed using Bootstrap alert as shown in
Figure 2(c) (iii).
Handle unsuccessful registration and login in the same manner as the Staycation
case study. Any user who successfully logs in will be directed to the Deli page.
To exit from the application, the user selects log out. After a user has logged out,
the application should display the About page. The log out functionality is available
on the top panel only after a successful login as shown in Figure Q2c (iv).
You may copy the relevant code in the Staycation case study for the register, login
and logout functions to your application and make changes to achieve the new
effects. Explain your modification.
Register a participant (email peter@gmail.com, password 12345, name Peter Oh,
ID S1234567C, dob 1 Jun 1950, handicapped) and test that your functions are
working correctly.

Đăng ký, đăng nhập và đăng xuất
Tham khảo Hình 2(c) (i) và (ii) để biết giao diện người dùng dành cho Đăng ký và Đăng nhập
tương ứng. Đối với phần câu hỏi này, bạn sẽ cần định nghĩa lớp Người dùng trong Hình
Q2(b).ĐẠI HỌC KHOA HỌC XÃ HỘI SINGAPORE (SUSS) TMA – Trang 9/19
Tạo người dùng quản trị (email: admin@abc.com, mật khẩu 12345 và tên Admin)
nếu bộ sưu tập người dùng trống. Bạn có thể tạo người dùng quản trị viên thông qua La bàn
hoặc thông qua một số mã ứng dụng. Không cần phải bao gồm các chi tiết khác cho
người dùng quản trị viên như ID dob, bộ dành cho người khuyết tật và đồ nguội.
Tương tự như nghiên cứu điển hình Staycation, người tham gia (người dùng không phải quản trị viên) cần phải
được xác thực trước khi anh ta có thể sử dụng một số chức năng nhất định của ứng dụng. Vì vậy, anh ấy
phải đăng ký tài khoản. Sau khi đăng ký thành công, anh ta sẽ được chuyển đến một
trang đăng nhập với một thông báo nhấp nháy được hiển thị bằng cảnh báo Bootstrap như trong
Hình 2(c) (iii).
Xử lý việc đăng ký và đăng nhập không thành công tương tự như Staycation
nghiên cứu trường hợp. Bất kỳ người dùng nào đăng nhập thành công sẽ được chuyển đến trang Deli.
Để thoát khỏi ứng dụng, người dùng chọn đăng xuất. Sau khi người dùng đã đăng xuất,
ứng dụng sẽ hiển thị trang Giới thiệu. Chức năng đăng xuất có sẵn
chỉ trên bảng trên cùng sau khi đăng nhập thành công như trong Hình Q2c (iv).
Bạn có thể sao chép mã có liên quan trong nghiên cứu điển hình Staycation để đăng ký, đăng nhập
và chức năng đăng xuất khỏi ứng dụng của bạn và thực hiện các thay đổi để đạt được mục tiêu mới
các hiệu ứng. Giải thích sự sửa đổi của bạn.
Đăng ký người tham gia (email peter@gmail.com, mật khẩu 12345, tên Peter Oh,
ID S1234567C, dob ngày 1 tháng 6 năm 1950, người khuyết tật) và kiểm tra xem chức năng của bạn có phù hợp không
hoạt động chính xác