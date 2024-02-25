class Jeep:
    def __init__(self, fuel: int = 10,  speed: int = 40, armor_resistance: int = 65,age: int = 1):
        self.fuel = fuel
        self.speed = speed
        self.armor_resistance = armor_resistance
        self.age = age


    def drive(self, hours: int):
        self.fuel -= hours
        self.age += hours * 0.01

    def refuel(self, fuel_amount: int):
        if self.fuel <= 0:
            self.fuel += fuel_amount
        else:
            self.fuel = 10


    def upgrade(self, upgrade: int):

        self.speed += upgrade

        self.armor_resistance += upgrade

    def crash(self, strength):
        self.fuel -= strength
        self.armor_resistance -= strength

    def car_charecters(self):
        print(f"Fuel:{self.fuel}, Speed:{self.speed}, Armor_resistance:{self.armor_resistance}, Age: {self.age}")


class SportCar:
    def __init__(self, fuel: int = 15, speed: int = 100, armor_resistance: int = 35, age: int = 5):
        self.fuel = fuel
        self.speed = speed
        self.armor_resistance = armor_resistance
        self.age = age

    def drive(self, hours: int):
        self.fuel -= hours
        self.age += hours * 0.01

    def refuel(self, fuel_amount: int):
        if self.fuel <= 0:
            self.fuel += fuel_amount
        else:
            self.fuel = 10

    def upgrade(self, upgrade: int):

        self.speed += upgrade

        self.armor_resistance += upgrade

    def crash(self, strength):
        self.fuel -= strength
        self.armor_resistance -= strength

    def car_charecters(self):
        print(f"Fuel:{self.fuel}, Speed:{self.speed}, Armor_resistance:{self.armor_resistance}, Age: {self.age}")


class Lorry:
    def __init__(self, fuel: int = 40, speed: int = 25, armor_resistance: int = 78, age: int = 12):
        self.fuel = fuel
        self.speed = speed
        self.armor_resistance = armor_resistance
        self.age = age

    def drive(self, hours: int):
        self.fuel -= hours
        self.age += hours * 0.01

    def refuel(self, fuel_amount: int):
        if self.fuel <= 0:
            self.fuel += fuel_amount
        else:
            self.fuel = 10

    def upgrade(self, upgrade: int):

        self.speed += upgrade

        self.armor_resistance += upgrade

    def crash(self, strength):
        self.fuel -= strength
        self.armor_resistance -= strength

    def car_charecters(self):
        print(f"Fuel:{self.fuel}, Speed:{self.speed}, Armor_resistance:{self.armor_resistance}, Age: {self.age}")


car = input("Choose car j/s/l: ")

if car == "j":
    jeep1 = Jeep()

elif car == "s":
    sportcar1 = SportCar()

elif car == "l":
    lorry = Lorry()

    drive = input("Drive: ")

    refuel = input("Refuel: ")