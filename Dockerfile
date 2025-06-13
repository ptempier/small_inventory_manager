# Use official Python image as base
FROM fedora:42

# Create working directory
WORKDIR /inventory-manager

# Install system dependencies
RUN dnf install -y python3-flask

# Copy application code
COPY . /inventory-manager

# Expose Flask port
EXPOSE 5000

# Run the Flask app
CMD ["flask", "run", "--host=0.0.0.0"]