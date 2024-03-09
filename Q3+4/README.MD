# 3
Learning objectives:
• Apply programming methods to present information in HTML
• Employ web programming framework for developing website
This question focuses on the non-admin set functions: create delisets, order deliset and view
orders. For this question, you must define the DeliSet and Order classes in Figure Q2(b). Ensure
that the User class has been defined according to the class diagram in Figure Q2(b).
(a) Create DeliSet
The participant provides a name for the new deli set to be created. He can select
the delis he wishes to add, and then click on the button to add the delis to the set.
Figure Q3(a)(i) shows the top of the page for Create DeliSet and Figure Q3(a)(ii)
shows the bottom of the page.
Figure Q3(a) (i) Top of Create DeliSet page with provided input
Figure Q3(a) (ii) Bottom of Create DeliSet page with provided input
The price of the deli set is the sum of each selected deli. The total fats and total
calories are similarly computed. The consume in hours for a deli set is the minimum
of the expiryHours attribute of delis in the deli set. The name of a deli set must
have a different name from the names of a participant’s existing deli sets. Provide
the necessary instruction as shown in Figure Q3(a) (iii).
Figure Q3(a) (iii) Create DeliSet page with instruction
Flash appropriate messages such as
• Please use a different deli set name
Deli set name checks are case-insensitive. Therefore, My FAV lunch is
considered same as My Fav Lunch.
• Please select at least one deli
A deli set must have at least one selected Deli which is added to a newly
created deli set. Subsequent selected delis should be added one at a time to
the newly-created deli set.
• Deli set inputName created with the selected delis: deliCode1, …,
delicoden
The message is flashed if the deliset is successfully created and added to
the dictionary of deli sets for the participant. Use the deli set name as key
and Deliset object as value.
Flash the appropriate message when the button is clicked, and return to the same
page. An example is shown in Figure Q3(a) (iv).
Figure Q3(a) (iv) Create DeliSet page with flashed message
(b)
(i) Order DeliSet
When a participant has not created a deli set, he cannot place any order. Therefore,
clicking on the hyperlink Order DeliSet shows a page as shown in Figure Q3(b) (i).
Figure Q3(b) (i) Order DeliSet page when participant has no deli set
If the participant has created deli sets, they are listed in alphabetical order, case
insensitive. The participant provides a delivery datetime for a selected deli set and
click on the corresponding button to place order.
Check that the same deli set must not have been ordered yet to be delivered at the
same time. Flash an appropriate message when the button is clicked, and return to
the same page. The two appropriate messages are as follows:
• Order deliset delisetName placed for deliveryDateTime
• Order failed. Deliset delisetName has already been placed for
deliveryDateTime
An example is shown in Figure Q3(b) (ii).
Figure Q3(b) (ii) Order DeliSet page with flashed message
(ii) View Orders
When a participant has not placed any order, clicking on the hyperlink Order
DeliSet shows a page as shown in Figure Q3(b) (iii).
Figure Q3(b) (iii) View Order page when participant has no order
If the participant has placed some orders, they are listed in chronological order,
starting from the later datetime, shown in Figure Q3b(iv). Delivery charge is
waived for participants who are at least 75 years of age on the year the order is
made or are handicapped at the time of order.

