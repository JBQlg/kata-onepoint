from booking_system.flight import Flight


class Flight_handler : 
    def __init__(self):
        self.flights = []
    
    def __str__(self):
        flights = ""
        for flight in self.flights:
            flights += f"Flight {flight.id} : {flight.departure} to {flight.arrival} ({flight.date}) \n"
        return(flights)
    
    def create_flight(self, plane_id, departure, destination, schedule, date, reservations):
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
    
    