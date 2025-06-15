#!/usr/bin/env python3

from flask import Flask, render_template, request, redirect, url_for, flash, session
import os
from auth_utils import authenticate_user, require_login
from users_utils import get_users, add_user, edit_user, delete_user
from locations_utils import get_locations, add_location, edit_location, delete_location
from items_utils import get_items, add_item, edit_item, delete_item
from actions_utils import get_actions, add_action, edit_action, delete_action
from operations_utils import get_operations, add_operation

app = Flask(__name__)
app.secret_key = 'your-secret-key-change-this-in-production'

# Initialize data directory
if not os.path.exists('data'):
    os.makedirs('data')

@app.route('/')
def index():
    if 'user' not in session:
        return redirect(url_for('login'))
    return render_template('main.html', 
                         users=get_users(), 
                         locations=get_locations(), 
                         items=get_items(), 
                         actions=get_actions(),
                         operations=get_operations())

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if authenticate_user(username, password):
            session['user'] = username
            return redirect(url_for('index'))
        else:
            flash('Invalid credentials')
    return render_template('login.html')

@app.route('/logout')
def logout():
    session.pop('user', None)
    return redirect(url_for('login'))

# User management routes
@app.route('/add_user', methods=['POST'])
@require_login
def add_user_route():
    login = request.form['login']
    password = request.form['password']
    group = request.form['group']
    add_user(login, password, group)
    flash('User added successfully')
    return redirect(url_for('index'))

@app.route('/edit_user/<int:user_id>', methods=['POST'])
@require_login
def edit_user_route(user_id):
    login = request.form['login']
    password = request.form['password']
    group = request.form['group']
    edit_user(user_id, login, password, group)
    flash('User updated successfully')
    return redirect(url_for('index'))

@app.route('/delete_user/<int:user_id>')
@require_login
def delete_user_route(user_id):
    delete_user(user_id)
    flash('User deleted successfully')
    return redirect(url_for('index'))

# Location management routes
@app.route('/add_location', methods=['POST'])
@require_login
def add_location_route():
    name = request.form['name']
    address = request.form['address']
    add_location(name, address)
    flash('Location added successfully')
    return redirect(url_for('index'))

@app.route('/edit_location/<int:location_id>', methods=['POST'])
@require_login
def edit_location_route(location_id):
    name = request.form['name']
    address = request.form['address']
    edit_location(location_id, name, address)
    flash('Location updated successfully')
    return redirect(url_for('index'))

@app.route('/delete_location/<int:location_id>')
@require_login
def delete_location_route(location_id):
    delete_location(location_id)
    flash('Location deleted successfully')
    return redirect(url_for('index'))

# Item management routes
@app.route('/add_item', methods=['POST'])
@require_login
def add_item_route():
    location = request.form['location']
    name = request.form['name']
    comment = request.form['comment']
    add_item(location, name, comment)
    flash('Item added successfully')
    return redirect(url_for('index'))

@app.route('/edit_item/<int:item_id>', methods=['POST'])
@require_login
def edit_item_route(item_id):
    location = request.form['location']
    name = request.form['name']
    comment = request.form['comment']
    edit_item(item_id, location, name, comment)
    flash('Item updated successfully')
    return redirect(url_for('index'))

@app.route('/delete_item/<int:item_id>')
@require_login
def delete_item_route(item_id):
    delete_item(item_id)
    flash('Item deleted successfully')
    return redirect(url_for('index'))

# Action management routes
@app.route('/add_action', methods=['POST'])
@require_login
def add_action_route():
    name = request.form['name']
    comment = request.form['comment']
    add_action(name, comment)
    flash('Action added successfully')
    return redirect(url_for('index'))

@app.route('/edit_action/<int:action_id>', methods=['POST'])
@require_login
def edit_action_route(action_id):
    name = request.form['name']
    comment = request.form['comment']
    edit_action(action_id, name, comment)
    flash('Action updated successfully')
    return redirect(url_for('index'))

@app.route('/delete_action/<int:action_id>')
@require_login
def delete_action_route(action_id):
    delete_action(action_id)
    flash('Action deleted successfully')
    return redirect(url_for('index'))

# Operation management routes
@app.route('/add_operation', methods=['POST'])
@require_login
def add_operation_route():
    comment = request.form['comment']
    action = request.form['action']
    user = session['user']
    location = request.form['location']
    add_operation(comment, action, user, location)
    flash('Operation added successfully')
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)