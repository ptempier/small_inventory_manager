from flask import Flask, render_template, redirect, url_for, session, request
from create_user import bp_create_user
from create_location import bp_create_location
from create_item_type import bp_create_item_type
from create_action import bp_create_action
import os
import csv

app = Flask(__name__)
app.secret_key = "super-secret-key"  # Change this for production

# Register blueprints
app.register_blueprint(bp_create_user)
app.register_blueprint(bp_create_location)
app.register_blueprint(bp_create_item_type)
app.register_blueprint(bp_create_action)

USER_FILE = 'data/users.csv'
USER_FIELDS = ['id', 'name', 'role', 'password']


def check_credentials(username, password):
    if not os.path.exists(USER_FILE):
        return False
    with open(USER_FILE, 'r') as f:
        reader = csv.DictReader(f, delimiter='|')
        for row in reader:
            if row['name'] == username and row['password'] == password:
                return row  # return user dict
    return False


@app.route('/')
def index():
    if not session.get('user'):
        return redirect(url_for('login'))
    return render_template('main.html', user=session.get('user'))


@app.route('/login', methods=['GET', 'POST'])
def login():
    error = ""
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        user = check_credentials(username, password)
        if user:
            session['user'] = user
            return redirect(url_for('index'))
        else:
            error = "Invalid credentials"
    return render_template('login.html', error=error)


@app.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('login'))


if __name__ == '__main__':
    os.makedirs('data', exist_ok=True)
    app.run(debug=True)