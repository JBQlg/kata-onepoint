
import booking_system.utils as ut
from booking_system.passenger import Passenger
from booking_system.seat import Seat

class Reservation:
    _id_counter = 1
    
    def __init__(self, flight_id, passengers, seats) :
        if len(passengers) != len(seats):
            raise ValueError("The number of passengers and seats must be the same and not null")
        self.id = "RES"  + str(Reservation._id_counter)
        Reservation._id_counter += 1
        self.flight_id = flight_id # allow to find the instance of the flight in the flight
        self.passengers = passengers #list of passenger's instance
        self.seats = seats # instance of the seat for the reservation
        self.statut = "PENDING"
    
    def __str__(self) :
        # return the reservation in a string format, with all the information about the reservation including for each passengers
        tmp = f"Reservation {self.id} pour le vol {self.flight_id} :\n"
        for i, passenger in enumerate(self.passengers):
            tmp += f"Passager: {passenger} - Siège: {self.seats[i]} - Statut: {self.statut}\n"
        return tmp
        
    def confirm(self) :
        """This method will confirm the reservation and set the status to CONFIRMED
        """
        for seat in self.seats:
            seat.is_booked = True
        self.statut = "CONFIRMED"
        print(f"Reservation {self.id} confirmed")
        
    def cancel(self) :
        """This method will cancel the reservation and set the status to CANCELLED"""
        for seat in self.seats:
            seat.is_booked = False
        self.statut = "CANCELLED"
        print(f"Reservation {self.id} cancelled !")

    def to_dict(self):
        """Convert the Reservation object to a dictionary for JSON serialization."""
        return {
            "id": self.id,
            "flight_id": self.flight_id,
            "passengers": [passenger.to_dict() for passenger in self.passengers],  # Ensure Passenger has to_dict method
            "seats": [seat.to_dict() for seat in self.seats],  # Ensure Seat has to_dict method
            "statut": self.statut
        }
    
    @classmethod
    def from_dict(cls, data):
        """Create a Reservation object from a dictionary (JSON deserialization)."""
        passengers = [Passenger.from_dict(p) for p in data["passengers"]]
        seats = [Seat.from_dict(s) for s in data["seats"]]
        return cls(
            flight_id=data["flight_id"],
            passengers=passengers,
            seats=seats
        )