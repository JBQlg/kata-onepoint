from booking_system.flight_handler import Flight_handler
from booking_system.plane_handler import Plane_handler
from booking_system.reservation_handler import Reservation_handler  

class BookingSystem: 
    """This class is the main class of the booking system. 
    It will handle the main menu and the different handlers.
    Each handler will handle the different actions of the system.
    This class make the interactions with the user and make the link between the different handlers.
    """
    def __init__(self):
        # create the different handlers
        self.flight_handler = Flight_handler()
        self.plane_handler = Plane_handler()
        self.reservation_handler = Reservation_handler()
    
    def display_menu(self):
        # display the main menu and return the choice of the user
        print("\n Menu Principal :")
        print("1. Faire une réservation")
        print("2. Afficher les vols")
        print("3. Modifier une réservation")
        print("4. Afficher les détails d'une réservation")
        print("5. Quitter")
        choix = input("Veuillez entrer votre choix : ")
        #check if the choice is valid
        while choix not in ["1", "2", "3", "4", "5"]:
            print("Choix invalide")
            choix = input("Veuillez entrer votre choix : ")
        return choix
    
    def modification_menu(self):
        # display the modification menu and return the choice of the user
        print("\n Que voulez-vous modifier ?")
        print("1. Modifier le passager")
        print("2. Modifier le siège")
        print("3. Annuler la réservation")
        print("4. Retour")
        choix = input("Veuillez entrer votre choix : ")
        #check if the choice is valid
        while choix not in ["1", "2", "3", "4"]:
            print("Choix invalide")
            choix = input("Veuillez entrer votre choix : ")
        return choix
    
    def main_menu_handler(self):
        # dispatch the user choice to the right handler or the correcti function
        while True:
            choix = self.display_menu()
            if choix == "1":
                # create a reservation
                self.flight_handler.flights = self.reservation_handler.create_reservation(self.flight_handler.flights, self.plane_handler.planes)
            elif choix == "2":
                print(self.flight_handler)
            elif choix == "3":
                self.flight_handler.flights = self.reservation_handler.modify_reservation(self.modification_menu(), self.flight_handler.flights, self.plane_handler.planes)
            elif choix == "4":
                self.reservation_handler.print_reservation_details(self.flight_handler.flights)
            elif choix == "5":
                break
            else:
                print("Choix invalide")
    
    
    def items_simulation(self):
        """This function create some items to simulate the system
        """
        # create some planes
        self.plane_handler.create_plane("Airbus A320", 10, 6)   
        self.plane_handler.create_plane("Boeing 747", 5, 4)
        self.plane_handler.create_plane("Airbus A380", 6, 5)
        self.plane_handler.create_plane("Boeing 787", 7, 6)
    
        #create some flights with those planes
        self.flight_handler.create_flight(plane_id=self.plane_handler.planes[0].id, departure="Paris", destination="New York", schedule="12:00", date="2021-07-01", reservations=[])
        self.flight_handler.create_flight(plane_id=self.plane_handler.planes[1].id, departure="Paris", destination="London", schedule="12:00", date="2021-07-02", reservations=[])
        self.flight_handler.create_flight(plane_id=self.plane_handler.planes[1].id, departure="Paris", destination="Madeira", schedule="8:00", date="2021-07-02", reservations=[])
        self.flight_handler.create_flight(plane_id=self.plane_handler.planes[2].id, departure="Paris", destination="Tokyo", schedule="15:00", date="2021-07-03", reservations=[])
        self.flight_handler.create_flight(plane_id=self.plane_handler.planes[3].id, departure="Paris", destination="Los Angeles", schedule="10:00", date="2021-07-04", reservations=[])
        
        # create some reservations
        # passenger1 = self.reservation_handler.build_passenger("123456789", "John", "Doe", 34)
        # passenger2 = self.reservation_handler.build_passenger("987654321", "Jane", "Doe", 32)
        # flight = self.reservation_handler.assign_seat(flight=self.flight_handler.flights[0], passenger=passenger1, seat="C5", list_planes=self.plane_handler.planes)    
        # flight = self.reservation_handler.assign_seat(flight=self.flight_handler.flights[0], passenger=passenger2, seat="D5", list_planes=self.plane_handler.planes)    
            
    
    
if __name__ == "__main__":
    booking = BookingSystem()
    
    # simulation des items pour tester le système
    print("Simulation des items : " )
    booking.items_simulation()

    # lancement du menu principal
    booking.main_menu_handler()
    
    print("Au revoir !")