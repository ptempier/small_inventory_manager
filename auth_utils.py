from flask import session
import csv
import os

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

def is_user_authenticated():
    return session.get('user') is not None