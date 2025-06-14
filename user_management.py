from flask import Blueprint, render_template, request, redirect, url_for
import csv
import os

bp_create_user = Blueprint('create_user', __name__, template_folder='templates')
USER_FILE = 'data/users.csv'
USER_FIELDS = ['id', 'name', 'role', 'password']

def next_user_id():
    if not os.path.exists(USER_FILE):
        return 1
    with open(USER_FILE, 'r') as f:
        reader = csv.DictReader(f, delimiter='|')
        ids = [int(row['id']) for row in reader]
        return max(ids, default=0) + 1

@bp_create_user.route('/create_user', methods=['GET', 'POST'])
def create_user():
    msg = ""
    if request.method == 'POST':
        user = {
            'id': str(next_user_id()),
            'name': request.form['name'],
            'role': request.form['role'],
            'password': request.form['password']
        }
        file_exists = os.path.isfile(USER_FILE)
        with open(USER_FILE, 'a', newline='') as f:
            writer = csv.DictWriter(f, fieldnames=USER_FIELDS, delimiter='|')
            if not file_exists:
                writer.writeheader()
            writer.writerow(user)
        msg = "User created!"
    return render_template('create_user.html', message=msg)

def list_users():
    if not os.path.exists(USER_FILE):
        return []
    with open(USER_FILE, 'r') as f:
        reader = csv.DictReader(f, delimiter='|')
        users = [row for row in reader if row.get('id')]
    return users

def write_users(users):
    with open(USER_FILE, 'w', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=USER_FIELDS, delimiter='|')
        writer.writeheader()
        writer.writerows(users)

@bp_create_user.route('/edit_user/<user_id>', methods=['GET', 'POST'])
def edit_user(user_id):
    users = list_users()
    user = next((u for u in users if u['id'] == user_id), None)
    if not user:
        return "User not found", 404
    if request.method == 'POST':
        user['name'] = request.form['name']
        user['role'] = request.form['role']
        user['password'] = request.form['password']
        write_users(users)
        return redirect(url_for('index'))
    return render_template('edit_user.html', user=user)

@bp_create_user.route('/delete_user/<user_id>', methods=['POST'])
def delete_user(user_id):
    users = list_users()
    users = [u for u in users if u['id'] != user_id]
    write_users(users)
    return redirect(url_for('index'))

@bp_create_user.route('/users')
def users():
    users = list_users()
    return render_template('users.html', users=users)

def read_users():
    users = []
    try:
        with open(USER_FILE, 'r') as f:
            reader = csv.DictReader(f, delimiter='|')
            for row in reader:
                users.append(row)
    except FileNotFoundError:
        pass
    return users