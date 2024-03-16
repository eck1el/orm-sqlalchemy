from sqlalchemy import Column, Integer, String

import db


class Person(db.Base):

    __tablename__   =  "person"

    #optional
    __table_args__  =   {'sqlite_autoincrement':True}
    id_person = Column(Integer, primary_key=True)
    name = Column(String, nullable=False) #It can't be empty
    age = Column(Integer)
    def __init__(self, name, age):
        self.name = name
        self.age = age
        print("Person created successfully")

    def __str__(self):
        return "Person({} {})".format(self.name, self.age)