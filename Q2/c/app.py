from flask import Flask, render_template, request, redirect, flash
from pymongo import MongoClient
from datetime import datetime

app = Flask(__name__)
app.static_folder = 'assets'
app.config['SECRET_KEY'] = 'secretkey'

client = MongoClient('localhost', 27017)

current_user = {}

STANDARD_EXPIRY = 2

# Đưa đến enpoint '/about' mặc định khi vào website
@app.route('/')
def index():
    global current_user

    return redirect('/about')

# Hiển thị trang about khi truy cập endpoint '/about'
@app.route('/about')
def about():
    global current_user
    return render_template('about.html', current_user = current_user)

# Hiển thị tất cả các deli trong database khi truy cập endpoint '/delis'
@app.route('/delis', methods=['GET'])
def get_delis():
    global current_user
    cold_delis = [x for x in client.get_database('db').get_collection('colddelis').find()]
    hot_delis = [x for x in client.get_database('db').get_collection('hotdelis').find()]
    return render_template('delis.html', cold_delis = cold_delis, hot_delis = hot_delis, current_user = current_user)

# Hiển thị trang login khi truy cập endpoint '/login' với phương thức 'GET'
# Xử lý dữ liệu khi truy cập endpoint '/login' với phương thức 'POST', kiểm tra user có trong database không, nếu có kiểm tra password tương ứng
# Nếu đúng email và password chuyến đến trang delis, lưu thông tni user vào biến global current_user, nếu sai thông tin thì hiển thị thông báo bằng flash
@app.route('/login', methods=['GET', 'POST'])
def login():
    global current_user
    if request.method == 'POST':
        params = request.form
        user = client.get_database('db').get_collection('users').find_one({'email': params['email']})
        if user:
            if user['password'] == params['password']:
                current_user = user
                return render_template('delis.html', current_user = current_user)
            else:
                flash('Wrong password, please try again')
                return render_template('login.html',current_user = current_user)
        else:
            flash('User with email is not exist, please try again')
            return render_template('login.html', current_user = current_user)
        
    if request.method == 'GET':
        return render_template('login.html', current_user = current_user)

# Hiển thị trang register khi truy cập endpoint '/register' với phương thức 'GET'
# Xử lý dữ liệu khi truy cập endpoint '/register' với phương thức 'POST', kiểm tra user có trong database không
# Nếu email đăng kí chưa có trong database thì tạo user mới, đưa về trang login, hiển thị thông báo từng trường hợp bằng flash
@app.route('/register', methods=['GET', 'POST'])
def register():
    global current_user
    if request.method == 'POST':
        params = request.form
        if client.get_database('db').get_collection('users').find_one({'email': params['email']}):
            flash('User already exists, please login')
            return render_template('register.html', current_user = current_user)
        client.get_database('db').get_collection('users').insert_one(params.to_dict())
        flash('User registered successfully')
        return render_template('login.html', current_user = current_user)
    if request.method == 'GET':
        return render_template('register.html', current_user = current_user)

# Xử lý dữ liệu khi truy cập endpoint '/logout' với phương thức 'POST'
# Nếu chưa đăng nhập, báo lỗi với flash và đưa về trang đăng nhập, nếu dăng nhập rồithì xoá dữ liệu trong biến current_user để đăng xuất, trả về trang about
@app.route('/logout', methods=['POST'])
def logout():
    global current_user
    if current_user:
        current_user = None
        flash("Logout successfully")
        return render_template('about.html', current_user = current_user)
    else:
        flash("Please login first")
        return render_template('login.html', current_user = current_user)

if __name__ == '__main__':
    app.run()