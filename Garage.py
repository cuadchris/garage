import random


class Garage():

    spots = ["1A", "1B", "1C", "1D", "1E", "1F", "1G", "1H", "1I", "1J"]

    spaces = {}

    open_spots = []

    taken_spots = []

    def generateGarage(self):

        cars = ["Telsa", "BMW", "Ferrari", "Ford", "Porche", "Honda", "Toyota", "Audi", "Jeep", "Subaru",
                "Cadillac", "Chrysler", "Chevy", "Dodge", "Hyundai", "Mazda", "Nissan", "Lexus", "Acura", "Kia",
                "Volkswagen", "GMC", "Infiniti", "Lincoln", "Pontiac"]

        availibility = ["open", "taken"]

        for i in self.spots:
            self.spaces[i] = {"status": random.choice(availibility)}
            if self.spaces[i]["status"] == "open":
                self.spaces[i]["car"] = ''
            else:
                self.spaces[i]["car"] = random.choice(cars)

        self.open_spots = [spot for spot in self.spaces.keys(
        ) if self.spaces[spot]["status"] == "open"]

        self.taken_spots = [spot for spot in self.spaces.keys(
        ) if self.spaces[spot]["status"] == "taken"]

    def startMessage(self):

        if len(self.open_spots) == 0:
            entry = input("*** GARAGE AT CAPACITY *** \n\nYou may 'Leave' or 'Quit': ").lower()
        else:
            entry = input("*** GARAGE OPEN *** \n\nYou may 'Enter', 'Leave' or 'Quit': ").lower()



