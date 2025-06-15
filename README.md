This project is an inventory management system designed to streamline the process of managing :
items, sites/locations, users, and transactions within an organization. The system includes the following features:

Inventory Tracking: Users can inventory items at various sites/locations.
Item Transactions: Users can send, receive, or order items, with each action logged in a detailed log file.
Site/Location Management: Administrators can create and manage new sites/locations.
User Management: Administrators can create and manage new users.
Item Management: Administrators can create and manage new items.
The system is built using Python with flask and includes the following components:

The project use the following files :
- app.py: The main application file, it routes requests between pages and include relevant functions, it has a shebang/header to be started from a shell
- actions_utils.py: Handles various actions such as inventory, send/receive/order items, and user/site/item management.
- locations_utils.py: Manages locations, it can list, create, edit, delete them
- item_utils.py: Manages items, it can list, create, edit, delete them
- users_utils.py: Manages user, it can list, create, edit, delete them
- auth_utils.py: Manages users authentication
- actions_utils.py: Manages actions, it can list, create, edit, delete them
- operations_utils.py: Manages users operations on items

Dockerfile: Provides a Docker container for easy deployment.
The project use the following folders
- templates/: Contains HTML templates for the web interface.  It contains one template for each python file prebiousely mentionned
- static/: Contains static files such as CSS and JavaScript.
- data/: Contains the csv files that stores the data.

The main page use tabs for the interface.
it always displays theses tabs , users, items, locations, items, action
in each of theses pages, there's the list of elements, with a buton next to them delete, a button do edit : and a form at the top to add

All the data is stored as a csv file, but the separator is |
there is one csv for : users, locations, items , actions, operations

these files can be read and writen as whole files
users : has a login; a password, a group , it is initialised with : a user admin with password 123 ; and 3 lines of test users
items : has a location , a name, a comment , initialised with 3 lines of test data
locations : has a name and an adress, , initialised with 3 lines of test data
actions : has a name and a comment , it is initialised with : add, remove, move, inventory

this file is always only appended to
operations :  has a comment , an action , a user,  a location