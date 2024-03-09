from flask import Flask, render_template, request, redirect, flash
from pymongo import MongoClient
from db import *

app = Flask(__name__)
app.static_folder = 'assets'
app.config['SECRET_KEY'] = 'secretkey'
app.config['UPLOAD_FOLDER'] = 'upload'
client = MongoClient('localhost', 27017)

current_user = {}

STANDARD_EXPIRY = 2
STANDARD_DELIVERY_FEE = 2.0
# Tạo các deli theo đề bài 
all_delis = [{'code': 'C001', 'name': 'Smoked Duck Salad', 'price': 3.0, 'fat':12.5, 'carbohydydrate': 23.0,'protein': 15.0, 'styleOrTemp': '16','url': 'https://picniclifestyle.com/wp-content/uploads/2020/10/Grilled-pearsalad-6.jpg'},
{'code': 'C002', 'name': 'Strawberry Pudding', 'price': 2.0, 'fat': 0.3,'carbohydydrate': 10.0,'protein': 0.7, 'styleOrTemp': '3','url': 'https://veenaazmanov.com/wp-content/uploads/2014/05/Homemade-StrawberryPudding-15.jpg'},
{'code': 'C003', 'name': 'Chocolate Cake', 'price': 1.5, 'fat': 14.3,'carbohydydrate': 50.7,'protein': 5.0, 'styleOrTemp': '12','url': 'https://www.joannasteven.com/wp-content/uploads/2015/08/GFchocolatecake-1024x1024.jpg'},
{'code': 'C004', 'name': 'Smoked Salmon', 'price': 2.4, 'fat': 3.7,'carbohydydrate': 0.0,'protein': 16.0, 'styleOrTemp': '3','url': 'https://goodtastefoods.co.uk/wp-content/uploads/2019/11/smokedsalmon_143296537-1.jpg'},
{'code': 'C005', 'name': 'Chilled Papaya Smoothie', 'price': 2.2, 'fat': 2.1,'carbohydydrate': 21.3,'protein': 7.0, 'styleOrTemp': '8','url': 'https://insanelygoodrecipes.com/wp-content/uploads/2022/09/HealthyPapaya-Smoothie-with-Oat-Flakes-and-Cinnamon-683x1024.jpg'},
{'code': 'C006', 'name': 'Berry Yoghurt Surprise', 'price': 2.2, 'fat': 1.0,'carbohydydrate': 9.2,'protein': 3.0, 'styleOrTemp': '3','url': 'https://www.pcrm.org/sites/default/files/berries-nondairy-yogurt.jpg'},
{'code': 'C007', 'name': 'Beetroot Raita', 'price': 2.0, 'fat': 1.0,'carbohydydrate': 12.4,'protein': 3.5, 'styleOrTemp': '8','url': 'https://werecipes.com/app/uploads/2015/04/dahi-raita-beetroot-raitarecipe.jpg'},
{'code': 'H001', 'name': 'Croissant', 'price': 2.0, 'fat': 15.0,'carbohydydrate': 26.7,'protein': 4.6, 'styleOrTemp': 'Baking','url': 'https://3.bp.blogspot.com/-HMLcbz567qg/TlgWSbpD1uI/AAAAAAAACgM/1xnYGFTZemE/s1600/croissant.JPG'},
{'code': 'H002', 'name': 'Chicken Pie', 'price': 2.8, 'fat': 21.3,'carbohydydrate': 32.0,'protein': 10.0, 'styleOrTemp': 'Baking','url': 'https://img.taste.com.au/94eodL4O/taste/2016/11/creamy-chicken-andleek-pies-80359-1.jpeg'},
{'code': 'H003', 'name': 'Roast Beef', 'price': 3.5, 'fat': 21.8,'carbohydydrate': 0.0,'protein': 19.6, 'styleOrTemp': 'Roasting','url': 'https://i2.wp.com/www.domesticate-me.com/wp-content/uploads/2013/12/slowroasted-beef-tenderloin-with-rosemary-13.jpg'},
{'code': 'H004', 'name': 'Asparagus & Poached Egg', 'price': 3.0, 'fat': 4.9,'carbohydydrate': 3.1, 'protein': 7.9, 'styleOrTemp': 'Boiled','url': 'https://www.healthbenefitstimes.com/recipe/wpcontent/uploads/2018/07/Roasted-Asparagus-with-Poached-Eggs-and-HollandaiseRecipe.gif'},
{'code': 'H005', 'name': 'Apple Sesame Tart', 'price': 1.8, 'fat': 7.5,'carbohydydrate': 49.1,'protein': 4.9, 'styleOrTemp': 'Baking','url':'https://i.pinimg.com/736x/fc/22/c0/fc22c0106471cd2939ca371bfc80c38e.jpg'},
{'code': 'H006', 'name': 'Beef & Brown Rice Spicy Soup', 'price': 3.2, 'fat':6.35,'carbohydydrate': 17.7, 'protein': 18.0, 'styleOrTemp': 'Boiled','url':'https://i.pinimg.com/originals/f6/78/41/f678414dccf92a0af0a8f09e3572caa1.jpg'},
{'code': 'H007', 'name': 'Fish & Potato Pie', 'price': 3.0, 'fat': 5.5,'carbohydydrate': 15.0,'protein': 16.5, 'styleOrTemp': 'Baking','url': 'https://www.sprinklesandsprouts.com/wp-content/uploads/2019/10/Fish-Pie-4.jpg'},
{'code': 'H008', 'name': 'Banana Pancakes', 'price': 2.0, 'fat': 7.0,'carbohydydrate': 20.0,'protein': 3.6, 'styleOrTemp': 'Pan-Fried','url': 'https://3.bp.blogspot.com/-BTNuMoVzv3Y/Vkq1QEgta_I/AAAAAAAANdY/19_4zLnWfcc/s1600/Buttermilk%2BBanana%2BPancakes%2Brecipe.jpg'},
{'code': 'H009', 'name': 'Boiled Banana with Grated Coconut', 'price': 2.0, 'fat':2.2,'carbohydydrate': 30.7, 'protein': 2.0, 'styleOrTemp': 'Boiled','url': 'https://thumbs.dreamstime.com/b/boiled-slice-banana-eat-coconut-fooddiet-154458927.jpg'},
{'code': 'H010', 'name': 'Buckwheat Pancakes', 'price': 2.4, 'fat': 6.0,'carbohydydrate': 39.0,'protein': 7.0, 'styleOrTemp': 'Pan-Fried','url': 'https://bakeitpaleo.com/wp-content/uploads/2021/05/paleo-buckwheatpancake-recipe.jpg'},
{'code': 'H011', 'name': 'Chicken with Brown Rice', 'price': 3.0, 'fat': 5.8,'carbohydydrate': 48.3,'protein': 15.0, 'styleOrTemp': 'Steaming','url': 'https://dinnerthendessert.com/wp-content/uploads/2019/05/Baked-Chickenand-Rice.jpg'},
{'code': 'H012', 'name': 'Carrot & Coriander Soup', 'price': 2.0, 'fat': 2.6,'carbohydydrate': 13.8,'protein': 1.6, 'styleOrTemp': 'Boiled','url': 'https://i1.wp.com/cookingwithbry.com/wp-content/uploads/2019/11/CarotCoriander-Soup-Recipe-17.jpg'},
{'code': 'H013', 'name': 'Beancurd With Bean Sauce', 'price': 2.5, 'fat': 3.3,'carbohydydrate': 6.8,'protein': 10.2, 'styleOrTemp': 'Steaming','url': 'https://www.pekinghouse.co.nz/wp-content/uploads/2015/10/DeepFriedBeanCurdinChiliBeanSauce-600x600.jpg'}]

