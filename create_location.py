from flask import Blueprint, render_template, request
import csv
import os

bp_create_location = Blueprint('create_location', __name__, template_folder='templates')
LOCATION_FILE = 'data/locations.csv'
LOCATION_FIELDS = ['id', 'name', 'address']

def next_location_id():
    if not os.path.exists(LOCATION_FILE):
        return 1
    with open(LOCATION_FILE, 'r') as f:
        reader = csv.DictReader(f, delimiter='|')
        ids = [int(row['id']) for row in reader]
        return max(ids, default=0) + 1

@bp_create_location.route('/create_location', methods=['GET', 'POST'])
def create_location():
    msg = ""
    if request.method == 'POST':
        location = {
            'id': str(next_location_id()),
            'name': request.form['name'],
            'address': request.form['address']
        }
        file_exists = os.path.isfile(LOCATION_FILE)
        with open(LOCATION_FILE, 'a', newline='') as f:
            writer = csv.DictWriter(f, fieldnames=LOCATION_FIELDS, delimiter='|')
            if not file_exists:
                writer.writeheader()
            writer.writerow(location)
        msg = "Location created!"
    return render_template('create_location.html', message=msg)