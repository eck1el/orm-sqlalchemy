import db
from models import Person

if __name__ == "__main__":

    #Reset database if it exists
    db.Base.metadata.drop_all(bind=db.engine, checkfirst=True)

    #Here we instruct SQLAlchemy to create tables for each model in models.py, if it doesn't exist
    db.Base.metadata.create_all(db.engine)

    p1 = Person(name = "Ezequiel", age = "30")
    print(p1)