for deli in all_delis:
    create_deli(deli.get('code'), deli.get('name'), deli.get('price'), deli.get('fat'), deli.get('carbohydydrate'), deli.get('protein'), deli.get('styleOrTemp'), deli.get('url'))

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
    cold_delis = [x for x in db.get_collection(COLD_DELI_COLLECTION_NAME).find()]
    hot_delis = [x for x in db.get_collection(HOT_DELI_COLLECTION_NAME).find()]
    return render_template('delis.html', cold_delis = cold_delis, hot_delis = hot_delis, current_user = current_user)

# Hiển thị trang login khi truy cập endpoint '/login' với phương thức 'GET'
# Xử lý dữ liệu khi truy cập endpoint '/login' với phương thức 'POST', kiểm tra user có trong database không, nếu có kiểm tra password tương ứng
# Nếu đúng email và password chuyến đến trang delis, lưu thông tni user vào biến global current_user, nếu sai thông tin thì hiển thị thông báo bằng flash
@app.route('/login', methods=['GET', 'POST'])
def login():
    global current_user
    if request.method == 'POST':
        params = request.form
        user = db.get_collection(USER_COLLECTION_NAME).find_one({'email': params['email']})
        if user:
            if user['password'] == params['password']:
                current_user = user
                flash('Login successfully')
                cold_delis = [x for x in db.get_collection(COLD_DELI_COLLECTION_NAME).find()]
                hot_delis = [x for x in db.get_collection(HOT_DELI_COLLECTION_NAME).find()]
                return render_template('delis.html', cold_delis = cold_delis, hot_delis = hot_delis, current_user = current_user)
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
        if db.get_collection(USER_COLLECTION_NAME).find_one({'email': params['email']}):
            flash('User already exists, please login')
            return render_template('register.html', current_user = current_user)
        if not create_user(id= f"C{params['email'].upper()}", 
                           name = params['name'], 
                           email= params['email'],
                           password= params['password'],
                           dob =  params['dob'].replace('-', ''), 
                           handicapped = True if params['handicapped'] else False):
            flash('Something went wrong, please try again')
            return render_template('register.html', current_user = current_user)
        flash('User registered successfully')
        return render_template('login.html', current_user = current_user)
    if request.method == 'GET':
        return render_template('register.html', current_user = current_user)

