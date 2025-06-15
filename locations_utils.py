import csv
import os

def initialize_locations():
    """Initialize locations CSV file with default data if it doesn't exist"""
    locations_file = 'data/locations.csv'
    if not os.path.exists(locations_file):
        with open(locations_file, 'w', newline='', encoding='utf-8') as f:
            writer = csv.writer(f, delimiter='|')
            writer.writerow(['Warehouse A', '123 Storage St, City, State'])
            writer.writerow(['Warehouse B', '456 Depot Ave, City, State'])
            writer.writerow(['Office Main', '789 Business Blvd, City, State'])

def get_locations():
    """Get all locations from CSV file"""
    initialize_locations()
    locations_file = 'data/locations.csv'
    locations = []
    
    try:
        with open(locations_file, 'r', newline='', encoding='utf-8') as f:
            reader = csv.reader(f, delimiter='|')
            for i, row in enumerate(reader):
                if len(row) >= 2:
                    locations.append({
                        'id': i,
                        'name': row[0],
                        'address': row[1]
                    })
    except FileNotFoundError:
        pass
    
    return locations

def add_location(name, address):
    """Add a new location to CSV file"""
    initialize_locations()
    locations_file = 'data/locations.csv'
    
    with open(locations_file, 'a', newline='', encoding='utf-8') as f:
        writer = csv.writer(f, delimiter='|')
        writer.writerow([name, address])

def edit_location(location_id, name, address):
    """Edit an existing location"""
    locations = get_locations()
    
    if 0 <= location_id < len(locations):
        locations[location_id] = {
            'id': location_id,
            'name': name,
            'address': address
        }
        
        # Write all locations back to file
        locations_file = 'data/locations.csv'
        with open(locations_file, 'w', newline='', encoding='utf-8') as f:
            writer = csv.writer(f, delimiter='|')
            for location in locations:
                writer.writerow([location['name'], location['address']])

def delete_location(location_id):
    """Delete a location"""
    locations = get_locations()
    
    if 0 <= location_id < len(locations):
        locations.pop(location_id)
        
        # Write remaining locations back to file
        locations_file = 'data/locations.csv'
        with open(locations_file, 'w', newline='', encoding='utf-8') as f:
            writer = csv.writer(f, delimiter='|')
            for location in locations:
                writer.writerow([location['name'], location['address']])