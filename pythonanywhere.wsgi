
import sys
import os

# Add the directory containing your Flask app to the Python path
project_home = '/home/jcino2024/pythonstatboticsproject'
if project_home not in sys.path:
    sys.path.append(project_home)

# Set up the Flask application object
from app import app as application

# Set environment variables if necessary
os.environ['SOME_VARIABLE'] = 'value'