# Xử lý dữ liệu khi truy cập endpoint '/logout' với phương thức 'POST'
# Nếu chưa đăng nhập, báo lỗi với flash và đưa về trang đăng nhập, nếu dăng nhập rồithì xoá dữ liệu trong biến current_user để đăng xuất, trả về trang about
@app.route('/logout', methods=['GET'])
def logout():
    global current_user
    if current_user:
        current_user = None
        flash("Logout successfully")
        return render_template('about.html', current_user = current_user)
    else:
        flash("Please login first")
        return render_template('login.html', current_user = current_user)

# Hiển thị trang createdeliset khi truy cập endpoint '/createdeliset' với phương thức 'GET'
# Xử lý dữ liệu khi truy cập endpoint '/createdeliset' với phương thức 'POST'
# Nếu tạo thành công, đưa đến trang orderdeliset, hiện thị báo bằng flash
# Nếu không tạo được, load lại trang, thông báo bằng flash
@app.route('/createdeliset', methods=['GET', 'POST'])
def createdeliset():
    global current_user
    if request.method == 'POST':
        params = request.form
        name = params['name']
        deliList = []
        for x in params:
            if x != "name":
                deliList.append(db.get_collection(DELI_COLLECTION_NAME).find_one({'deliCode': x}))
        if not create_deliset(name, deliList):
            flash('Deli set already exists or something went wrong, please try again')
            return render_template('createdeliset.html', current_user = current_user)
        return redirect('/delis')
    
    elif request.method == 'GET':
        if not current_user:
            return redirect('/login')
        else:
            all_delis = []
            for x in db.get_collection(DELI_COLLECTION_NAME).find():
                all_delis.append(x)
            return render_template('createdeliset.html', all_delis = all_delis, current_user = current_user)

# Hiển thị trang orderdeliset khi truy cập endpoint '/orderdeliset' với phương thức 'GET', nếu chău có deliset nào được tạo, hiển thị thông báo
@app.route('/orderdeliset', methods=['GET'])
def orderdeliset():
    global current_user
    if not current_user:
        return redirect('/login')
    else:
        all_delisets =  [x for x in db.get_collection(DELISET_COLLECTION_NAME).find()]
        if not all_delisets:
            return render_template('orderdeliset.html', current_user = current_user, noti = "No deli set yet. Please create a deli set first")
        else:
            for deliset in all_delisets:
                total_fat = 0.0
                total_price = 0.0
                total_calories = 0.0
                for deli in deliset['deliList']:
                    total_fat += float(deli['fat'])
                    total_price += float(deli['price'])
                    total_calories += float(deli['calories'])
                consume_in = min([float(x['expiryhours']) for x in deliset['deliList']])
                deliset['consume_in'] = consume_in
                deliset['total_fat'] = total_fat
                deliset['total_price'] = total_price
                deliset['total_calories'] = total_calories

            return render_template('orderdeliset.html', all_delisets = all_delisets, current_user = current_user)

# Xử lý dữ liệu khi truy cập endpoint '/createorderdeliset' với phương thức 'POST'
# Nếu chưa đăng nhập, đưa về trang đăng nhập
# Nếu chưa chọn thời gian vận chuyển, thông báo bằng flash
# Thông báo khi tạo đơn hàng thành công hay không, tạo thành công đưa đến trang vieworders
@app.route('/createorderdeliset', methods=['POST'])
def createorderdeliset():
    global current_user
    params = request.form
    name = params['name']
    datetimeDelivery = params['datetimeDelivery']
    if not current_user:
        flash('You need to login first')
        return redirect('/login')
    if not params['datetimeDelivery']:
        flash('Please enter datetime of delivery')
        return redirect('/orderdeliset')
    if not create_order(current_user, name, datetimeDelivery):
        flash('Something went wrong, please try again')
        return redirect('/orderdeliset')
    all_orders =  [x for x in db.get_collection(ORDER_COLLECTION_NAME).find()]
    return render_template('vieworders.html', current_user = current_user, all_orders = all_orders, noti = f"Order deliset {name} placed for {params['datetimeDelivery']}")

