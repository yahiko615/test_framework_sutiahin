from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

DATABASE_URI = 'postgresql://postgres:12345@localhost/misha'
engine = create_engine(DATABASE_URI)
Session = sessionmaker(bind=engine)
