import csv
import os
from auth_utils import initialize_users

def get_users():
    """Get all users from CSV file"""
    initialize_users()
    users_file = 'data/users.csv'
    users = []
    
    try:
        with open(users_file, 'r', newline='', encoding='utf-8') as f:
            reader = csv.reader(f, delimiter='|')
            for i, row in enumerate(reader):
                if len(row) >= 3:
                    users.append({
                        'id': i,
                        'login': row[0],
                        'password': row[1],
                        'group': row[2]
                    })
    except FileNotFoundError:
        pass
    
    return users

def add_user(login, password, group):
    """Add a new user to CSV file"""
    initialize_users()
    users_file = 'data/users.csv'
    
    with open(users_file, 'a', newline='', encoding='utf-8') as f:
        writer = csv.writer(f, delimiter='|')
        writer.writerow([login, password, group])

def edit_user(user_id, login, password, group):
    """Edit an existing user"""
    users = get_users()
    
    if 0 <= user_id < len(users):
        users[user_id] = {
            'id': user_id,
            'login': login,
            'password': password,
            'group': group
        }
        
        # Write all users back to file
        users_file = 'data/users.csv'
        with open(users_file, 'w', newline='', encoding='utf-8') as f:
            writer = csv.writer(f, delimiter='|')
            for user in users:
                writer.writerow([user['login'], user['password'], user['group']])

def delete_user(user_id):
    """Delete a user"""
    users = get_users()
    
    if 0 <= user_id < len(users):
        users.pop(user_id)
        
        # Write remaining users back to file
        users_file = 'data/users.csv'
        with open(users_file, 'w', newline='', encoding='utf-8') as f:
            writer = csv.writer(f, delimiter='|')
            for user in users:
                writer.writerow([user['login'], user['password'], user['group']])