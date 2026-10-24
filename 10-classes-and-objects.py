# class - blueprint
# object - actual thing created from blueprint (class)

class Rocket:
    def __init__(self, name, fuel, velocity):
        self.name = name
        self.fuel = fuel
        self.velocity = velocity

falcon = Rocket("Falcon", 100, 15000)

print(falcon.name)
print(falcon.fuel)
print(falcon.velocity)

