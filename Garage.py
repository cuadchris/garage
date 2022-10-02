import random
from re import L


class Garage():

    spots = ["1A", "1B", "1C", "1D", "1E", "1F", "1G", "1H", "1I", "1J"]

    spaces = {}

    open_spots = []

    def generateGarage(self):

        # cars = ["Telsa", "BMW", "Ferrari", "Ford", "Porche", "Honda", "Toyota", "Audi", "Jeep", "Subaru",
        #         "Cadillac", "Chrysler", "Chevy", "Dodge", "Hyundai", "Mazda", "Nissan", "Lexus", "Acura", "Kia",
        #         "Volkswagen", "GMC", "Infiniti", "Lincoln", "Pontiac"]

        availibility = [["open", "taken"], [True, False]]

        for i in self.spots:
            self.spaces[i] = {"status": random.choice(availibility[0])}
            if self.spaces[i]["status"] == "open":
                self.spaces[i]["paid"] = ''
            else:
                self.spaces[i]["paid"] = random.choice(availibility[1])

        self.open_spots = [spot for spot in self.spaces.keys(
        ) if self.spaces[spot]["status"] == "open"]

    def showGarage(self):
        for key, value in self.spaces.items():
            print(f'{key}: {value}')

    def lenOpenSpots(self):
        return len(self.open_spots)

    def updateSpots(self):
        self.open_spots = [spot for spot in self.spaces.keys(
        ) if self.spaces[spot]["status"] == "open"]

    def startMessage(self):

        if self.lenOpenSpots() == 0:
            commands = ["pay", "leave", "quit"]
            command = input(
                "***GARAGE FULL*** \n Please type 'Pay', 'Leave', or 'Quit': ").lower()
            if command not in commands:
                print("Invalid response; try again")
        else:
            commands = ["pay", "leave", "quit", "enter"]
            command = input(
                "***GARAGE OPEN*** \n Please type 'Enter', 'Pay', 'Leave', or 'Quit: ").lower()
            if command not in commands:
                print("Inavlid response; try again")

        return command

    def listUnpaidTickets(self):
        return [spot for spot in self.spaces.keys() if self.spaces[spot]["paid"] == False]

    def takeTicket(self):
        if self.lenOpenSpots() > 0:
            print("Welcome! Here is a list of available spaces: ")
            for spot in self.open_spots:
                print(spot)
            command = input("Please enter one of these spaces: ").upper()
            if command not in self.open_spots:
                print("Invalid response; try again.")
            else:
                self.spaces[command]["status"] = "taken"
                self.spaces[command]["paid"] = False
                print("Thank you. Don't lose your ticket!")
                self.updateSpots()

    def payForParking(self):
        print("Here is a list of current unpaid tickets: ")
        for ticket in self.listUnpaidTickets():
            print(ticket)
        currentTicket = input("Please present your ticket: ").upper()
        if currentTicket not in self.listUnpaidTickets():
            print("Invalid response; try again.")
        else:
            commands = ["cash", "card"]
            command = input("Will you be paying with Cash or Card?: ")
            if command not in commands:
                print("Invalid response; try again.")
            else:
                self.spaces[currentTicket]["paid"] = True
                print("Thank you. Payment complete. You have 15 minutes to leave")
                self.updateSpots()
                print(self.listUnpaidTickets())
                


    def leaveGarage(self):
        pass

    def runGarage(self):
        pass


user = Garage()
user.generateGarage()
user.payForParking()