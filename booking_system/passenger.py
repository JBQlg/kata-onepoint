

class Passenger:
    def __init__(self, passport_number,firstname, lastname, age ):
        self.passport_number = passport_number # unique identifier
        self.firstname = firstname
        self.lastname = lastname
        self.age = age
        # self.flights = [] # list of flights id the passenger booked
        # # allow to find easly his reservation
        

    def book_flight(self, flight):
        self.flights.append(flight)

    def get_flights(self):
        return self.flights

    def __str__(self):
        return f"{self.firstname} {self.lastname} ({self.age}) - {self.passport_number}"