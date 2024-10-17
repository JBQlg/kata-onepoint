from booking_system.flight import Flight
from booking_system.utils import validate_date
class Flight_handler : 
    def __init__(self):
        self.flights = []
    
    def __str__(self):
        flights = ""
        for flight in self.flights:
            flights += f"{flight} \n"
        return(flights)
    
    def create_flight(self, plane_id, departure, destination, schedule, date, reservations):
        # checking inputs
        if not isinstance(plane_id, str):
            raise ValueError("plane_id must be a string")
        if not isinstance(departure, str) or not isinstance(destination, str):
            raise ValueError("departure and destination must be a string")
        validate_date(date)
        flight = Flight(plane_id=plane_id, departure=departure, arrival=destination, date=date, schedule=schedule, reservations=reservations)
        self.flights.append(flight)
        print(f"Flight {flight.id} created for {flight.departure} to {flight.arrival} on {flight.date}")
        return flight
    
    def delete_flight(self, id_flight):
        for flight in self.flights : 
            if flight.id == id_flight:
                self.flights.remove(flight)
                print(f"Flight {id_flight} deleted")
                return
        print(f"Flight {id_flight} not found")
    
    def get_flight(self, id_flight):
        for flight in self.flights : 
            if flight.id == id_flight:
                return flight
        print(f"Flight {id_flight} not found")
        return None
    
    @classmethod
    def from_dict(cls, data):
        """Create a Flight_handler object from a dictionary (JSON deserialization)."""
        handler = cls()
        handler.flights = [Flight.from_dict(flight_data) for flight_data in data]
        return handler