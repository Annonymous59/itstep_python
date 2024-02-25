class Human:
    def __init__(self,name: str = "Sim",age: int = 0 ,energy: int = 100,hapiness: int = 100,hunger: int = 0):
        self.name = name
        self.age = age
        self.energy = energy
        self.hapiness = hapiness
        self.hunger = hunger

    def eat (self, food: int):
        self.hunger -= food
        if self.hunger < 0:
            self.hunger = 0

        print(f"{self.name} ate. hunger: {self.hunger}")


    def sleep(self,hours: int):
        self.energy += hours
        if self.energy > 100:
            self.energy = 100

        print(f"{self.name} slept. energy: {self.energy}")


    def play(self, activity: int):
        self.hapiness += activity
        if self.hapiness > 100:
            self.hapiness = 100

        print(f"{self.name} played. hapiness: {self.hapiness}")

    def age_up(self,years: int):
        self.age += years

        print(f"{self.name} aged up. age: {self.age}")

    def status(self):

        print(f"{self.name} status: Age:{self.age} Energy: {self.energy} Hapiness: {self.hapiness} Hunger: {self.hunger}")


sim = Human("Sim1")

a = int(input("Eat: "))
sim.eat(a)

b = int(input("Sleep: "))
sim.sleep(b)

c = int(input("Play:"))
sim.play(c)

d = int(input("Ageup: "))
sim.age_up(d)

sim.status()

