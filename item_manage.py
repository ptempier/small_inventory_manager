from flask import Blueprint, render_template, request, redirect, url_for
import datetime
import os
import ast

bp_create_item_type = Blueprint('create_item_type', __name__, template_folder='templates')
ITEMS_LOG = 'data/orders_items.log'

@bp_create_item_type.route('/create_item_type', methods=['GET', 'POST'])
def create_item_type():
    msg = ""
    if request.method == 'POST':
        entry = {
            'event': 'create_item_type',
            'item_type': request.form['item_type'],
            'description': request.form['description'],
            'timestamp': datetime.datetime.utcnow().isoformat()
        }
        with open(ITEMS_LOG, 'a') as f:
            f.write(str(entry) + '\n')
        msg = "Item type created!"
    return render_template('item_type_create.html', message=msg)

@bp_create_item_type.route('/edit_item_type/<item_type>', methods=['GET', 'POST'])
def edit_item_type(item_type):
    item_types = list_item_types()
    item = next((i for i in item_types if i['item_type'] == item_type), None)
    if not item:
        return "Item type not found", 404
    if request.method == 'POST':
        item['item_type'] = request.form['item_type']
        item['description'] = request.form['description']
        write_item_types(item_types)
        return redirect(url_for('index'))
    return render_template('edit_item_type.html', item_type=item)

@bp_create_item_type.route('/delete_item_type/<item_type>', methods=['POST'])
def delete_item_type(item_type):
    item_types = list_item_types()
    item_types = [i for i in item_types if i['item_type'] != item_type]
    write_item_types(item_types)
    return redirect(url_for('index'))