from person import Person
from entities import persons
from methods import *

root_person = Person("Jesus", "Christ", "0", "35", "Male", [], [], [], 0)

persons.append(root_person)

print(root_person.__dict__)

while(True):
    person_id = input("Enter correct person ID: ")

    person = get_person_from_id(person_id)
    if person is None:
        continue

    while(True):
        operation_code = input("P: add a parent \nS: add a spouse \nC: add a child \nD: delete person \nV: view person \nX: exit \nEnter operation code: ")

        if operation_code == 'P':
            add_parent(person)
        elif operation_code == 'S':
            add_spouse(person)
        elif operation_code == 'C':
            add_child(person)
        elif operation_code == 'D':
            delete_person(person)
        elif operation_code == 'V':
            view_person(person)
        elif operation_code == 'X':
            break
        else:
            print("Shana mat ban na chapli")
        


