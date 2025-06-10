import csv

USER_FIELDS = ['id', 'name', 'role', 'password']
USER_FILE = 'data/users.csv'

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

def write_users(users):
    with open(USER_FILE, 'w', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=USER_FIELDS, delimiter='|')
        writer.writeheader()
        writer.writerows(users)