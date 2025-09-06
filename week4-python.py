    print(flyer.fly())    print(flyer.use_power())
    print(flyer.introduce())
    print(hero.use_power())
    print(hero.introduce())

    flyer = FlyingSuperhero("Skyhawk", "Wind Blast", "Sky City", 500)
    hero = Superhero("Shadow", "Invisibility", "Metro City")
if __name__ == "__main__":
# Example usage

        return f"{self.name} soars and uses {self.power}!"
    def use_power(self):
    # Polymorphism: override use_power

        return f"{self.name} flies at {self.flight_speed} km/h!"
    def fly(self):

        self.flight_speed = flight_speed
        super().__init__(name, power, city)
    def __init__(self, name, power, city, flight_speed):
class FlyingSuperhero(Superhero):
# Inheritance layer

        return f"{self.name} uses {self.power}!"
    def use_power(self):

        return f"I am {self.name}, protector of {self.city}!"
    def introduce(self):

        self.city = city
        self.power = power
        self.name = name
    def __init__(self, name, power, city):
class Superhero:
