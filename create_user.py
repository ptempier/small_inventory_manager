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
        users = [row for row in reader]
    return users