
import os
import sys

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from sqlalchemy import create_engine
from model.Profile import Base

def create_database() -> bool:
    try:
        if not os.path.exists('main.db'):
            print("Database file does not exist. Creating a new database...")
            engine = create_engine('sqlite:///main.db', echo=True)
            Base.metadata.create_all(engine)
        else:
            print("Database file already exists. Skipping creation.")
        return True
    except Exception as e:
        print(f"Error creating database: {e}")
        return False