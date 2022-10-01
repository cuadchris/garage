import random


class Garage():

    spots = ["1A", "1B", "1C", "1D", "1E"]

    spaces = {}

    open_spots = []

    taken_spots = []

    current_ticket = ""

    def generateGarage(self):

        # cars = ["Telsa", "BMW", "Ferrari", "Ford", "Porche", "Honda", "Toyota", "Audi", "Jeep", "Subaru",
        #         "Cadillac", "Chrysler", "Chevy", "Dodge", "Hyundai", "Mazda", "Nissan", "Lexus", "Acura", "Kia",
        #         "Volkswagen", "GMC", "Infiniti", "Lincoln", "Pontiac"]

        availibility = [["open", "taken"], [True, False]]

        for i in self.spots:
            self.spaces[i] = {"status": random.choice(availibility[0])}
            if self.spaces[i]["status"] == "open":
                # self.spaces[i]["car"] = ''
                self.spaces[i]["paid"] = ''
            else:
                # self.spaces[i]["car"] = random.choice(cars)
                self.spaces[i]["paid"] = random.choice(availibility[1])

        self.open_spots = [spot for spot in self.spaces.keys(
        ) if self.spaces[spot]["status"] == "open"]

        self.taken_spots = [spot for spot in self.spaces.keys(
        ) if self.spaces[spot]["status"] == "taken"]

    def startMessage(self):

        if len(self.open_spots) == 0:
            entry = input("*** GARAGE AT CAPACITY *** \n\nYou may 'Pay', 'Leave', 'Quit' or 'Come back later': ").lower()
        else:
            entry = input("*** GARAGE OPEN *** \n\nYou may 'Enter', 'Pay', 'Leave', or 'Quit': ").lower()

        return entry

    def takeTicket(self):
        print("Wonderful! Here's a list of available spaces: ")
        for space in self.open_spots:
            print(space)
        response = input("Enter the space you'd like to occupy, and then take your ticket: ").upper()
        self.open_spots.remove(response)
        self.spaces[response]["status"] = "taken"
        self.spaces[response]["paid"] = False
        self.current_ticket = response
        print(self.spaces[response])
        print("Great. You're all set. Don't forget your ticket!")

    def PayForParking(self):
        






user = Garage()
user.generateGarage()
# print(user.open_spots)
# print(user.taken_spots)
user.takeTicket()
# user.startMessage()