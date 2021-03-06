import os
workers = int(os.environ.get('GUNICORN_PROCESSES', '5'))
threads = int(os.environ.get('GUNICORN_THREADS', '3'))
timeout = 60000
forwarded_allow_ips = '*'
secure_scheme_headers = { 'X-Forwarded-Proto': 'https' }