Mục tiêu học tập:
• Áp dụng các phương pháp lập trình để trình bày thông tin dưới dạng HTML
• Sử dụng framework lập trình web để phát triển website
Câu hỏi này tập trung vào các chức năng không phải của quản trị viên: tạo deliset, deliset thứ tự và xem
đơn đặt hàng. Đối với câu hỏi này, bạn phải xác định các lớp DeliSet và Order trong Hình Q2(b). Đảm bảo
rằng lớp Người dùng đã được xác định theo sơ đồ lớp trong Hình Q2(b).
(a) Tạo DeliSet
Người tham gia cung cấp tên cho set đồ nguội mới sẽ được tạo. Anh ấy có thể chọn
món ăn ngon mà anh ấy muốn thêm, sau đó nhấp vào nút để thêm món ăn ngon vào bộ.
Hình Q3(a)(i) hiển thị phần đầu của trang Tạo DeliSet và Hình Q3(a)(ii)
hiển thị phần dưới cùng của trang.
Hình Q3(a) (i) Đầu trang Tạo DeliSet với thông tin đầu vào được cung cấp
Hình Q3(a) (ii) Cuối trang Tạo DeliSet với thông tin đầu vào được cung cấp
Giá của set đồ nguội là tổng của mỗi món đồ nguội đã chọn. Tổng lượng chất béo và tổng số
lượng calo được tính toán tương tự. Mức tiêu thụ tính bằng giờ cho một set đồ nguội là tối thiểu
thuộc tính ExpirationHours của đồ nguội trong tập hợp đồ nguội. Tên của một set đồ nguội phải
có tên khác với tên của các set đồ nguội hiện có của người tham gia. Cung cấp
hướng dẫn cần thiết như trong Hình Q3(a) (iii).
Hình Q3(a) (iii) Tạo trang DeliSet kèm theo hướng dẫn
Flash các tin nhắn thích hợp như
• Vui lòng sử dụng tên set đồ nguội khác
Việc kiểm tra tên set đồ nguội không phân biệt chữ hoa chữ thường. Vì vậy, bữa trưa FAV của tôi là
được coi giống như Bữa trưa yêu thích của tôi.
• Vui lòng chọn ít nhất một món ăn ngon
Một set đồ nguội phải có ít nhất một món đồ nguội đã chọn được thêm vào một món mới
đã tạo ra bộ đồ nguội. Các món ăn ngon được chọn tiếp theo sẽ được thêm lần lượt vào
bộ đồ nguội mới được tạo.
• Deli set inputName được tạo với deliCode1, …,
decodeden
Thông báo sẽ nhấp nháy nếu quá trình xóa được tạo và thêm thành công vào
từ điển các bộ đồ nguội dành cho người tham gia. Sử dụng tên set deli làm chìa khóa
và đối tượng Deliset làm giá trị.
Nhấp nháy thông báo thích hợp khi nhấp vào nút và quay lại thông báo tương tự
trang. Một ví dụ được thể hiện trong Hình Q3(a) (iv).
Hình Q3(a) (iv) Tạo trang DeliSet với thông báo nhấp nháy
(b)
(i) Đặt món DeliSet
Khi người tham gia chưa tạo set đồ nguội, anh ta không thể đặt bất kỳ đơn hàng nào. Vì thế,
nhấp vào siêu liên kết Order DeliSet sẽ hiển thị một trang như trong Hình Q3(b) (i).
Hình Q3(b) (i) Đặt trang DeliSet khi người tham gia không có set đồ nguội
Nếu người tham gia đã tạo các set đồ nguội, chúng sẽ được liệt kê theo thứ tự bảng chữ cái, viết hoa
vô cảm. Người tham gia cung cấp ngày giờ giao hàng cho một set đồ nguội đã chọn và
bấm vào nút tương ứng để đặt hàng.
Kiểm tra để đảm bảo rằng set đồ nguội tương tự chưa được đặt hàng và được giao tại
cùng một lúc. Nhấp nháy một thông báo thích hợp khi nhấp vào nút và quay lại
cùng một trang. Hai tin nhắn thích hợp như sau:
• Đặt hàng deliset delisetName đã đặt để giao hàngNgày giờ
• Đặt hàng không thành công. Deliset delisetName đã được đặt cho
ngày giao hàngthời gian
Một ví dụ được thể hiện trong Hình Q3(b) (ii).
Hình Q3(b) (ii) Trang Đặt hàng DeliSet với thông báo nhấp nháy
(ii) Xem đơn hàng
Khi người tham gia chưa đặt bất kỳ đơn hàng nào, hãy nhấp vào siêu liên kết Đặt hàng
DeliSet hiển thị một trang như trong Hình Q3(b) (iii).
Hình Q3(b) (iii) Xem trang Đặt hàng khi người tham gia không có đơn hàng
Nếu người tham gia đã đặt một số đơn hàng, chúng sẽ được liệt kê theo thứ tự thời gian,
bắt đầu từ ngày giờ sau đó, được hiển thị trong Hình Q3b(iv). Phí giao hàng là
miễn trừ cho những người tham gia ít nhất 75 tuổi vào năm lệnh được thực hiện
được thực hiện hoặc bị khuyết tật tại thời điểm đặt hàng.

# 4
Learning objectives:
• Employ web programming framework for developing website
Figure Q4 (i) shows the Upload page. The Upload function is available to only the admin user.
To access the function, the admin user must log in. The Deli page will show up, and then, he
must click on the Upload link on the sidebar. Note that the admin user need not register himself.
Figure Q4 (i) Upload Page
Once a data type and a file are chosen, the admin user clicks on Upload to activate the upload
of data to the backend to be stored in Mongodb.
Data type Fields, example and messages
Participant ID,name,dob,handicapped,email
S4428006Z,Tan Yan Meng,19480708,False,tanym@gmail.com
Flash message when a participant’s email is already in database:
• Participant with email someEmail already exists
Deli
#cold deli
deliCode,name,price,fat,carbohydrates,protein,storageTemperature,url
C001,Smoked Duck Salad,3.0,12.5,23,15,16,https://picniclifestyle.com/wpcontent/uploads/2020/10/Grilled-pear-salad-6.jpg
#hot deli
deliCode,name,price,fat,carbohydrates,protein,cookingStyle,url
H001,Croissant,2.0,15,26.7,4.6,Baking,https://3.bp.blogspot.com/-
HMLcbz567qg/TlgWSbpD1uI/AAAAAAAACgM/1xnYGFTZemE/s1600/croissant.JPG
Flash message when a delicode is already in database:
• Deli someDeliCode already exists!
Order
#Order
email,deliveryDateTime,name,deliList
wongyh@gmail.com,2024-01-04 09:00,My Breakfast,H001,C001,H008
peter@gmail.com,2024-01-04 09:00,My fav lunch
Flash messages:
• Participant with email someEmail has not registered!
when participant in data line with email not registered in the application.SINGAPORE UNIVERSITY OF SOCIAL SCIENCES (SUSS) TMA – Page 15 of 19
• Order for same deliset someDeliSetName, delivery datetime
someDeliveryDateTime by participant with email someEmail already
exists
when the data line is for an existing order, that is, for the same participant,
the same deli set and the same delivery time.
• deliset someDeliSetName does not exist and cannot be created without
delicode
when a deli set does not exist yet and there is no deli code in the data line.
Note that if the data line contains deli code, then a deli set can be created
for a participant, and an order is then placed.
However, if a deli set already exists for a participant, it is not necessary for
a data line to list the deli codes in the deli set. If there are deli codes are in
the data line for an existing deli set, the deli codes are ignored. That is,
there is no need to update the existing deli set with the deli codes in the
data line.
Flash the number of records created at the end of each file upload. Refer to Figure Q4 (ii) for
an example.
Figure Q4 (ii) Upload Page after an upload
Extend the flask application to allow admin user to upload data as described.

