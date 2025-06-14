from flask import Blueprint, render_template, request
import datetime
import os

bp_create_action = Blueprint('create_action', __name__, template_folder='templates')
ITEMS_LOG = 'data/orders_items.log'

@bp_create_action.route('/create_action', methods=['GET', 'POST'])
def create_action():
    msg = ""
    if request.method == 'POST':
        entry = {
            'event': 'action',
            'action_type': request.form['action_type'],  # order, inventory, send, receive
            'item_type': request.form['item_type'],
            'quantity': request.form['quantity'],
            'from_location': request.form['from_location'],
            'to_location': request.form['to_location'],
            'timestamp': datetime.datetime.utcnow().isoformat(),
            'note': request.form['note']
        }
        with open(ITEMS_LOG, 'a') as f:
            f.write(str(entry) + '\n')
        msg = "Action recorded!"
    return render_template('create_action.html', message=msg)