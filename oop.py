# object-oriented programming
# class takes sentence case
class Person:
    def __init__(self, name, age, country):
        self.name = name
        self.age = age
        self.country = country


person1 = Person("may", 23, 'Kenya')
person2 = Person("Steph", 18, "Kenya")


print(person1.name)
print(f"Hi, my name is {person1.name}")
