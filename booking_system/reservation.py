
import booking_system.utils as ut

class Reservation:
    _id_counter = 1
    
    def __init__(self, flight_id, passengers, seats) :
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
        for seat in self.seats:
            seat.is_booked = True
        self.statut = "CONFIRMED"
        print(f"Reservation {self.id} confirmed")
        
    def cancel(self) :
        for seat in self.seats:
            seat.is_booked = False
        self.statut = "CANCELLED"
        print(f"Reservation {self.id} cancelled !")
    