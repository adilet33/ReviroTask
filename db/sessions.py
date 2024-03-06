import os

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from typing import Generator


DATABASE_URL = os.getenv(
    "DATABASE_URL", "postgresql+psycopg2://adilet:frontend@localhost:5432/fastapi_db"
)

engine = create_engine(DATABASE_URL, future=True)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
