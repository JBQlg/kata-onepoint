

class Passenger:
    def __init__(self, passport_number,firstname, lastname, age ):
        if len(passport_number) != 9:
            raise ValueError("Passport number must be 9 characters long")
        if int(age) < 0:
            raise ValueError("Age must be positive")
        self.passport_number = passport_number # unique identifier
        self.firstname = firstname
        self.lastname = lastname
        self.age = age
        self.flights = [] # list of flights id the passenger booked
        # # allow to find easly his reservation
        
    def book_flight(self, flight_id):
        # check if the flight is already booked
        if flight_id in self.flights:
            raise ValueError("Flight  already booked by this passenger")
        self.flights.append(flight_id)
        
    def get_flights(self):
        return self.flights

    def __str__(self):
        return f"{self.firstname} {self.lastname} ({self.age}) - {self.passport_number}"
    
    def to_dict(self):
        """Convert Passenger object to a dictionary for JSON serialization."""
        return {
            "passport_number": self.passport_number,
            "firstname": self.firstname,
            "lastname": self.lastname,
            "age": self.age
        }
    
    @classmethod
    def from_dict(cls, data):
        """Create a Passenger object from a dictionary (JSON deserialization)."""
        return cls(
            passport_number=data["passport_number"],
            firstname=data["firstname"],
            lastname=data["lastname"],
            age=data["age"]
        )