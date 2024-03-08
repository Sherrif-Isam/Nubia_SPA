import os

# Directory paths
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TEMPLATES_DIR = os.path.join(BASE_DIR, 'templates')
STATIC_DIR = os.path.join(BASE_DIR, 'static')
MEDIA_DIR = os.path.join(BASE_DIR, 'media')

# Print directory paths
print("Base directory:", BASE_DIR)
print("Templates directory:", TEMPLATES_DIR)
print("Static directory:", STATIC_DIR)
print("Media directory:", MEDIA_DIR)
