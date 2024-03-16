import sys

import db
from models import Person
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
    pass
def addNewPerson():
    print("\n > Adding person")
    name = input("Please enter person's name: ")
    age = int(input("Please enter person's age: "))
    p = Person(name, age)
    db.session.add(p)
    db.session.commit()
    db.session.close()

def updatePerson():
    pass
def deletePerson():
    pass
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




