import os
import sys

sys.path.append(os.path.abspath(os.path.dirname(__file__)+'/..'))

from src.app import app, db

PORT = 3001

if __name__ == "__main__":
    with app.app_context():
        db.create_all()  # Create database tables
        app.run(host="0.0.0.0", port=PORT, debug=True)
