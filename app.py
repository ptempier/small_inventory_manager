from flask import Flask, render_template, redirect, url_for, session, request
from create_user import bp_create_user
from create_location import bp_create_location, list_locations
from create_item_type import bp_create_item_type
from create_action import bp_create_action
import csv
import os

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
    locations = list_locations()
    return render_template('main.html', user=session.get('user'), locations=locations)


@app.route('/login', methods=['GET', 'POST'])
def login():
    error = ""
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        user = check_credentials(username, password)
        if user:
            session['user'] = {'id': user['id'], 'name': user['name'], 'role': user['role']}
            return redirect(url_for('index'))
        else:
            error = "Invalid credentials"
    return render_template('login.html', error=error)


@app.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('login'))


@app.route('/locations')
def locations():
    if not session.get('user'):
        return redirect(url_for('login'))
    locations = list_locations()
    return render_template('locations.html', user=session.get('user'), locations=locations)


@app.route('/edit_location/<int:location_id>', methods=['GET', 'POST'])
def edit_location(location_id):
    if not session.get('user'):
        return redirect(url_for('login'))
    location = None
    if request.method == 'POST':
        # Here you would handle the form submission for editing a location
        # For now, let's just redirect to the locations page
        return redirect(url_for('locations'))
    else:
        # Load the location data for the given location_id
        locations = list_locations()
        for loc in locations:
            if loc['id'] == location_id:
                location = loc
                break
    return render_template('edit_location.html', user=session.get('user'), location=location)


@app.context_processor
def utility_processor():
    def url_for_edit_location(location_id):
        return url_for('create_location.edit_location', location_id=location_id)
    return dict(url_for_edit_location=url_for_edit_location)


if __name__ == '__main__':
    os.makedirs('data', exist_ok=True)
    app.run(debug=True)