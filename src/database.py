from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os

#Where the database will be stored
SQLALCHEMY_DATABASE_URL = "sqlite:///../data/database.sqlite"

#create the database engine
engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False})

#Create a session local class 
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Base class for our models to inherit from
Base = declarative_base()