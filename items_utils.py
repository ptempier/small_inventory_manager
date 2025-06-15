import csv
import os

def initialize_items():
    """Initialize items CSV file with default data if it doesn't exist"""
    items_file = 'data/items.csv'
    if not os.path.exists(items_file):
        with open(items_file, 'w', newline='', encoding='utf-8') as f:
            writer = csv.writer(f, delimiter='|')
            writer.writerow(['Warehouse A', 'Laptop Dell XPS 13', 'Business laptop for mobile work'])
            writer.writerow(['Warehouse B', 'Office Chair Ergonomic', 'Adjustable office chair with lumbar support'])
            writer.writerow(['Office Main', 'Printer HP LaserJet', 'Black and white laser printer for documents'])

def get_items():
    """Get all items from CSV file"""
    initialize_items()
    items_file = 'data/items.csv'
    items = []
    
    try:
        with open(items_file, 'r', newline='', encoding='utf-8') as f:
            reader = csv.reader(f, delimiter='|')
            for i, row in enumerate(reader):
                if len(row) >= 3:
                    items.append({
                        'id': i,
                        'location': row[0],
                        'name': row[1],
                        'comment': row[2]
                    })
    except FileNotFoundError:
        pass
    
    return items

def add_item(location, name, comment):
    """Add a new item to CSV file"""
    initialize_items()
    items_file = 'data/items.csv'
    
    with open(items_file, 'a', newline='', encoding='utf-8') as f:
        writer = csv.writer(f, delimiter='|')
        writer.writerow([location, name, comment])

def edit_item(item_id, location, name, comment):
    """Edit an existing item"""
    items = get_items()
    
    if 0 <= item_id < len(items):
        items[item_id] = {
            'id': item_id,
            'location': location,
            'name': name,
            'comment': comment
        }
        
        # Write all items back to file
        items_file = 'data/items.csv'
        with open(items_file, 'w', newline='', encoding='utf-8') as f:
            writer = csv.writer(f, delimiter='|')
            for item in items:
                writer.writerow([item['location'], item['name'], item['comment']])

def delete_item(item_id):
    """Delete an item"""
    items = get_items()
    
    if 0 <= item_id < len(items):
        items.pop(item_id)
        
        # Write remaining items back to file
        items_file = 'data/items.csv'
        with open(items_file, 'w', newline='', encoding='utf-8') as f:
            writer = csv.writer(f, delimiter='|')
            for item in items:
                writer.writerow([item['location'], item['name'], item['comment']])