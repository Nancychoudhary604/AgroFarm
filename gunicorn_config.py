# gunicorn_config.py
bind = '0.0.0.0:8000'  # Set the host and port for Gunicorn
workers = 4  # You can adjust the number of workers based on your server's capabilities
