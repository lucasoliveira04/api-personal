import os
from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import psycopg2

load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL")

engine = create_engine(DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def get_engine():
    return engine

def get_session():
    return SessionLocal()

def get_connection() -> bool:
    try:
        conn = psycopg2.connect(DATABASE_URL)
        conn.close()
        return True
    except Exception as e:
        return False
