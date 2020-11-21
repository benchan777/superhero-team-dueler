class Animal:
    def __init__(self, name):
        self.name = name

    def eat(self):
        print(f"{self.name} is eating.")

    def drink(self):
        print(f"{self.name} is drinking.")

class Frog(Animal):
    def jump(self):
        print(f"{self.name} is jumping.")

my_dog = Animal("Sophie")
my_dog.eat()
my_dog.drink()
# my_dog.jump()

frog = Frog("Tim")
frog.jump()
frog.drink()