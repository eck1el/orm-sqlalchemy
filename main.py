import sys

import db
from models import Person
from sqlalchemy import and_, or_, text


def addInitPerson():
    p1 = Person("Daniel", 20)
    p2 = Person("Alex", 31)
    p3 = Person("Sara", 25)
    p4 = Person("Maria", 18)
    p5 = Person("Marta", 33)
    p6 = Person("Mario", 18)

    peopleList = [p1, p2, p3, p4, p5, p6]

    db.session.add_all(peopleList)
    db.session.commit()
    db.session.close()
def testquery():
    print("\n #1 Get an object by Id(its primary key) if it does not exist I will get NONE")
    #result = db.session.query(Person).get(id) Deprecated version
    result = db.session.get(Person, 3)
    print(result)
    print(type(result))
    print(result.name)

    print("\n #2 Get all the objects from a table")
    result = db.session.query(Person).all()
    for p in result:
        print("\t > Id: {} -> Name: {} -> Age: {}".format(p.id_person, p.name, p.age))

    print("\n #3 Get the first object in a query(oldest)")
    result = db.session.query(Person).first()
    print(result)

    print("\n #4 Get the number of elements in a table")
    result = db.session.query(Person).count()
    print(result)

    print("\n #5 Sort results in a query")
    result = db.session.query(Person).order_by("name").all()
    for p in result:
        print("\t > Id: {} -> Name: {} -> Age: {}".format(p.id_person, p.name, p.age))

    print("\n #6 Sort results and show the first three")
    result = db.session.query(Person).order_by("name").limit(3)
    for p in result:
        print("\t > Id: {} -> Name: {} -> Age: {}".format(p.id_person, p.name, p.age))

    print("\n #7 applying ilike filter")
    result = db.session.query(Person).filter(Person.name.ilike("Ma%")).all()
    for p in result:
        print("\t > Id: {} -> Name: {} -> Age: {}".format(p.id_person, p.name, p.age))

    print("\n #8 applying in_ filter")
    result = db.session.query(Person).filter(Person.id_person.in_([1, 2, 6])).all()
    for p in result:
        print("\t > Id: {} -> Name: {} -> Age: {}".format(p.id_person, p.name, p.age))

    print("\n #9 applying and_ filter")
    c1 = Person.id_person > 4
    c2 = Person.name.ilike("M%")
    result = db.session.query(Person).filter(and_(c1, c2)).all()
    for p in result:
        print("\t > Id: {} -> Name: {} -> Age: {}".format(p.id_person, p.name, p.age))

    print("\n #10 Run explicit sql queries")
    result = db.session.query(Person).from_statement(text("SELECT * FROM person")).all()
    for p in result:
        print("\t > Id: {} -> Name: {} -> Age: {}".format(p.id_person, p.name, p.age))
def addNewPerson():
    print("\n > Adding person")
    name = input("Please enter person's name: ")
    age = int(input("Please enter person's age: "))
    p = Person(name, age)
    db.session.add(p)
    db.session.commit()
    db.session.close()

def updatePerson():
    print("\n > Update people")
    showPeople()
    person_id = int(input("please input person's ID: "))
    person = db.session.query(Person).filter(Person.id_person == person_id).first()

    if person is None:
        print("This person does not exist")
    else:
        new_age = int(input("Please Enter new age: "))
        person.age = new_age
        db.session.commit()
        db.session.close()
        print("The person has been updated")
def deletePerson():
    print("\n > Delete people")
    showPeople()
    person_id = int(input("please input person's ID: "))
    person = db.session.query(Person).filter(Person.id_person == person_id).first()

    if person is None:
        print("This person does not exist")
    else:
        db.session.delete(person)
        db.session.commit()
        db.session.close()
        print("The person has been updated")
def showPeople():
    people = db.session.query(Person).all()
    for p in people:
        print("\t > Id: {} -> Name: {} -> Age: {}".format(p.id_person, p.name, p.age))



if __name__ == "__main__":

    #Reset database if it exists
    db.Base.metadata.drop_all(bind=db.engine, checkfirst=True)

    #Here we instruct SQLAlchemy to create tables for each model in models.py, if it doesn't exist
    db.Base.metadata.create_all(db.engine)

    while(True):
        print(
            "\n1. Add init person"
            "\n2. Test query"
            "\n3. Add new person"
            "\n4. update person"
            "\n5. Delete new person"
            "\n6. Show people"
            "\n7. Exit"
        )

        option = int(input("Please choose an option by pressing a number between(1-7)"))
        if option == 1:
            addInitPerson()
        elif option ==2:
            testquery()
        elif option ==3:
            addNewPerson()
        elif option==4:
            updatePerson()
        elif option==5:
            deletePerson()
        elif option == 6:
            showPeople()
        elif option == 7:
            sys.exit(1)
        else:
            print("Opcion no válida")




