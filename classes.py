class Dog:
    def __init__(self, name, age, sound):
        self.name = name
        self.age = age
        self.sound = sound

    def fetch(self):
        print(f"Hey {self.name}, fetch!")

    def description(self):
        print(f"{self.name} is {self.age} years old!")

    def __str__(self):
        return(f"{self.name} is {self.age} years old!")

    def bark(self):
        print(f"{self.name}: {self.sound}")

miles = Dog("Miles", 13, "Wuff Wuff!!")
buddy = Dog("Buddy", 3, "Wauuuuu!")
retardog = Dog("Sammy", 6, "Miau!")

print(miles.name)
print(miles.age)
miles.fetch()
retardog.bark()
miles.description()
print(miles)
