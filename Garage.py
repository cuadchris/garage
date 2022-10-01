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
            entry = input("*** GARAGE AT CAPACITY *** \n\nYou may 'Pay', 'Leave', or 'Come back later': ").lower()
        else:
            entry = input("*** GARAGE OPEN *** \n\nYou may 'Enter', 'Pay', or 'Leave': ").lower()

        return entry

    def takeTicket(self):

        if self.current_ticket != '':
            print("You currently have an open and unpaid ticket!")
        else:
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

    def payForParking(self):
        
        if self.spaces[self.current_ticket]["paid"] == True:
            print(f'Your ticket for {self.current_ticket} is already paid for. You may leave the garage.')
        else:
            response = input("Will that be cash or card?: ").lower()
            if response == "cash" or response == "card":
                self.spaces[self.current_ticket]["paid"] = True
                print("Your ticket is now paid! You have 15 minutes to leave.")

    def leaveGarage(self):
        if self.spaces[self.current_ticket]["paid"] == False:
            response = input("I'm sorry. It appears you haven't paid for your ticket. Would you like to pay now? 'Yes', or 'No: ").lower()
            if response == "yes":
                self.payForParking()
            elif response == "no":
                print("Okay. You may not leave unless payment is acquired.")
            else:
                print("Sorry, not a valid response.")
        else:
            self.spaces[self.current_ticket]["status"] = "open"
            self.spaces[self.current_ticket]["paid"] = ''
            self.current_ticket = ''
            print("Thank you, have a nice day!")
            return True

    def runGarage(self):

        commands = ["enter", "pay", "leave", "quit", "come back later"]

        while True:

            command = self.startMessage()

            if command not in commands:
                print(f'{command.title()} isn\'t a valid response! Try again.')
            elif command in commands and self.current_ticket == '' and command != "enter" and command != "leave":
                print("You don't currently have a ticket!")
            elif command == "enter":
                self.takeTicket()
            elif command == "pay":
                self.payForParking()
            elif command == "leave" and self.current_ticket == '':
                print("See ya!")
                break
            elif command == "leave":
                if self.leaveGarage():
                    break
            elif command == "come back later" and self.open_spots == 0:
                print("Sorry the garage is so busy! Try again later")
                self.generateGarage()
            elif command == "come back later":
                print("Sure thing, see you later!")









user = Garage()
user.generateGarage()
user.runGarage()
