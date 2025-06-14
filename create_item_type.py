from flask import Blueprint, render_template, request
import datetime
import os

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
    return render_template('create_item_type.html', message=msg)
def list_item_types():
    if not os.path.exists(ITEMS_LOG):
        return []
    item_types = set()
    with open(ITEMS_LOG, 'r') as f:
        for line in f:
            entry = eval(line)
            item_types.add(entry['item_type'])
    return list(item_types)