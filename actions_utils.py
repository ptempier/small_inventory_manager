import csv
import os

def initialize_actions():
    """Initialize actions CSV file with default data if it doesn't exist"""
    actions_file = 'data/actions.csv'
    if not os.path.exists(actions_file):
        with open(actions_file, 'w', newline='', encoding='utf-8') as f:
            writer = csv.writer(f, delimiter='|')
            writer.writerow(['add', 'Add new item to inventory'])
            writer.writerow(['remove', 'Remove item from inventory'])
            writer.writerow(['move', 'Move item between locations'])
            writer.writerow(['inventory', 'Perform inventory count'])

def get_actions():
    """Get all actions from CSV file"""
    initialize_actions()
    actions_file = 'data/actions.csv'
    actions = []
    
    try:
        with open(actions_file, 'r', newline='', encoding='utf-8') as f:
            reader = csv.reader(f, delimiter='|')
            for i, row in enumerate(reader):
                if len(row) >= 2:
                    actions.append({
                        'id': i,
                        'name': row[0],
                        'comment': row[1]
                    })
    except FileNotFoundError:
        pass
    
    return actions

def add_action(name, comment):
    """Add a new action to CSV file"""
    initialize_actions()
    actions_file = 'data/actions.csv'
    
    with open(actions_file, 'a', newline='', encoding='utf-8') as f:
        writer = csv.writer(f, delimiter='|')
        writer.writerow([name, comment])

def edit_action(action_id, name, comment):
    """Edit an existing action"""
    actions = get_actions()
    
    if 0 <= action_id < len(actions):
        actions[action_id] = {
            'id': action_id,
            'name': name,
            'comment': comment
        }
        
        # Write all actions back to file
        actions_file = 'data/actions.csv'
        with open(actions_file, 'w', newline='', encoding='utf-8') as f:
            writer = csv.writer(f, delimiter='|')
            for action in actions:
                writer.writerow([action['name'], action['comment']])

def delete_action(action_id):
    """Delete an action"""
    actions = get_actions()
    
    if 0 <= action_id < len(actions):
        actions.pop(action_id)
        
        # Write remaining actions back to file
        actions_file = 'data/actions.csv'
        with open(actions_file, 'w', newline='', encoding='utf-8') as f:
            writer = csv.writer(f, delimiter='|')
            for action in actions:
                writer.writerow([action['name'], action['comment']])