Mục tiêu học tập:
• Sử dụng framework lập trình web để phát triển website
Hình Q4 (i) hiển thị trang Tải lên. Chức năng Tải lên chỉ khả dụng cho người dùng quản trị.
Để truy cập chức năng, người dùng quản trị phải đăng nhập. Trang Deli sẽ hiển thị, sau đó anh ta
phải nhấp vào liên kết Tải lên trên thanh bên. Lưu ý rằng người dùng quản trị không cần phải tự đăng ký.
Hình Q4 (i) Trang tải lên
Khi loại dữ liệu và tệp được chọn, người dùng quản trị viên nhấp vào Tải lên để kích hoạt tải lên
dữ liệu vào phần phụ trợ sẽ được lưu trữ trong Mongodb.
Kiểu dữ liệu Trường, ví dụ và thông báo
ID người tham gia, tên, dob, người khuyết tật, email
S4428006Z,Tanym Meng,19480708,False,tanym@gmail.com
Thông báo flash khi email của người tham gia đã có trong cơ sở dữ liệu:
• Người tham gia có email someEmail đã tồn tại
đồ nguội
#đồ nguội
deliCode,tên,giá,chất béo,tinh bột,protein,nhiệt độ bảo quản,url
C001,Gỏi vịt hun khói,3.0,12.5,23,15,16,https://picniclifestyle.com/wpcontent/uploads/2020/10/Grilled-pear-salad-6.jpg
#đồ ăn nóng
deliCode,tên,giá,chất béo,tinh bột,protein,kiểu nấu ăn,url
H001,Bánh sừng bò,2.0,15,26.7,4.6,Làm bánh,https://3.bp.blogspot.com/-
HMLcbz567qg/TlgWSbpD1uI/AAAAAAAACgM/1xnYGFTZemE/s1600/croissant.JPG
Thông báo flash khi delicode đã có trong cơ sở dữ liệu:
• Deli someDeliCode đã tồn tại!
Đặt hàng
#Đặt hàng
email,ngày giao hàng,thời gian,tên,deliList
wongyh@gmail.com,2024-01-04 09:00,Bữa sáng của tôi,H001,C001,H008
peter@gmail.com,2024-01-04 09:00,Bữa trưa yêu thích của tôi
Tin nhắn flash:
• Người tham gia có email someEmail chưa đăng ký!
khi người tham gia vào dòng dữ liệu có email chưa được đăng ký trong ứng dụng.
• Đặt hàng cho cùng một món ăn deliset someDeliSetName, ngày giao hàng
someDeliveryDateTime bởi người tham gia có email someEmail rồi
tồn tại
khi dòng dữ liệu dành cho một đơn hàng hiện có, nghĩa là dành cho cùng một người tham gia,
cùng một suất đồ nguội và cùng thời gian giao hàng.
• xóa someDeliSetName không tồn tại và không thể được tạo nếu không có
giải mã
khi bộ đồ nguội chưa tồn tại và không có mã đồ nguội trong dòng dữ liệu.
Lưu ý rằng nếu dòng dữ liệu chứa mã đồ nguội thì có thể tạo một bộ đồ nguội
cho một người tham gia, và sau đó một đơn đặt hàng sẽ được đặt.
Tuy nhiên, nếu đã có sẵn set đồ ăn ngon dành cho người tham gia thì không cần thiết phải
một dòng dữ liệu để liệt kê các mã đồ nguội trong bộ đồ nguội. Nếu có mã đồ nguội trong
dòng dữ liệu cho một bộ đồ nguội hiện có, mã đồ nguội sẽ bị bỏ qua. Đó là,
không cần phải cập nhật bộ đồ nguội hiện có với mã đồ nguội trong
dòng dữ liệu.
Flash số lượng bản ghi được tạo ở cuối mỗi lần tải lên tệp. Tham khảo Hình Q4 (ii) để biết
một ví dụ.
Hình Q4 (ii) Trang tải lên sau khi tải lên
Mở rộng ứng dụng bình để cho phép người dùng quản trị tải lên dữ liệu như mô tả.