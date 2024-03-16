from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

#The engine allows communication to database through SQLAlchemy
#https://docs.sqlalchemy.org/en/14/core/engines.html

engine = create_engine("sqlite:///database/personas.db")

#creating session, This session allows us to create transactions(Operations) inside DB
Session = sessionmaker(bind=engine)
session = Session()

#Now we go to the file models.py to the classes that we want to convert to tables
# We add this variable and mapping and linking each class to each table
Base = declarative_base()
