import random

class Garage():

    spots = ["1A", "1B", "1C", "1D", "1E", "1F", "1G", "1H", "1I", "1J"]

    spaces = {}

    open_spots = []

    def generateGarage(self):
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
        
    def takenSpaces(self):
        return [spot for spot in self.spaces.keys() if self.spaces[spot]["status"] == "taken"]
        
    def updateSpots(self):
        self.open_spots = [spot for spot in self.spaces.keys(
        ) if self.spaces[spot]["status"] == "open"]

    def startMessage(self):
        if self.lenOpenSpots() == 0:
            commands = ["pay", "leave", "quit", "come back later"]
            command = input(
                "***GARAGE FULL*** \n Please type 'Pay', 'Leave', 'Come back later', or 'Quit': ").lower()
            if command not in commands:
                print("Invalid response; try again")
        else:
            commands = ["pay", "leave", "quit", "enter"]
            command = input(
                "***GARAGE OPEN*** \n Please type 'Enter', 'Pay', 'Leave', or 'Quit: ").lower()
            if command not in commands:
                print("Invalid response; try again")

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
        if len(self.listUnpaidTickets()) == 0:
            print(
                "There are currently no unpaid tickets. Try 'Leave' and present your ticket.")
        else:
            print("Here is a list of current unpaid tickets: ")
            for ticket in self.listUnpaidTickets():
                print(ticket)
            currentTicket = input("Please present your ticket: ").upper()
            if currentTicket not in self.listUnpaidTickets():
                print("Invalid response; try again.")
            else:
                commands = ["cash", "card"]
                command = input(
                    "Will you be paying with Cash or Card?: ").lower()
                if command not in commands:
                    print("Invalid response; try again.")
                else:
                    self.spaces[currentTicket]["paid"] = True
                    print("Thank you. Payment complete. You have 15 minutes to leave")
                    self.updateSpots()

    def leaveGarage(self):
        if self.takenSpaces() == []:
            print("There are currently no cars in the garage.")
        else:
            print("Here is a list of all taken spaces: ")
            for spot in self.takenSpaces():
                print(f'{spot}: paid: {self.spaces[spot]["paid"]}')
            ticket = input("Please present your ticket: ").upper()
            if ticket not in self.takenSpaces():
                print("Sorry, try again.")
            else:
                if self.spaces[ticket]["paid"] == False:
                    commands = ["yes", "no"]
                    command = input(
                        "Sorry, that ticket isn't paid. Would you like to pay now? Enter 'Yes' or 'No': ").lower()
                    if command not in commands:
                        print("Sorry, try again.")
                    elif command == "yes":
                        self.payFromLeave(ticket)
                    elif command == "no":
                        print(
                            "Okay. But the ticket must be paid before you can exit.")
                elif self.spaces[ticket]["paid"] == True:
                    self.spaces[ticket]["paid"] = ''
                    self.spaces[ticket]["status"] = "open"
                    self.updateSpots()
                    print("Thank you! Have a nice day.")

    def payFromLeave(self, ticket):
        commands = ["cash", "card"]
        command = input("Will you be paying with Cash or Card?: ").lower()
        if command not in commands:
            print("Invalid response; try again.")
        else:
            self.spaces[ticket]["paid"] = True
            print("Thank you. Payment complete. You have 15 minutes to leave")
            self.updateSpots()

    def runGarage(self):
        while True:

            command = self.startMessage()

            if command == 'quit':
                print("Sorry to see you go!")
                break
            elif command == "enter":
                self.takeTicket()
            elif command == "pay":
                self.payForParking()
            elif command == "leave":
                self.leaveGarage()
            elif command == "come back later":
                self.generateGarage()


example = Garage()

# You must call generateGarage() before runGarage(). You will get a randomly generated garage on each 
# execution of the program. Akin to real life, garages are rarely completely empty when you enter them.
# It's even possible to generate a completely full garage; and in that case nobody may enter. They may
# only pay or leave!

example.generateGarage()
example.runGarage()