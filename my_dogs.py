# my_dogs.py
import dog

my_dog = dog.Dog("Rex", "SuperDog")
my_dog.bark()

my_other_dog = dog.Dog('Annie', 'SuperDog')
print(my_other_dog.name)

first_dog = dog.Dog('Alex', 'Golden Retriever')
second_dog = dog.Dog('Sherlock', 'Shiba')
third_dog = dog.Dog('Max', 'German Shepherd')

first_dog.sit()
second_dog.roll_over()
third_dog.sit()