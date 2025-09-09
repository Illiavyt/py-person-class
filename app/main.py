class Person:
    people = {}

    def __init__(self, name, age):
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people_list):
    person_objects = []

    for pdata in people_list:
        person = Person(pdata["name"], pdata["age"])
        person_objects.append(person)

    for pdata in people_list:
        person = Person.people[pdata["name"]]
        if "wife" in pdata and pdata["wife"] is not None:
            setattr(person, "wife", Person.people[pdata["wife"]])
        if "husband" in pdata and pdata["husband"] is not None:
            setattr(person, "husband", Person.people[pdata["husband"]])

    return person_objects