from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv
import os

# Loading Environment Variables
load_dotenv()

# Commented PostgreSQL connection
# SQLALCHEMY_DATABSE_URL = os.getenv("DATABASE_URL")

# SQLite connection (file-based database)
SQLALCHEMY_DATABASE_URL = "sqlite:///./sql_app.db"

# Sqlalchemy Engine for SQLite with check_same_thread=False for FastAPI
engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)

# Session Maker
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Base Class
Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()