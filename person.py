class Person:
    def __init__(
        self, first_name, last_name, yob, gender, parents, spouses, children, uid
    ):
        self.first_name = first_name
        self.last_name = last_name
        self.yob = yob
        self.gender = gender
        self.parents = parents
        self.spouses = spouses
        self.children = children
        self.uid = uid


    def __str__(self) -> str:
        return f"Name: {self.first_name}. {self.last_name}. \nYOB: {self.yob} \nGender: {self.gender} \nParents' ID: {self.parents} \nSpouses' ID :{self.spouses} \nChildren's ID: {self.children} \nID:{self.uid} \n \n"