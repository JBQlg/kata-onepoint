from booking_system.seat import Seat
from booking_system.reservation import Reservation
from booking_system.utils import validate_date
class Flight: 
    _id_counter = 1
    def __init__(self, departure, arrival, schedule, date, plane_id, reservations=[]) :
        if plane_id is None or departure == "" or arrival == "" or date == "" or schedule == "":
            raise ValueError("All fields must be filled")
        # check date
        validate_date(date)
        self.id = "FL"+str(Flight._id_counter)
        Flight._id_counter += 1
        self.departure = departure
        self.arrival = arrival
        self.date = date
        self.schedule = schedule
        self.plane_id = plane_id
        self.reservations = reservations
        

    def __str__(self):
        return f"Flight {self.id} : {self.departure} to {self.arrival} ({self.date} - {self.schedule}) on plane {self.plane_id}"
    
    def is_seat_available(self, seat, planes):
        """This method checks if a seat is available for booking.

        Args:
            seat (seat): The seat to check
            planes (plane): List of planes to check 

        Returns:
            boolean : True if the seat is available and correct, False otherwise
        """
        for p in planes:
            if p.id == self.plane_id:
                if seat.row > p.row_nb or seat.col > p.col_nb:
                    return False
        for resa in self.reservations:
            for s in resa.seats:
                if s.row == seat.row and s.col == seat.col:
                    return False
        return True
    
    def display_plane_plan(self, plane_list):
        """ Display the plane plan for booking with the corridors.
            Display the available seats with a 0 and the booked seats with an X.
                    
        Args: plein_list ([plane]): plane list to get the plane from the plane_id
        
        return: str: string representing the plane plan
        """
        places_format = "      "  # Préparer la ligne de l'en-tête des colonnes (A, B, C, D, ...)
        
        # Recherche de l'avion dans la liste des avions à partir de son id
        for plane in plane_list:
            if plane.id == self.plane_id:
                # Avion trouvé, génération du plan de sièges
                col_nb = plane.col_nb
                
                # Déterminer la position du ou des couloirs selon le nombre de colonnes
                if col_nb > 6:
                    couloir1_pos = col_nb // 3
                    couloir2_pos = (col_nb * 2) // 3
                else:
                    couloir1_pos = col_nb // 2
                    couloir2_pos = None  # Pas de second couloir si moins de 6 colonnes
                
                # Création de l'en-tête avec les lettres de colonnes (A, B, C...)
                for i in range(col_nb):
                    places_format += f" {chr(65 + i)} "
                    if i == couloir1_pos - 1:
                        places_format += " | "  # Ajouter le premier couloir
                    if couloir2_pos and i == couloir2_pos - 1:
                        places_format += " | "  # Ajouter le second couloir (si applicable)
                places_format += "\n"

                # Parcourir chaque rangée
                for row in range(plane.row_nb):
                    places_format += f"{row + 1:2d}    "  # Ajoute le numéro de rangée (1, 2, 3...)
                    
                    # Parcourir chaque siège de la rangée
                    for col in range(col_nb):
                        seat = Seat(row, col)  # Créer un siège pour cette rangée et colonne
                        seat_found = False  # Indicateur pour savoir si le siège est réservé
                        
                        # Vérifier si ce siège est réservé dans une réservation
                        for resa in self.reservations:
                            if any(s.row == seat.row and s.col == seat.col and s.is_booked==True for s in resa.seats ):
                                places_format += " X "  # Siège occupé
                                seat_found = True
                                break

                        # Si le siège n'est pas trouvé dans les réservations, il est libre
                        if not seat_found:
                            places_format += " 0 "  # Siège libre
                        
                        # Ajouter le couloir dans l'affichage après la bonne colonne
                        if col == couloir1_pos - 1:
                            places_format += " | "  # Couloir 1
                        if couloir2_pos and col == couloir2_pos - 1:
                            places_format += " | "  # Couloir 2

                    places_format += "\n"
                
                # Afficher le plan complet
                print(places_format)
                return places_format
        print(f"Plane with ID {self.plane_id} not found.")

    def to_dict(self):
        """Convert the Flight object to a dictionary for JSON serialization."""
        return {
            "id": self.id,
            "departure": self.departure,
            "arrival": self.arrival,
            "date": self.date,
            "schedule": self.schedule,
            "plane_id": self.plane_id,
            "reservations": [reservation.to_dict() for reservation in self.reservations]
        }
    
    @classmethod
    def from_dict(cls, data):
        """Create a Flight object from a dictionary (JSON deserialization)."""
        flight = cls(
            departure=data["departure"],
            arrival=data["arrival"],
            date=data["date"],
            schedule=data["schedule"],
            plane_id=data["plane_id"]
        )
        # Charger les réservations
        flight.reservations = [Reservation.from_dict(resa_data) for resa_data in data.get("reservations", [])]
        return flight