from sqlalchemy import Column, Integer, Unicode, create_engine
from sqlalchemy.ext.declarative import declarative_base

from setting import setting

conn = setting()
engine = create_engine(str(conn.GetConnectionString()), echo=True)

Base = declarative_base()


class personnel(Base):
    __tablename__ = 'personnel'
    id = Column(Integer, primary_key=True)
    name = Column(Unicode(100))
    family = Column(Unicode(100))
    age = Column(Integer)

    def __init__(self, name="", family="", age=0):
        self.name = name
        self.family = family
        self.age = age


try:
    Base.metadata.create_all(engine)
    print("Tables created successfully!")
except Exception as e:
    print(f"Error occurred while creating tables: {e}")
