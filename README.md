# small_inventory_manager
# Inventory Management System

This project is an inventory management system designed to streamline the process of managing items, sites/locations, users, and transactions within an organization. The system includes the following features:

- **Inventory Tracking**: Users can inventory items at various sites/locations.
- **Item Transactions**: Users can send, receive, or order items, with each action logged in a detailed log file.
- **Site/Location Management**: Administrators can create and manage new sites/locations.
- **User Management**: Administrators can create and manage new users.
- **Item Management**: Administrators can create and manage new items.

The system is built using Python and includes the following components:

- `app.py`: The main application file.
- `create_action.py`: Handles various actions such as inventory, send/receive/order items, and user/site/item management.
- `create_user.py`: Manages user creation and authentication.
- `Dockerfile`: Provides a Docker container for easy deployment.
- `requirements.txt`: Lists all the necessary Python packages.
- `templates/`: Contains HTML templates for the web interface.
- `static/`: Contains static files such as CSS and JavaScript.

To get started, follow these steps:

1. Clone the repository.
2. Install the required dependencies using `pip install -r requirements.txt`.
3. Run the application using `python app.py`.

For more information on how to use the system, please refer to the documentation or contact the support team.