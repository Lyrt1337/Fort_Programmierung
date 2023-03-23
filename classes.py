class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def fetch(self):
        print(f"Hey {self.name}, fetch!")

    def description(self):
        print(f"{self.name} is {self.age} years old!")

    def __str__(self):
        return f"{self.name} is {self.age} years old!"

    def bark(self, sound):
        print(f"{self.name}: {sound}")


class Bulldog(Dog):
    def bark(self, sound="Arf"):
        print(f"{self.name} goes: {sound}")
        return f"{self.name} goes: {sound}"


miles = Dog("Miles", 13)
buddy = Dog("Buddy", 3)
retardog = Dog("Retardog", 6)
chad = Bulldog("Chad", 8)

print(miles.name)
print(miles.age)
miles.fetch()
retardog.bark("Miau")
miles.description()
print(miles)
chad.bark("Woof")
chad.fetch()
