from flask import Flask, render_template, request, redirect
from pymongo import MongoClient
from datetime import datetime

app = Flask(__name__)
app.static_folder = 'assets'
app.config['SECRET_KEY'] = 'secretkey'

client = MongoClient('localhost', 27017)

STANDARD_EXPIRY = 2

# Hiển thị trang about mặc định khi vào website
@app.route('/')
def index():
    return redirect('/about')

# Hiển thị trang about khi truy cập enpoint '/about'
@app.route('/about')
def about():
    global current_user
    return render_template('about.html')

# Hiển thị tất cả các deli trong database khi truy cập enpoint '/delis' theo coldelis hoặc hotdelis
@app.route('/delis', methods=['GET'])
def get_delis():
    cold_delis = [x for x in client.get_database('db').get_collection('colddelis').find()]
    hot_delis = [x for x in client.get_database('db').get_collection('hotdelis').find()]
    return render_template('delis.html', cold_delis = cold_delis, hot_delis = hot_delis)

if __name__ == '__main__':
    app.run()