from flask import Flask, render_template, request, redirect, url_for
from pymongo import MongoClient


app = Flask(__name__)


# Подключение к MongoDB
client = MongoClient("mongodb://localhost:27017/")
db = client["myDatabase"]
collection = db["users"]


@app.route('/')
def index():
    users = list(collection.find())
    if not users:
        message = "Нет пользователей для отображения."
    else:
        message = None
    return render_template('index.html', users=users, message=message)


@app.route('/add', methods=['GET', 'POST'])
def add_user():
    if request.method == 'POST':
        user_data = {
            'name': request.form['name'],
            'age': int(request.form['age']),
            'email': request.form['email']
        }
        collection.insert_one(user_data)
        return redirect(url_for('index'))
    return render_template('add_user.html')


@app.route('/delete/<user_id>')
def delete_user(user_id):
    collection.delete_one({'_id': user_id})
    return redirect(url_for('index'))


if __name__ == '__main__':
    app.run(debug=True)
