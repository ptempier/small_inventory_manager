from flask import Blueprint, render_template, request, redirect, url_for
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

def list_locations():
    if not os.path.exists(LOCATION_FILE):
        return []
    with open(LOCATION_FILE, 'r') as f:
        reader = csv.DictReader(f, delimiter='|')
        locations = [row for row in reader]
    return locations

def write_locations(locations):
    with open(LOCATION_FILE, 'w', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=LOCATION_FIELDS, delimiter='|')
        writer.writeheader()
        writer.writerows(locations)

@bp_create_location.route('/edit_location/<location_id>', methods=['GET', 'POST'])
def edit_location(location_id):
    locations = list_locations()
    location = next((l for l in locations if l['id'] == location_id), None)
    if not location:
        return "Location not found", 404
    if request.method == 'POST':
        location['name'] = request.form['name']
        location['address'] = request.form['address']
        write_locations(locations)
        return redirect(url_for('index'))
    return render_template('edit_location.html', location=location)

@bp_create_location.route('/delete_location/<location_id>', methods=['POST'])
def delete_location(location_id):
    locations = list_locations()
    locations = [l for l in locations if l['id'] != location_id]
    write_locations(locations)
    return redirect(url_for('index'))