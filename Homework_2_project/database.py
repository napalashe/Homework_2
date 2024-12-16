''' database.py
This file handles the database connection and session creation.'''

#Used to create a DB engine
from sqlalchemy import create_engine  
#sessionmaker creates sessions, Base is used for model inheritance
from sqlalchemy.orm import sessionmaker, declarative_base  


SQLALCHEMY_DATABASE_URL = "mysql+pymysql://bookuser:bookpass@localhost:3306/bookdb"

#create_engine: Takes a database URL and returns an Engine object.
engine = create_engine(SQLALCHEMY_DATABASE_URL, echo=True)  # echo=True logs all SQL statements

# sessionmaker: Factory for creating new Session objects to talk to the database
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Base class for all our models to inherit from
Base = declarative_base()

