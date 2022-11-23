from person import Person
from entities import persons

def get_person_from_id(person_id):
    try:
        person_id = int(person_id)
    except:
        print("Shana mat ban na chapli")
        return None

    person_uids = [p.uid for p in persons]

    if person_id not in person_uids:
        print("Shana mat ban na chapli")
        return None

    person = [p for p in persons if p.uid == person_id][0]
    return person

def add_parent(person):
    parent = add_person() 
    if parent is None:
        return   
        
    parent.children.append(person.uid)
    person.parents.append(parent.uid)
    print(person.__dict__)

def add_spouse(person):
    pass

def add_child(person):
    pass

def add_person():
    exists = input("Is this person added already?: ")
    if exists == "Y":
        person_id = input("Enter the added person's ID: ")
        return get_person_from_id(person_id)

    elif not exists == "N":
        print("Shana mat ban na chapli")
        return None

    first_name = input("Enter first_name: ")
    last_name = input("Enter last_name: ")
    yob = input("Enter yob: ")
    yod = input("Enter yod: ")
    gender = input("Enter gender: ")
    parents = []
    spouses = []
    children = []
    uid = persons[-1].uid + 1
    person = Person(first_name, last_name, yob, yod, gender, parents, spouses, children, uid)
    persons.append(person)
    return person

def view_person(person):
    print(person.__dict__)

def delete_person(person):
    pass