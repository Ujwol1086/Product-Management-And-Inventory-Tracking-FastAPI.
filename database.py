from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine

db_url = "postgresql://postgres:ujwol@localhost:5432/ujwol"
engine = create_engine(db_url)
session = sessionmaker(autocommit=False, autoflush=False, bind=engine)