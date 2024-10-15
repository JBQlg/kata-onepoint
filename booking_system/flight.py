from booking_system.seat import Seat

class Flight: 
    _id_counter = 1
    def __init__(self, departure, arrival, date, schedule, plane_id, reservations=[]) :
        self.id = "FL"+str(Flight._id_counter)
        Flight._id_counter += 1
        self.departure = departure
        self.arrival = arrival
        self.date = date
        self.schedule = schedule
        self.plane_id = plane_id
        self.reservations = reservations
        

    def __str__(self):
        return f"Flight {self.id} : {self.departure} to {self.arrival} ({self.schedule}) on plane {self.plane_id}"
    
    def get_reservations(self):
        return self.reservation
    
    def is_seat_available(self, seat):
        # Check if the seat is already booked
        for resa in self.reservations:
            if resa.seat.row == seat.row and resa.seat.col == seat.col:
                return False
        return True
    
    def display_plane_plan(self, plane_list):
        # Fonction d'affichage du plan de l'avion 
        # on retrouve l'avion via l'id dans la liste fournie
        places_format = "      "
        for plane in plane_list:
            if plane.id == self.plane_id:
                #on a trouvé l'avion et ses dimensions 
                # création d'un header des places (A, B, C, D, E, F)
                for i in range(plane.col_nb):
                    places_format += f" {chr(65+i)} "
                places_format += "\n"
                # création des places, leur numéro de rangé adapté au header
                # et leur statut (libre (0) ou occupé (X)) sachant qu'on a la liste de réservation disponible
                nb_places = plane.row_nb * plane.col_nb
                # rappel : seat(row, col) colonne 1 = A, colonne 2 = B, colonne 3 = C, colonne 4 = D, colonne 5 = E, colonne 6 = F
                for i in range(plane.row_nb):
                    places_format += f"{i+1:2d}    "
                    for j in range(plane.col_nb):
                        seat = Seat(i+1, j+1)
                        for resa in self.reservations:
                            if seat.row == resa.seat.row and seat.col == resa.seat.col:
                                places_format += " X "
                                break
                        else:
                            places_format += " 0 "
                    places_format += "\n"
                print(places_format)
   