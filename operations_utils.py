import csv
import os
from datetime import datetime

def initialize_operations():
    """Initialize operations CSV file if it doesn't exist"""
    operations_file = 'data/operations.csv'
    if not os.path.exists(operations_file):
        # Create empty file, operations are only appended
        with open(operations_file, 'w', newline='', encoding='utf-8') as f:
            pass

def get_operations():
    """Get all operations from CSV file"""
    initialize_operations()
    operations_file = 'data/operations.csv'
    operations = []
    
    try:
        with open(operations_file, 'r', newline='', encoding='utf-8') as f:
            reader = csv.reader(f, delimiter='|')
            for i, row in enumerate(reader):
                if len(row) >= 5:
                    operations.append({
                        'id': i,
                        'timestamp': row[0],
                        'comment': row[1],
                        'action': row[2],
                        'user': row[3],
                        'location': row[4]
                    })
    except FileNotFoundError:
        pass
    
    return operations

def add_operation(comment, action, user, location):
    """Add a new operation to CSV file (append only)"""
    initialize_operations()
    operations_file = 'data/operations.csv'
    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    
    with open(operations_file, 'a', newline='', encoding='utf-8') as f:
        writer = csv.writer(f, delimiter='|')
        writer.writerow([timestamp, comment, action, user, location])

def get_operations_by_user(username):
    """Get operations filtered by user"""
    operations = get_operations()
    return [op for op in operations if op['user'] == username]

def get_operations_by_location(location):
    """Get operations filtered by location"""
    operations = get_operations()
    return [op for op in operations if op['location'] == location]

def get_operations_by_action(action):
    """Get operations filtered by action"""
    operations = get_operations()
    return [op for op in operations if op['action'] == action]