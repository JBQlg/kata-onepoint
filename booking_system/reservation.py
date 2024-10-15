
import booking_system.utils as ut

class Reservation:
    _id_counter = 1
    
    def __init__(self, flight_id, passenger, seat) :
        self.id = "RES"  + str(Reservation._id_counter)
        Reservation._id_counter += 1
        self.flight_id = flight_id # allow to find the instance of the flight in the flight
        self.passenger = passenger
        self.seat = seat # instance of the seat for the reservation
        self.statut = "PENDING"
    
    def __str__(self) :
        return f"Reservation {self.id} for {self.passenger} on flight number :{self.flight_id} for seat :{ut.reverse_coordinates_converter(self.seat.row,self.seat.col)} ({self.statut})"
        
    def confirm(self) :
        self.seat.is_booked = True
        self.statut = "CONFIRMED"
        print(f"Reservation {self.id} confirmed")
        
    def cancel(self) :
        self.statut = "CANCELLED"
        self.seat.is_booked = False
        print(f"Reservation {self.id} cancelled !")
    