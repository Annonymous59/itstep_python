class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):

        print(f"{self.name} says something")



class Dog(Animal):

    def bark(self):
        print(f"{self.name} gav gav!!")


# animal = Animal("Animal")
# animal.speak()
#
# dog = Dog("Dog")
#
# dog.speak()
# dog.bark()

class BreedDog(Animal):

    def __init__(self, name, breed):
        super().__init__(name)
        self.breed = breed


    def speak(self):
        print(f"{super().speak()} and {self.name} is {self.breed}")




breed_dog = BreedDog("Hot","Dog")

breed_dog.speak()


