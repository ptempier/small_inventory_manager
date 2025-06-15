import csv
import os
from functools import wraps
from flask import session, redirect, url_for

def initialize_users():
    """Initialize users CSV file with default data if it doesn't exist"""
    users_file = 'data/users.csv'
    if not os.path.exists(users_file):
        with open(users_file, 'w', newline='', encoding='utf-8') as f:
            writer = csv.writer(f, delimiter='|')
            writer.writerow(['admin', '123', 'admin'])
            writer.writerow(['user1', 'pass1', 'user'])
            writer.writerow(['user2', 'pass2', 'user'])
            writer.writerow(['manager1', 'pass3', 'manager'])

def authenticate_user(username, password):
    """Authenticate user credentials"""
    initialize_users()
    users_file = 'data/users.csv'
    
    try:
        with open(users_file, 'r', newline='', encoding='utf-8') as f:
            reader = csv.reader(f, delimiter='|')
            for row in reader:
                if len(row) >= 3 and row[0] == username and row[1] == password:
                    return True
    except FileNotFoundError:
        return False
    
    return False

def get_user_group(username):
    """Get user group by username"""
    initialize_users()
    users_file = 'data/users.csv'
    
    try:
        with open(users_file, 'r', newline='', encoding='utf-8') as f:
            reader = csv.reader(f, delimiter='|')
            for row in reader:
                if len(row) >= 3 and row[0] == username:
                    return row[2]
    except FileNotFoundError:
        pass
    
    return None

def require_login(f):
    """Decorator to require user login"""
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if 'user' not in session:
            return redirect(url_for('login'))
        return f(*args, **kwargs)
    return decorated_function

def require_admin(f):
    """Decorator to require admin privileges"""
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if 'user' not in session:
            return redirect(url_for('login'))
        
        user_group = get_user_group(session['user'])
        if user_group != 'admin':
            return redirect(url_for('index'))
        
        return f(*args, **kwargs)
    return decorated_function