# Hiển thị trang vieworders khi truy cập endpoint '/vieworders' với phương thức 'GET'
@app.route('/vieworders', methods=['GET'])
def vieworders():
    global current_user
    if request.method == 'GET':
        if not current_user:
            flash('You need to login first')
            return redirect('/login')
        else:
            all_orders =  [x for x in db.get_collection(ORDER_COLLECTION_NAME).find({'participant': current_user})]
            if not all_orders:
                return render_template('vieworders.html', current_user = current_user, noti = "No order yet. Please place an order first")
            else:
                for order in all_orders:
                    total_fat = 0.0
                    total_price = 0.0
                    total_calories = 0.0
                    for deli in order['deliSet']['deliList']:
                        total_fat += float(deli['fat'])
                        total_price += float(deli['price'])
                        total_calories += float(deli['calories'])
                    consume_in = min([float(x['expiryhours']) for x in order['deliSet']['deliList']])
                    order['consume_in'] = consume_in
                    order['total_fat'] = total_fat
                    order['total_price_deliset'] = total_price
                    order['total_calories'] = total_calories
                    if current_user['handicapped']:
                        order['delivery_fee'] = 0.0
                    else:
                        order['delivery_fee'] = STANDARD_DELIVERY_FEE
                    order['total_price'] = order['total_price_deliset'] + order['delivery_fee']
                return render_template('vieworders.html', all_orders = all_orders, current_user = current_user)

# Xử lý dữ liệu khi truy cập endpoint '/upload' với phương thức 'GET'
# Nếu chưa đăng nhập, trả về trang đăng nhập
@app.route('/upload', methods=['GET', 'POST'])
def upload():
    global current_user
    if not current_user or current_user['name'] != 'Admin':
        flash('You need to login by admin first')
        return render_template('login.html', current_user = current_user)
    if request.method == 'POST':
        type = request.form['datatype']
        path = request.form['path']
        with open(f"upload/{path}", 'r') as f:
            data = f.readlines()
        # Nếu kiểu upload là 'participant', tạo user với từng dòng dữ liệu trong file
        if type == 'participant':
            for line in data:
                params = line.split(',')
                if not create_user(
                    id = params[0],
                    name = params[1],
                    email = params[4].strip(),
                    password = "12345",
                    dob= params[2],
                    handicapped = bool(params[3])
                ):
                    flash(f'Participant with email {params[4].strip()} already exists')
                else:
                    flash(f'create participant {params[1]} successfully')
        # Nếu kiểu upload là 'deli', tạo deli với các dữ liệu trong file
        elif type == 'deli':
            for line in data:
                params = line.split(',')
                if create_deli(
                    deliCode= params[0],
                    name = params[1],
                    price = float(params[2]),
                    fat = float(params[3]),
                    carbonhydrate = float(params[4]),
                    protein = float(params[5]),
                    styleOrTemp = params[6],
                    url = params[7]
                ):
                    flash(f'Deli {params[0]} already exists!')
                else:
                    flash(f'create deli {params[1]} failed')
        # Nếu kiểu upload là 'order', tạo order với các dữ liệu trong file
        elif type == 'order':
            for line in data:
                params = line.split(',')
                deliset = db.get_collection('deliSets').find_one({'name': params[2]})
                if not deliset:
                    if len(params) == 3:
                        create_deliset(name=params[2], deliList=[])
                    else:
                        codes = [x.strip()  for x in params[3:]]
                        delilist = []
                        for code in codes:
                            print(code)
                            deli = db.get_collection(DELI_COLLECTION_NAME).find_one({'deliCode': code})
                            delilist.append(deli)
                        deliset = create_deliset(name=params[2], deliList=delilist)
                participant = db.get_collection('users').find_one({'email': params[0]})
                if not participant:
                    flash(f'Participant with email someEmail has not registered!')
                    continue
                deliveryDatetime = params[1]
                if not create_order(participant, deliset, deliveryDatetime):
                    flash(f'Create order deliset with name {params[2]} failed ')
                else:
                    flash(f'Create order deliset with name {params[2]} successfully')
        return redirect('/upload')

    return render_template('upload.html', current_user = current_user)

if __name__ == '__main__':
    app.run()